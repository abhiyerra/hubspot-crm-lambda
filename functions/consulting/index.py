import json
import requests
import os

print "New function"

hubspotUrl = "http://api.hubapi.com/contacts/v1/contact/createOrUpdate/email/{}/?hapikey={}"

def handler(event, context):
    hubspotApi = os.environ['HUBSPOT_API']
    url = hubspotUrl.format(event['email'], hubspotApi)

    # http://developers.hubspot.com/docs/methods/contacts/v2/get_contacts_properties
    properties = {
        "properties": [
            {
                "property": "firstname",
                "value": event["firstname"]
            },
            {
                "property": "lastname",
                "value": event["lastname"]
            },
            {
                "property": "company",
                "value": event["company"]
            },
            {
                "property": "lifecyclestage",
                "value": "opportunity"
            },
            # {
            #     "property": "message",
            #     "value": event["message"]
            # }
        ]
    }

    print json.dumps(properties)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    r = requests.post(url, data=json.dumps(properties), headers=headers)

    response = r.content
    print response
