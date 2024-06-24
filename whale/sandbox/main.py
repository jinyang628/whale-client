from whale.models.component import Component
from whale.models.database.api_manager import ApiManager


def main():
    test_component = Component(name="test", description="test description", api_manager=ApiManager)
    print(test_component)
    
if __name__ == "__main__":
    main()