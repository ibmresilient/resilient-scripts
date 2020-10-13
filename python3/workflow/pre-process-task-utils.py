# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

# An example of using module importation from a pre-process script.
# Pre-process scripts are used for preparing the inputs that will be fed to a function
# This example shows how we can streamline the task-utils app with the inclusion of module imports

import json
#######################################
### Define pre-processing functions ###
#######################################
payload = {
    "required": True,
    "instr_text": "Close out this required Task",
    "phase_id": "Initial"
}

# prepare a JSON payload using above code;
inputs.task_utils_payload = json.dumps(payload)

# Take the incident id from this incident
inputs.incident_id = incident.id

inputs.task_name = "Perform Enrichment on Artifact {}".format(artifact.value)
