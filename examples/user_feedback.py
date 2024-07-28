import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table
from whale_client.models.manager import Manager


async def main():

    user_feedback_columns = [
        Column(name="name", data_type=DataType.STRING, nullable=False),
        Column(name="email", data_type=DataType.STRING, nullable=True),
        Column(name="feedback", data_type=DataType.STRING, nullable=True),
        Column(name="personal_notes", data_type=DataType.STRING, nullable=True),
    ]

    user_feedback_table = Table(
        name="feedback",
        description="This table stores the user feedback",
        columns=user_feedback_columns,
        primary_key=PrimaryKey.AUTO_INCREMENT,
        enable_created_at_timestamp=True,
        enable_updated_at_timestamp=True,
    )

    user_feedback_tables = [user_feedback_table]

    application_name = "user_feedback"

    application = Application(application_name, user_feedback_tables)

    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
