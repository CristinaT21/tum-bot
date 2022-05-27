import requests
import urllib3

from pyfacebook import GraphAPI

USER_API_TOKEN = "EAAXulEsjZAMEBAOkeP1dBMzZB4mrG3JSZBlv4zZBCeu4yKL43ZArMNT89HwBQ6psCSPQpZAZBN1guW5ZBF8B2cnpnN5Cyrs5kzjMDlI6l2FHH4j9ncRp8buhSYDjlxp1OgaWr19enLOqltiJ1uZAuU1ZBu9YeRPIhoC2hNOl2pxPYAe9ZCVWc3QhZANRbaFtuAEFXZCmfvdqXzP4ohEK4UWXXZAmln"

graph_api_instance = GraphAPI(access_token=USER_API_TOKEN)
# Not able do get event object.
# events = graph_api_instance.get_object(object_id="event", fields="poetry")

