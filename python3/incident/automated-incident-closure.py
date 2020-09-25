if incident.confirmed == False:
    incident.resolution_id = "Not an Issue"
    # This portion will take the original incident title and description and throw them to notes.
    incident.resolution_summary = "This was determined not to be an issue based on automated Resilient rules, and was closed."
    # Because the IF statement implies a false positive finding, the title and description are changed to reflect that
    title = helper.createRichText(incident.name)
    desc = helper.createRichText(incident.description.content)
    falsePos = "<b > This incident was determined not to be an issue based on automated Resilient rules and was closed < /b > <br > <br > The original title/name and description have been placed under Notes for record keeping."
    incident.addNote("Original Title/Name: " + title.content)
    incident.addNote("Original Description: " + desc.content)
    incident.name = "False Positive"
    # log.info(str(incident.resolution_summary.content))
    incident.description = falsePos

if incident.resolution_summary is None:
    incident.resolution_summary = principal.display_name + \
        " has yet to provide the appropriate resolution information."
if not incident.resolution_id:
    incident.resolution_id = "Resolved"
    incident.plan_status = "C"
