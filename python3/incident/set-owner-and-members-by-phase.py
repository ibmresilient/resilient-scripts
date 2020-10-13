# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

# Script to set incident owner and members based on Incident Phase.
# To be run when the phase changes.

# Phase is a select field with API name `phase_id`,
# so the tests below are written as
#     if incident.phase_id == "value":

# Based on the current phase name, set a single Group or User as Incident Owner.
# NOTE:
#    When you change the owner of an incident, the previous owner is removed,
#    but also automatically added to Members so they still has access to the incident.
if incident.phase_id == 'Post-Incident':
    incident.owner_id = "Group_Name"
elif incident.phase_id == 'Some Other Phase':
    incident.owner_id = "User_Email@example.com"

# Based on the current phase name, add members to the incident.
# The list of members can include multiple groups and individual users.
# NOTE:
#    Here we **add** the new members to the existing list,
#    don't just overwrite the existing list (which would remove members)!
if incident.phase_id == 'Phase_Name':
    incident.members = list(incident.members) + \
        ["Group_Name", "User_Email@example.com"]
