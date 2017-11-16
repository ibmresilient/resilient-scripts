# Set Owner and Members by Incident Type

This script will set Incident Owner and Incident Members, based on the Incident Type of the incident.  For example, when the incident type is "CSIRT", the script can change the owner to the group responsible for critical incidents, and add the team manager to the members.

## Create the Script

This script is named "Set Owner And Members For Incident Type", and object type is "Incident".

```python
# Script to set incident owner and members based on Incident Type(s).
# To be run when the incident type changes.

# Incident type is a multi-value field with API name `incident_type_ids`, 
# so the tests below are written as
#     if "value" in incident.incident_type_ids:

# Based on the current incident type(s), set a single Group or User as Incident Owner.
# NOTE:
#    When you change the owner of an incident, the previous owner is removed,
#    but also automatically added to Members so they still has access to the incident.
if "CSIRT" in incident.incident_type_ids:
  incident.owner_id = "CSIRT_Group_Name"
if "Some Other Type" in incident.incident_type_ids:
  incident.owner_id = "User_Email@example.com"

# Based on the current incident type(s), add members to the incident.
# The list of members can include multiple groups and individual users.
# NOTE:
#    Here we **add** the new members to the existing list,
#    don't just overwrite the existing list (which would remove members)!
if "Malware" in incident.incident_type_ids:
   incident.members = list(incident.members) + ["Another_Group_Name", "User_Email@example.com"]
```

## Create the Rule

To trigger this script when the incident type is changed,
* Create an automatic Rule for the incident
* Conditions: when Incident Type is changed
* Ordered activities: Run Script "Set Owner And Members For Incident Type".
