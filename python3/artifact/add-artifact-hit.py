# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

# A script to add a hit to an artifact that you provide. 
# You must provide a name, value, and type for each property. 
# The type must be a string, number, uri, ip, or lat_lng. 
# This operation does not support the Observed Data artifact type, and is available in Python 3 only.

hit =[
            {
                "name": "Behavior",
                "type": "string",
                "value": "Ransomware (document-network-get-exe)"
            },
            {
                "name": "Scan Report",
                "type": "uri",
                "value": "https://threatintel.com/threat_report.pdf"
            },
            {
                "name": "Location",
                "type": "lat_lng",
                "value": {
                    "lat": 42.366,
                    "lng": -71.081}
            },
            {
                "name": "Resolved IP Address",
                "type": "ip",
                "value": "123.45.67.8"
            },
            {
                "name": "ASN Number",
                "type": "number",
                "value": "12345"
            }
    ]

artifact.addHit("Hits added via in-product script", hit)
