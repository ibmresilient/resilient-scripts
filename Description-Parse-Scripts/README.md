# Parsing Values from the Incident Description

When an incident is received from an external source, or when you have a large body of text
pasted into an incident field, it can be very useful to parse values from the field automatically.

For example, the inbound Email connector works by receiving an incident by mail, then parsing the subject, description, and other fields to assign the incident, create artifacts, and so on.

This parsing function can be done by in-product scripts.  Then the parsing will apply to all incidents, regardless their source: email, Splunk, manually created, and so on.

> _Note_: the email connector has other functions that can't be replaced by these scripts.  The most important is that it can choose whether to update an existing incident, or create a new incident, for example by lookup to determine whether an incident already exists for some values in the subject of the email.

> The parser language in Email connector is JavaScript, and product scripting is Python, so there are some differences in how the script is written.

An example below searches the incident description for URLs, IP addresses and a MD5 hash, and creates various artifacts from them.

## Create the Script

Create a script
* Name: `parse_description`
* Object type: Incident
```python
# Parse values from the incident description.
import re
body = incident.description.content

# The body content is HTML rich text.  For many purposes it will be easier to
# deal with plaintext, so here's a rough-and-ready way to strip HTML tags:
plain_body = re.compile(r'(<([^>]+)>)', re.IGNORECASE | re.MULTILINE ).sub("\n", body).strip()

# The plain body may still include HTML entities, so let's fix them
# - at least the five XML entities &quot; &apos; &amp; &lt; &gt;
entities = {"&quot;": "\"", "&apos;": "'", "&gt;": ">", "&lt;": "<", "&amp;": "&"}
plain_body = re.compile('|'.join(entities.keys())).sub(lambda e: entities[e.group(0)], plain_body)

# Now let's start hunting for things we want
# (This uses artifacts... you could add notes or data-table rows in a similar way)
# Be careful to only find artifacts that have a valid format, otherwise Resilient will reject them!
artifacts = []
url_regex = r'(?:http|https|file|gopher|ftp):\/\/[^\'" >]+'
ip_regex = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
md5_regex = r'(?:0x)?[a-fA-F0-9]{32}'
sha1_regex = r'(?:0x)?[a-fA-F0-9]{40}'
sha256_regex = r'(?:0x)?[a-fA-F0-9]{64}'
host_regex = r'[a-zA-Z0-9\-.]+'

def between(text, start, end):
  # find whatever is between 'start' and 'end'
  return re.findall(r'(?s)' + start + '(.*?)' + end, body, re.MULTILINE)

# Find specific things in the plaintext body
# This example is looking for the format typically used in a FireEye alert, like this:
#    explanation: 
#      malware-detected: 
#        malware (name:PUA.Win.Packer.Upx-49): 
#          type: exe
#          md5sum: e64d95129d28d0086807504afaa5e4f7
#          executed-at: 2017-07-01T07:07:07Z
#    src: 
#      vlan: 2419
#      ip: 10.17.139.235
#      host: dchimxt1160kr.corp.example.com
#      port: 64276
#      mac: 00:2b:6a:8c:ea:c3
#    dst: 
#      ip: 69.196.228.80
#      mac: 00:c0:bd:28:50:7e
#      port: 443
#    occurred: 2017-07-01T07:08:09Z

for url in re.findall(r'href=[\'"]?(' + url_regex + ')', body):
  artifacts.append({"type": "URL", "value": url, "description": "Parsed from description"})

for md5 in re.findall(r'md5sum:\s(' + md5_regex + ')', plain_body):
  artifacts.append({"type": "Malware MD5 Hash", "value": md5, "description": "md5sum (from FireEye)"})

for substring in between(plain_body, "src", "dst"):
  for ip in re.findall(r'ip:(?:\s*)(' + ip_regex + ')', substring):
    artifacts.append({"type": "IP Address", "value": ip, "description": "Source IP (from FireEye)"})
  for host in re.findall(r'host:(?:\s*)(' + host_regex + ')', substring):
    artifacts.append({"type": "DNS Name", "value": host, "description": "Source Host (from FireEye)"})

for substring in between(plain_body, "dst", "occurred"):
  for ip in re.findall(r'ip:(?:\s*)(' + ip_regex + ')', substring):
    artifacts.append({"type": "IP Address", "value": ip, "description": "Destination IP (from FireEye)"})

# Now add the artifacts to the incident
for artifact in artifacts:
  incident.addArtifact(artifact.get("type"), artifact.get("value"), artifact.get("description"))
```

## Create the Rule

The rule should trigger the script only once.  There are a few alternative ways to do this:
* Use a condition such as "when the description is changed".  This is easiest.
* Use a hidden field as a "flag".  For example, create a custom time/date field named `description_was_processed`.  In the script, set the value to `Date().time`.  In the rule, use a condition "description_was_processed does not have a value".


