import requests

from indeed import IndeedClient

CLIENT_ID = "ebe5f221b125151724de4686bc242b78a647519e52c4522737e59fe247828ae0"
CLIENT_SECRET = "uNJsGq9jaykrcPCpl2hpiPp8A6c6sAhwadTjPClrAZuXNkjKv9ztPmu4X1mPhcEy"

API_TOKEN_METHOD = "POST"
API_TOKEN_URL = "https://apis.indeed.com/oauth/v2/tokens"
API_TOKEN_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}
API_TOKEN_FIELDS = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "grant_type": "client_credentials",
}

APP_ENDPOINT_URL = "https://secure.indeed.com/v2/api/appinfo"


def get_api_token():
    response = requests.post(API_TOKEN_URL, headers=API_TOKEN_HEADERS, data=API_TOKEN_FIELDS)

    return response.json()


def get_app_info(api_token):
    request_headers = {
        "Authorization": api_token["token_type"] + " " + api_token["access_token"]
    }

    response = requests.get(APP_ENDPOINT_URL, headers=request_headers)

    return response.json()


api_token_object = get_api_token()
print(get_app_info(api_token_object))

# NOT IMPLEMENTED

# indeed_client = IndeedClient(publisher=PUBLISHER_ID)
#
# parameters = {
#     "q": "python developer",
#     "l": "Location",
#     "sort": "date",
#     "fromage": "X",
#     "limit": "Y",
#     "filter": "Z"
# }
