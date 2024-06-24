from whale.models.component import Component
from whale.models.api import Api


def main():
    test_component = Component(name="test", description="test description", api_type=Api.GET)
    print(test_component)
    
if __name__ == "__main__":
    main()