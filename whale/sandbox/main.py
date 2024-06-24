from whale.application import Application
from whale.models.database.table import Column, DataType, Table


def main():
    
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
    
    application = Application(tables=user_profile_tables, api_key="test_key")
    
    print(application)
    
    
if __name__ == "__main__":
    main()