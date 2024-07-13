import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table
from whale_client.models.manager import Manager


async def main():

    features_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(name="title", data_type=DataType.STRING, nullable=False),
        Column(name="description", data_type=DataType.STRING, nullable=True),
        Column(name="priority", data_type=DataType.INTEGER, nullable=True),
    ]

    bugs_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(name="title", data_type=DataType.STRING, nullable=False),
        Column(name="description", data_type=DataType.STRING, nullable=True),
        Column(name="priority", data_type=DataType.INTEGER, nullable=True),
    ]

    features_table = Table(
        name="features",
        description="This table stores the features",
        columns=features_columns,
    )
    bugs_table = Table(
        name="bugs",
        description="This table stores the bugs",
        columns=bugs_columns,
    )

    tasks_application_tables = [features_table, bugs_table]

    application_name = "featuring_bugs"

    application = Application(application_name, tasks_application_tables)

    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
