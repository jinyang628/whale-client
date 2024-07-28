import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table
from whale_client.models.manager import Manager


async def main():

    features_columns = [
        Column(name="title", data_type=DataType.STRING, nullable=False, unique=True),
        Column(name="description", data_type=DataType.STRING, nullable=True),
        Column(name="priority", data_type=DataType.INTEGER, nullable=True),
    ]

    bugs_columns = [
        Column(name="title", data_type=DataType.STRING, nullable=False, unique=True),
        Column(name="description", data_type=DataType.STRING, nullable=True),
        Column(name="priority", data_type=DataType.INTEGER, nullable=True),
    ]

    features_table = Table(
        name="features",
        description="This table stores the features",
        columns=features_columns,
        primary_key=PrimaryKey.AUTO_INCREMENT,
        enable_created_at_timestamp=True,
        enable_updated_at_timestamp=True,
    )
    bugs_table = Table(
        name="bugs",
        description="This table stores the bugs",
        columns=bugs_columns,
        primary_key=PrimaryKey.AUTO_INCREMENT,
        enable_created_at_timestamp=True,
        enable_updated_at_timestamp=True,
    )

    tasks_application_tables = [features_table, bugs_table]

    application_name = "featuring_bugs"

    application = Application(application_name, tasks_application_tables)

    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
