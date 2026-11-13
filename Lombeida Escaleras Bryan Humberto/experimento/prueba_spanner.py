"""Prueba local de una transferencia atómica con el emulador de Spanner.

Ejecutar cada etapa por separado para conservar salidas y capturas originales.
No mide replicación, particiones ni rendimiento del servicio de producción.
"""

import argparse
import os

from google.cloud import spanner


PROJECT_ID = "ta-ind-01-local"
INSTANCE_ID = "spanner-bryan"
DATABASE_ID = "transferencias-bryan"
TABLE = "Cuentas"


class CancelacionDeliberada(Exception):
    """Interrumpe la transacción de prueba antes del commit."""


def get_database():
    if os.environ.get("SPANNER_EMULATOR_HOST") != "localhost:9010":
        raise SystemExit(
            "Antes de ejecutar, usa: export SPANNER_EMULATOR_HOST=localhost:9010"
        )
    client = spanner.Client(project=PROJECT_ID)
    config = f"{client.project_name}/instanceConfigs/emulator-config"
    instance = client.instance(INSTANCE_ID, configuration_name=config, node_count=1)
    return instance, instance.database(DATABASE_ID)


def show(database):
    with database.snapshot() as snapshot:
        rows = list(
            snapshot.execute_sql(
                "SELECT CuentaId, Titular, Saldo FROM Cuentas ORDER BY CuentaId"
            )
        )
    for cuenta_id, titular, saldo in rows:
        print(f"Cuenta {cuenta_id}: {titular}; saldo = {saldo}")
    print(f"Total de saldos = {sum(row[2] for row in rows)}")


def setup(instance, database):
    if not instance.exists():
        print("Creando instancia local...")
        instance.create().result(timeout=120)
    else:
        print("La instancia local ya existe.")

    if not database.exists():
        print("Creando base de datos y tabla...")
        database = instance.database(
            DATABASE_ID,
            ddl_statements=[
                "CREATE TABLE Cuentas ("
                "CuentaId INT64 NOT NULL, "
                "Titular STRING(100) NOT NULL, "
                "Saldo INT64 NOT NULL"
                ") PRIMARY KEY (CuentaId)"
            ],
        )
        database.create().result(timeout=120)
        with database.batch() as batch:
            batch.insert(
                table=TABLE,
                columns=("CuentaId", "Titular", "Saldo"),
                values=[(1, "Bryan", 100), (2, "Destino de prueba", 50)],
            )
        print("Datos iniciales insertados.")
    else:
        print("La base ya existe; no se reinician ni duplican los datos.")
    show(database)


def transfer(database, cancel):
    def work(transaction):
        rows = list(
            transaction.execute_sql(
                "SELECT CuentaId, Saldo FROM Cuentas ORDER BY CuentaId"
            )
        )
        balances = {row[0]: row[1] for row in rows}
        if balances.get(1) != 100 or balances.get(2) != 50:
            raise ValueError(
                "La prueba requiere saldos iniciales 100 y 50. "
                "Revisa los datos antes de repetirla."
            )
        transaction.update(
            table=TABLE,
            columns=("CuentaId", "Titular", "Saldo"),
            values=[
                (1, "Bryan", 90),
                (2, "Destino de prueba", 60),
            ],
        )
        if cancel:
            raise CancelacionDeliberada("Cancelación intencional antes del commit")

    print("Saldos antes:")
    show(database)
    try:
        database.run_in_transaction(work)
    except CancelacionDeliberada as error:
        print(error)
        print("La biblioteca ejecutó rollback; se verifican los saldos:")
    else:
        print("Commit completado; se verifican los saldos:")
    show(database)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paso", choices=("preparar", "consultar", "cancelar", "confirmar"))
    args = parser.parse_args()
    instance, database = get_database()
    if args.paso == "preparar":
        setup(instance, database)
    elif args.paso == "consultar":
        show(database)
    else:
        transfer(database, cancel=args.paso == "cancelar")


if __name__ == "__main__":
    main()
