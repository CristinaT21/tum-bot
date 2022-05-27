import requests

from flask import Flask, request

from conversational_model.main import generate_response

app = Flask(__name__)

FACEBOOK_API_URL = "https://graph.facebook.com/v2.6/me/messages"
VERIFY_TOKEN = "9lPJjW+tNsN5b/8xcQI5OA5Gydr3qEpqxzWjVd1fe28="
PAGE_ACCESS_TOKEN = "EAAXulEsjZAMEBAIEPQ4yZAabeduEVTEhcYUGSVk2mimiofZCzx8X71HDwMkTE1ge59c7dpZBfzZAKMnPZBzfZBznv8Bq88LYLlCCnjEYZC374mPZBPixefKvukSvf4z63uPsX8ICWZBK9ZCNZBZA6zJ9EQRJHKbAK3pqG0Kv5kyGt6COVk9AFftUyt6gT"


def get_bot_response(message):
    return generate_response(message)


def verify_web_token(incoming_request):
    if incoming_request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return incoming_request.args.get("hub.challenge")
    else:
        return "Incorrect token"


def respond(sender, message):
    response = get_bot_response(message)
    send_message(sender, response)


def send_message(recipient_id, text):
    payload = {
        "message": {
            "text": text
        },
        "recipient": {
            "id": recipient_id
        },
        "notification_type": "regular"
    }

    auth = {"access_token": PAGE_ACCESS_TOKEN}

    response = requests.post(FACEBOOK_API_URL, params=auth, json=payload)

    return response.json()


def is_user_message(message):
    return message.get("message") and message["message"].get("text") and not message["message"].get("is_echo")


@app.route('/')
def hello_world():
    return request.args.get("hub.challenge")


@app.route("/webhook", methods=["GET", "POST"])
def listen():
    if request.method == "GET":
        return verify_web_token(request)

    if request.method == "POST":
        payload = request.json
        event = payload["entry"][0]["messaging"]
        for x in event:
            if is_user_message(x):
                text = x["message"]["text"]
                sender_id = x["sender"]["id"]
                respond(sender_id, text)

        return "ok"


if __name__ == "__main__":
    app.run(host="localhost", port=5002)
