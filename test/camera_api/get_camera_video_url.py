import requests
from PIL import Image
from io import BytesIO
from flask import send_file
import os


def get_camera_video_url(camera_id, token):
    url = f"https://na-api.beta.inrix.com/Traffic/Inrix.ashx?Action=GetTrafficCameraVideoURL&Token={token}&CameraID={camera_id}&ImageWidth=720&ImageHeight=480"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response)
    return response


if __name__ == '__main__':
    token = os.getenv("INRIX_TOKEN", "")
    if not token:
        raise SystemExit("Please set INRIX_TOKEN in environment before running this script.")
    get_camera_video_url(976, token)