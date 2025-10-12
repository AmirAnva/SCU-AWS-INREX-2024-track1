import time
import requests
import json
import schedule
from unittest.mock import patch



# Mock function for testing
def mocked_get_token():
    url = "https://na-api.beta.inrix.com/Traffic/Inrix.ashx?Action=GetSecurityToken&vendorId=1680049421&consumerId=3466e4ef-329b-474f-b52b-a3818e9df6b6&format=json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    token = json.loads(response.text)["result"]["token"]
    print("Token: " + token)
    return token


def test_schedule():
    # Patch the `get_token` function to mock behavior
    with patch("__main__.mocked_get_token", side_effect=mocked_get_token) as mock_function:
        # Schedule the mocked function every 5 seconds (for testing purposes)
        schedule.every(5).seconds.do(mock_function)

        print("Test started. Waiting for the scheduled function to execute...")
        execution_count = 0
        start_time = time.time()

        # Run the scheduler for 20 seconds
        while time.time() - start_time < 20:  # Run the test for 20 seconds
            schedule.run_pending()
            time.sleep(1)
            # Count the executions of the mocked function
            execution_count = mock_function.call_count

        print(f"Mocked `get_token` executed {execution_count} times.")

        # Assert that the function executed at least 3 times in 20 seconds
        assert execution_count >= 3, "Scheduled function did not execute as expected."
        print("Test passed!")


if __name__ == "__main__":
    test_schedule()
