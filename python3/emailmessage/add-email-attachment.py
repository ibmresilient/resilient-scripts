query = query_builder.equals(
    "id", "<replace this with an incident ID>").build()
# find the incident to associate it with
incidents = helper.findIncidents(query)
# Take the result from querybuilder and associate the top incident with the email message
if len(incidents) > 0:
    emailmessage.associateWithIncident(incidents[0])

# For each attachment in the email
for attachment in emailmessage.attachments:
    # Add an email attachment to incident
    emailAttachment = incident.addEmailAttachment(attachment.id)

assert incident.id
assert incident.name
