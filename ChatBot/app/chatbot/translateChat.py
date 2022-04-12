import requests, uuid, json

# Add your key and endpoint
key = "4f1aadf865e448ee940b48048a8a288f"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "Global"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['it']
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'Hello there'
},{
    'text': "Ok. Hallucinations and disorganization are common symptoms of schizophrenia. Please follow this link for more information, but you must see a doctor in order to get tested: https://www.nami.org/About-Mental-Illness/Mental-Health-Conditions/Schizophrenia"
},{
    'text': "I'm really sorry to hear that you are going through this but I am here for you. I think you might be depressed. Please see a doctor, if you would like more information please refer to the Wikipedia article in your console"
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))