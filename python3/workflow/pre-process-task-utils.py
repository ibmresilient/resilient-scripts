""" An example of using module importation from a pre-process script.
    Pre-process scripts are used for preparing the inputs that will be fed to a function
    This example shows how we can streamline the task-utils app with the inclusion of module imports
    """
import json
#######################################
### Define pre-processing functions ###
#######################################
payload = {
    "required": True,
    "instr_text": "Close out this required Task",
    "phase_id": "Initial"
}

# def dict_to_json_str(d):
#   """Function that converts a dictionary into a JSON stringself.
#     Supports basestring, bool and int.
#     If the value is None, it sets it to False"""

#   json_str = '"{ {0} }"'
#   json_entry = '"{0}":{1}'
#   json_entry_str = '"{0}":"{1}"'
#   entries = []

#   for entry in d:
#     key = entry
#     value = d[entry]


#     if value is None:
#       value = False


#     if isinstance(value, basestring):
#       entries.append(json_entry_str.format(key, value))

#     elif isinstance(value, bool):
#       value = 'true' if value == True else 'false'
#       entries.append(json_entry.format(key, value))

#     else:
#       entries.append(json_entry.format(key, value))

#   return '{' + ','.join(entries) + '}'
# prepare a JSON payload using above code;
inputs.task_utils_payload = json.dumps(payload)

# Take the incident id from this incident
inputs.incident_id = incident.id

inputs.task_name = "Perform Enrichment on Artifact {}".format(artifact.value)
