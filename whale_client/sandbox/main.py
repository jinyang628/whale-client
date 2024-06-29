import asyncio
from whale_client.models.application import Application
from whale_client.models.table import Column, DataType, Table
from whale_client.models.manager import Manager


async def main():
    
    user_info_columns = [
        Column(name="name", data_type=DataType.STRING, nullable=False),
        Column(name="email", data_type=DataType.STRING, nullable=True)
    ]
    
    user_info_table = Table(name="user_info", description="This table stores the user information", columns=user_info_columns)
    
    usage_columns = [
        Column(name="name", data_type=DataType.STRING, nullable=False),
        Column(name="tokens", data_type=DataType.INTEGER, nullable=False),
    ]
    
    usage_table = Table(name="usage", description="This table stores the usage information", columns=usage_columns) 
    
    user_profile_tables = [user_info_table, usage_table]
    application_name = "user_management123"
    
    application = Application(application_name, user_profile_tables)
    
    manager = Manager()
    response: str = manager.commit(application=application)
    print(response)
    
    
if __name__ == "__main__":
    asyncio.run(main())