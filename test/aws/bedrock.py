import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
import get_byte_image
import requests
import json
import random
import schedule
import time
import xml.etree.ElementTree as ET

def get_token():
    print("Generating Token...")
    url = "https://na-api.beta.inrix.com/Traffic/Inrix.ashx?Action=GetSecurityToken&vendorId=1680049421&consumerId=3466e4ef-329b-474f-b52b-a3818e9df6b6&format=json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    token = json.loads(response.text)["result"]["token"]
    print("Token is: " + token)
    return token

def get_camera_info(xml):
    cameras = []
    for camera in xml.findall(".//Camera"):
        camera_id = camera.get("id")
        point = camera.find("Point")
        latitude = point.get("latitude")
        longitude = point.get("longitude")
        cameras.append({"id": camera_id, "latitude": latitude, "longitude": longitude})
    return cameras

def get_cameras_in_a_box(token, corner1, corner2):
    url = f"https://na-api.beta.inrix.com/Traffic/Inrix.ashx?action=GetTrafficCamerasInBox&locale=en-US&corner1={corner1}&corner2={corner2}&token={token}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    root = ET.fromstring(response.text)
    camera_info = get_camera_info(root)

    # print(camera_info)
    return camera_info

def generate_random_coordinates():
    latitude = round(random.uniform(-90, 90),6)
    longitude = round(random.uniform(-180, 180),6)
    return f"{latitude}|{longitude}"

if __name__ == "__main__":
    load_dotenv()
    token = get_token()
    corner1 = generate_random_coordinates()
    corner2 = generate_random_coordinates()
    print("corner1: ", corner1)
    print("corner2: ", corner2)
    camera_list = get_cameras_in_a_box(get_token(), corner1, corner2)
    first_location = camera_list[0]
    print("First Camera id is: ",first_location["id"])
    image_b = get_byte_image.get_camera_image_in_bytes(first_location["id"], token)

    # Put your AWS credentials in a .env file
    access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    client = boto3.client(
        service_name="bedrock-runtime",
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name="us-west-2",
    )

    # The model ID for the model you want to use
    model_id = "us.anthropic.claude-3-sonnet-20240229-v1:0"

    # The message you want to send to the model
    # user_message = "How many traffic lights do you see? Describe the traffic in the image."
    system_prompt = ("Generate a JSON response with the following fields: "
                    "- Status: (integer) to represent an HTTP status code. "
                    "- Content: An object with fields: "
                    "- Congestion: (1 for yes, 0 for no)."
                    "- Car Accident: (1 for yes, 0 for no)."
                    "- Weather: (string) to describe the weather condition. (NA for no information) "
                    "Ensure the response follows this format.")

    conversation = [
        {
            "role": "user",
            "content": [{
                "image": {
                    "format": 'png',
                    "source": {
                        "bytes": image_b
                    }
                }}
            ],

        }
    ]

    try:
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
            system=[{
                'text': system_prompt
            }]
        )

        response_text = response["output"]["message"]["content"][0]["text"]
        print(response_text)
    except (ClientError, Exception) as e:
        print(f"ERROR: {e}")