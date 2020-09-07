# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

if not task.owner_id:
  if principal.type != "user":
    log.error("Cannot run as '{}' {}".format(principal.type, principal.display_name))

  if (principal.name != incident.owner_id) and (principal.name not in incident.members):
    helper.fail("You must be an Owner or Member of an Incident to close Tasks.")

  else:
    task.owner_id = principal.id

task.addNote("Task has been closed by " + principal.display_name)