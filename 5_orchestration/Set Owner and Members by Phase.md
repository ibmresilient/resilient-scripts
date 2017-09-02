# Set Owner and Members by Phase

This script will set Incident Owner and Incident Members, based on the Phase of the incident.  For example, when the incident phase changes to "Post-Incident", you may want the owner to be changed to a group responsible for after-action notification and review.

## Create the Script

This script is named "Set Owner And Members For Phase", and object type is "Incident".

```python
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
   incident.members = incident.members + ["Group_Name", "User_Email@example.com"]
```

## Create the Rule

To trigger this script when the phase of the incident is changed,
* Create an automatic Rule for the incident
* Conditions: when Phase is changed
* Ordered activities: Run Script "Set Owner And Members For Phase".