import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table, ForeignKey
from whale_client.models.manager import Manager


async def main():

    accelerator_columns = [
        Column(name="name", data_type=DataType.STRING, nullable=False, unique=True),
        Column(
            name="applied",
            data_type=DataType.BOOLEAN,
            nullable=False,
            default_value=False,
        ),
        Column(name="status", data_type=DataType.STRING, nullable=True),
        Column(name="contact", data_type=DataType.STRING, nullable=True),
        Column(name="opening_date", data_type=DataType.DATE, nullable=True),
        Column(name="deadline", data_type=DataType.DATE, nullable=True),
    ]

    # Define the columns for the feedback table
    feedback_columns = [
        Column(
            name="application_name",
            data_type=DataType.STRING,
            nullable=False,
            foreign_key=ForeignKey(table="accelerator_applications", column="name"),
        ),
        Column(name="feedback", data_type=DataType.STRING, nullable=True),
        Column(name="notes", data_type=DataType.STRING, nullable=True),
    ]

    # Create the accelerator_applications table
    accelerator_table = Table(
        name="accelerator_applications",
        description="This table stores accelerator application data",
        columns=accelerator_columns,
        primary_key=PrimaryKey.AUTO_INCREMENT,
        enable_created_at_timestamp=True,
        enable_updated_at_timestamp=True,
    )

    # Create the feedback table
    feedback_table = Table(
        name="feedback",
        description="This table stores feedback data for accelerator applications",
        columns=feedback_columns,
        primary_key=PrimaryKey.AUTO_INCREMENT,
        enable_created_at_timestamp=True,
        enable_updated_at_timestamp=True,
    )

    accelerator_application_tables = [accelerator_table, feedback_table]

    application_name = "accelerators"

    application = Application(application_name, accelerator_application_tables)

    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
