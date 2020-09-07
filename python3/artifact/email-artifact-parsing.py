# A script to parse an email message and add artifacts to the incident corresponding to certain message headers and contents.

# Import the email modules we'll need
from email.parser import Parser
from email.policy import default
import hashlib


def storeHashes(the_data: bytes, the_description: str):
  """
  A function to add a number of hashes of the data in the_data parameter as artifacts of the incident. Each artifact will have a description combining the name of the hash with the_description parameter.
  """
  
  incident.addArtifact("Malware MD5 Hash", hashlib.md5(the_data).hexdigest(), "MD5 {}".format(the_description))
  incident.addArtifact("Malware SHA-1 Hash", hashlib.sha1(the_data).hexdigest(), "SHA1 {}".format(the_description))
  incident.addArtifact("Malware SHA-256 Hash", hashlib.sha256(the_data).hexdigest(), "SHA256 {}".format(the_description))

  
headers = Parser(policy=default).parsestr(artifact.value)

# Extract the fundamental aspects of the email as artifacts
incident.addArtifact("Email Recipient", '{}'.format(headers['to']), "Email Recipient")
incident.addArtifact("Email Sender", '{}'.format(headers["from"]), "Email Sender")
incident.addArtifact("Email Subject", '{}'.format(headers['subject']), "Email Subject")
incident.addArtifact("Email Recipient", '{}'.format(headers['to'].addresses[0].username), "Email Recipient username")
incident.addArtifact("Email Sender Name", headers['from'].addresses[0].display_name, "Email Sender")

# Proess the body of the email message
the_body = headers.get_body()
incident.addArtifact("Email Body", str(the_body), "Suspicious email body")


# For each email attachment, add its hashes as artifacts to the incident
if the_body['content-type'].maintype == 'text':
    body = the_body.get_body(preferencelist=('html'))

    for part in body.iter_attachments():
      incident.addArtifact("Email Attachment Name", part.get_filename(), "Suspicious email attachment name")
      storeHashes(part.get_content(), " of suspicious email attachment")

elif the_body['content-type'].content_type == 'multipart/related':
    body = the_body.get_body(preferencelist=('html'))
    for part in the_body.iter_attachments():
      incident.addArtifact("Email Attachment Name", part.get_filename(), "Suspicious email attachment name")
      storeHashes(part.get_content(), " of suspicious email attachment")
