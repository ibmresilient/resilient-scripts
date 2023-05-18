[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![IBM Security](./IBM_Security_lockup_pos_RGB.png)

This directory contains python scripts which can be used by the in-product scripting feature showcasing working with context objects in python 3\. Each object type contains a README with detailed documentation about the methods and fields available for each object type.

## Module Importation

Module Importation is possible with the python 3 scripting feature and a number of modules are approved for use within the scripting runtime. For a full list of modules refer to the knowledge centre. Modules which attempt to make web requests or work with files are blocked by the runtime due to restrictions on network and file system access.

### Module Scripts

Provided are a number of scripts which demonstrate usage of modules in the python 3 scripting runtime. These scripts are :

+ email-artifact-parsing.py -- A Script which uses both the email and hashlib modules to work with an Email Message artifact file. Parses the email message and extracts artifacts from the parsed email. Any attachments found in the email message are hashed with the hashlib module and a MD5, SHA-1 and SHA-256 hash is stored.
+ malware-hash-matcher.py -- A script which uses hashlib to compare a hash artifact against a small blocklist of known malware hashes. If a match is found, the parent incident is updated with a warning the severity is set to High.

### Pre-process and post-process scripts for workflow function

Provided are two scripts that show how module imports can be used in pre- and post-process scripts for workflow functions.

+ `pre-process-task-utils.py` -- This script is a simple demonstration of using the json module in a pre-process script. A custom payload dictionary is converted into a json string and added to the inputs object for further processing in a task_utils workflow function.
+ `post-process-whois.py` -- This script makes use of the json module to easily parse and format the results coming from the fn_whois workflow function. The BeautifulSoup module is then used to enrich the incident by preparing an incident note with a rich text format.

## Context Objects

The Resilient in-product script runtime contains a representation of business objects present in the system which provide context for a script to perform operations based on contains or to update the respective business objects. Provided are a number of example scripts for working with context objects:

+ Incident
  + `automated-incident-closure.py` -- Combine with an automatic rule to close an incident based on some conditional info in that incident
  + `fail-based-on-incident-fields.py` -- Combine with an automatic rule to prevent the closure of an Incident unless certain incident field info is populated
  + `set-owner-and-members-by-phase.py` -- Script to set the owner and members of an incident based on a specific incident phase. Allows for incident handoff to another group or individual once a specific phase has been complete
  + `set-owner-and-members-by-type.py` -- Script to set owners and members to an incident based on the incident type. Automatically assign incident to the relevant team or individual based on what type of incident this is
+ Task
  + `assign_task_to_current_user_on_close.py` -- When an task is completed auto assign it to the user who closed the task. Prevent the closure of the task if the principal user is neither the task owner nor an incident member
  + `restrict_task_assignment.py` -- Prevent the assignment of a task to any user unless that user is a member of a permitted group
  + `task_due_7_days_from_now.py` -- Set the due date of the task to 7 days from the current time
  + `task_due_in_24hours_from_determineddate.py` -- Set the due date of the task to 24 hours from the incident's determined date field
+ Email Message
  + `add-email-attachment.py` -- associates the email message with an existing incident and adds all existing email attachments to the incident.
  + `associated-with-incident.py` -- Script which uses the  helper context object to find incidents and then associates the email message with an incident returned from the query.
  + `create-associated-incident.py` -- Script which creates a new incident which will be associated with the email message the script is ran on. Further changes to this new incident can be made in the script.
  + `get-body-html-raw.py` -- Script that gets the full raw html body of an email message.
  + `email_sample_script.py` -- This the Python 3 version of the email sample script.
+ Datatable
  + `datatable-addrow-onincident.py` -- Adds a row to a datatable of an incident and fills the columns with values.

## Query_Builder

+ `simple_query_builder_example.py` -- This script showcases the query_builder helper object and how to use it for querying incidents.
+  `helper_query_builder_start_length_example.py` -- This script showcases the query_builder helper object and how to use it for querying incidents and, limit the results returned with start and length.

