import uuid
import requests


subscription_key = ""
endpoint = "https://api.cognitive.microsofttranslator.com"

location = ""

path = "/translate"
constructed_url = endpoint + path

params = {"api-version": "3.0", "from": "en", "to": ["tr"]}
constructed_url = endpoint + path

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Ocp-Apim-Subscription-Region": location,
    "Content-type": "application/json",
    "X-ClientTraceId": str(uuid.uuid4()),
}


def translate(texts: list):
    body = [{"text": text} for text in texts]
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response
