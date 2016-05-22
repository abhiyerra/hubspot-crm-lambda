# hubspot-crm-lambda

Create a serverless form for collecting lead information from a web
form and putting it into [HubSpot CRM](hubspot.com). Check out
[an example on the Acksin site](https://www.acksin.com/consulting).

## Usage

1. Modify `project.json` and update the role.
1. Get Apex.
1. `apex deploy -s HUBSPOT_API=apikey consulting`
1. Include form.html in your site. Make sure to install the AWS Lambda.
