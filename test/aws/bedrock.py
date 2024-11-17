import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
import get_byte_image
import random
import json

def Chat(i):
    load_dotenv()
    #random_number = random.randint(1, 1500)

    # Put your AWS credentials in a .env file
    access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    inrix_token = os.getenv("INRIX_TOKEN")

    image_b = get_byte_image.get_camera_image_in_bytes(i, inrix_token)

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
    system_prompt = (
        "Analyze a traffic image and generate a JSON response with the following fields: "
        "- Status: (integer) HTTP status code representing the analysis result. "
        "  Use 200 for successful analysis, 400 for bad input, or 500 for server errors. "
        "- Content: An object containing: "
        "  - Congestion: (1 for yes, 0 for no). If the congestion level is 70% or higher, round up to 1; otherwise, round down to 0. "
        "  - Car Accident: (1 for yes, 0 for no). If the likelihood of a car accident is 90% or higher, round up to 1; otherwise, round down to 0. "
        "  - Weather: (string) describing the weather condition visible in the image, e.g., 'clear,' 'rainy,' 'foggy,' or 'snowy.' "
        "Ensure that the response adheres to the JSON format. "
        "Example responses: "
        "{"
        '  "Status": 200, '
        '  "Content": {'
        '    "Congestion": 1, '
        '    "Car Accident": 0, '
        '    "Weather": "rainy" '
        "  }"
        "} "
        "{"
        '  "Status": 400, '
        '  "Content": {'
        '    "Congestion": 0, '
        '    "Car Accident": 0, '
        '    "Weather": "unknown" '
        "  }"
        "} "
        "Base the analysis on the image content only. Use probability thresholds explicitly when deciding values."
    )


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
        data = json.loads(response_text)
        result = { 'Camera ID': f'{i}', **data }
        response_text = json.dumps(result)
        return response_text, image_b
    except (ClientError, Exception) as e:
        #print(f"ERROR: {e}")
        return f"ERROR: {e}"

