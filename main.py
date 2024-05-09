import requests
import json


def main() -> None:
    print("1. Fetch current weather data for a given latitude and longitude")
    print("2. Fetch current weather data in a locality/city")
    while True:
        choice = int(input("Enter which current data do you require (1 or 2): "))
        if choice in [1, 2]:
            data_fetcher(choice)
            break
        else:
            print("Enter a valid option")


def data_fetcher(choice) -> None:
    if choice == 1:
        print("Enter the correct co-ordinate details")
        print()
        latitude = float(input("Enter the correct latitude : "))
        longitude = float(input("Enter the correct longitude : "))
        api_handler(choice, latitude, longitude)

    else:
        print("Thane West code is : ZWL005442")
        region = input("Enter the locality/city : ")
        api_handler(choice, region, 0)


def api_handler(choice, latitude, longitude):
    headers = {"x-zomato-api-key": "ce3682540ecbf4ea14725372560c35a1"}
    if choice == 1:
        # url = f"https://weatherunion.com/gw/weather/external/v0/get_weather_data?latitude={latitude}&longitude={longitude}"
        response = requests.request("GET", url, headers=headers)
        data_handler(response)
    else:
        # url = f"https://weatherunion.com/gw/weather/external/v0/get_weather_data?locality_id={latitude}"
        # url = "https://weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id=ZWL007666"
        url = "https://weatherunion.com/gw/weather/external/v0/get_locality_weather_data?locality_id=ZWL005442"
        response = requests.request("GET", url, headers=headers)
        data_handler(response)


def data_handler(api_response):
    print(json.dumps(api_response.json(), indent=2))


if __name__ == "__main__":
    main()
