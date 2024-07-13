import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table, ForeignKey
from whale_client.models.manager import Manager


async def main():

    tasks_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(name="title", data_type=DataType.STRING, nullable=False),
        Column(name="description", data_type=DataType.STRING, nullable=True),
        Column(
            name="assigned_to",
            data_type=DataType.STRING,
            nullable=True,
            foreign_key=ForeignKey(table="whales", column="whales"),
        ),
        Column(name="priority", data_type=DataType.STRING, nullable=True),
        Column(name="status", data_type=DataType.STRING, nullable=True),
    ]

    whales_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(name="whales", data_type=DataType.STRING, nullable=False, unique=True),
    ]

    tasks_table = Table(
        name="tasks", description="This table stores the tasks", columns=tasks_columns
    )
    whales_table = Table(
        name="whales",
        description="This table stores the whales working on tasks",
        columns=whales_columns,
    )

    tasks_application_tables = [tasks_table, whales_table]

    application_name = "tasks"

    application = Application(application_name, tasks_application_tables)

    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
