import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, PrimaryKey, Table
from whale_client.models.manager import Manager


async def main():

    user_info_columns = [
        Column(
            name="id",
            data_type=DataType.INTEGER,
            nullable=False,
            primary_key=PrimaryKey.AUTO_INCREMENT,
        ),
        Column(name="name", data_type=DataType.STRING, nullable=False),
        Column(name="email", data_type=DataType.STRING, nullable=True),
    ]

    user_info_table = Table(
        name="user_info",
        description="This table stores the user information",
        columns=user_info_columns,
    )

    user_profile_tables = [user_info_table]
    application_name = "huge_whale"

    application = Application(application_name, user_profile_tables)

    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
