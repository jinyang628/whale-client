import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table, ForeignKey
from whale_client.models.manager import Manager


async def main():

    accelerator_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(name="name", data_type=DataType.STRING, nullable=False),
        Column(
            name="applied", data_type=DataType.BOOLEAN, nullable=True, default=False
        ),
        Column(name="status", data_type=DataType.STRING, nullable=True),
        Column(name="contact", data_type=DataType.STRING, nullable=True),
        Column(name="opening_date", data_type=DataType.DATE, nullable=True),
        Column(name="deadline", data_type=DataType.DATE, nullable=True),
    ]

    feedback_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(
            name="application_id",
            data_type=DataType.INTEGER,
            nullable=False,
            foreign_key=ForeignKey(table="accelerator_applications", column="id"),
        ),
        Column(name="feedback", data_type=DataType.STRING, nullable=True),
        Column(name="notes", data_type=DataType.STRING, nullable=True),
    ]

    accelerator_table = Table(
        name="accelerator_applications",
        description="This table stores the accelerator applications",
        columns=accelerator_columns,
    )

    feedback_table = Table(
        name="feedback",
        description="This table stores the feedback related to accelerator applications",
        columns=feedback_columns,
    )

    accelerator_application_tables = [accelerator_table, feedback_table]

    application_name = "accelerators"

    application = Application(application_name, accelerator_application_tables)

    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
