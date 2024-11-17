import requests
import json
import schedule
import time

# refreshed every hour
def get_token():
    print("Generating token...")
    url = "https://na-api.beta.inrix.com/Traffic/Inrix.ashx?Action=GetSecurityToken&vendorId=1680049421&consumerId=3466e4ef-329b-474f-b52b-a3818e9df6b6&format=json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    token = json.loads(response.text)["result"]["token"]
    print("Token: " + token)
    return token


if __name__ == '__main__':
    get_token()


    # Schedule the `get_token` function to run every hour
    # schedule.every(1).hours.do(get_token)

    # print("Scheduler started. Calling `get_token` every hour...")
    #
    # # Keep the script running
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)