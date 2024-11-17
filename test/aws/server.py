from flask import Flask, Response, request, jsonify, render_template_string
from bedrock import Chat
from PIL import Image
from io import BytesIO
import base64


app = Flask(__name__)

@app.route("/<count>") #count is how many images we want, starting from ID=1 to ID=count
def output(count):
    d={}
    for i in range(1, 1+int(count)):
        text, img =  Chat(i)
        img_base64 = base64.b64encode(img).decode('utf-8')
        d[text] = img_base64
   
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat Output</title>
    </head>
    <body>
        <h1>Chat Output</h1>
        {% for text, img_base64 in d.items() %}
            <div style="margin-bottom: 20px;">
                <p>{{ text }}</p>
                <img src="data:image/jpeg;base64,{{ img_base64 }}" alt="Chat Image" style="max-width: 100%; height: auto;"/>
            </div>
        {% endfor %}
    </body>
    </html>
    """

    return render_template_string(html_template, d=d)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
