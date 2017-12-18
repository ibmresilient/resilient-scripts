# Set Task Owner When Closed

When working with tasks in an incident, its's very common for an analyst to review and close a series of Tasks without being explicitly assigned these tasks.  Nevertheless, the traceability benefits of task assignment are important for reporting and process improvement.

The script and rule below show how to automatically assign a task to the person who closes it, if the task was not already assigned to anyone.

## Create the Script

Create a script
* Name: `assign_task`
* Object type: Task
```python
# If the task is not assigned: assign to the current user.
# Should be called from an automatic rule, when task is closed.

if not task.owner_id:
  
  # Scripts that run from a timer will run as "system", ignore these
  if principal.type != "user":
    log.error("Cannot run as '{}' {}".format(principal.type, principal.display_name))

  else:
    # Set the task owner to the current user
    task.owner_id = principal.id

    # add a note of ownership change
    task.addNote("Task Owner has been changed to " + principal.display_name)
```

## Create an Automatic Rule

To use this script for every task, create a rule that runs this script automatically when a task is closed.
* Object type: Task
* Condition: Task Status is changed to Closed
* Activity: Run Script

Alternatively, you could run the script from workflows, after specific tasks are completed.


