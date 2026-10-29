
import json

from api_client import APIClient
from data_parser import UserParser


def main():
    client = APIClient(
        "https://jsonplaceholder.typicode.com"
    )
    parser = UserParser()

    try:
        raw_data = client.fetch_user(1)
        clean_data = parser.parse(raw_data)

        print("Clean user data:")
        print(json.dumps(clean_data, indent=4))

        with open("user.json", "w", encoding="utf-8") as file:
            json.dump(clean_data, file, indent=4)

        print("\nData saved to user.json")

    except (ValueError, TypeError, OSError) as error:
        print(f"Application error: {error}")

    except Exception as error:
        print(f"API request failed: {error}")


if __name__ == "__main__":
    main()
