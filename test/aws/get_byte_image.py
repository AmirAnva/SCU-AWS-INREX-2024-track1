import requests
from PIL import Image
from io import BytesIO
from IPython.display import display

def get_camera_image_in_bytes(camera_id, token):
    url = f"https://na-api.beta.inrix.com/Traffic/Inrix.ashx?Action=GetTrafficCameraImage&Token={token}&CameraID={camera_id}&DesiredWidth=640&DesiredHeight=480"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    image = Image.open(BytesIO(response.content))
    #image.show()
    img_io = BytesIO()
    image.save(img_io, "JPEG")
    img_io.seek(0)

    return img_io.read()