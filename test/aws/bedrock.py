import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
import get_byte_image
import random


load_dotenv()
random_number = random.randint(1, 1500)
image_b = get_byte_image.get_camera_image_in_bytes(1050, "KSj2WVkxo3DeamYUTPh5K-E04KiMJ0AHBbUu5ZqbUO0|")

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
        "- Weather: (string) to describe the weather condition. "
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
            'text':system_prompt
        }]
    )


    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)
except (ClientError, Exception) as e:
    print(f"ERROR: {e}")
