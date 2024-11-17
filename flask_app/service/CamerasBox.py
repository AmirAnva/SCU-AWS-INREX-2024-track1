import requests
import xml.etree.ElementTree as ET

import Token
import random


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

    print(camera_info)
    return camera_info

def generate_random_coordinates():
    latitude = round(random.uniform(-90, 90),6)
    longitude = round(random.uniform(-180, 180),6)
    return f"{latitude}|{longitude}"

if __name__ == "__main__":
    # corner1 and corner2 are strings in the format "latitude|longitude"
    corner1 = generate_random_coordinates()
    corner2 = generate_random_coordinates()
    print("corner1: ",corner1)
    print("corner2: ",corner2)
    camera_list = get_cameras_in_a_box(Token.get_token(), corner1, corner2)
    first_location = camera_list[0]
    print(first_location["id"])

