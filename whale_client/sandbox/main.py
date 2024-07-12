import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table
from whale_client.models.manager import Manager


async def main():

    user_feedback_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(name="user_id", data_type=DataType.STRING, nullable=False),
        Column(name="application_name", data_type=DataType.STRING, nullable=False),
        Column(name="feedback", data_type=DataType.STRING, nullable=True),
        Column(name="personal_notes", data_type=DataType.STRING, nullable=True),
    ]

    user_feedback_table = Table(
        name="feedback",
        description="This table stores the user feedback",
        columns=user_feedback_columns,
    )

    user_feedback_tables = [user_feedback_table]

    application_name = "user_feedback"

    application = Application(application_name, user_feedback_tables)

    manager = Manager()
    response: str = manager.commit(application=application)

if __name__ == "__main__":
    asyncio.run(main())
