# First User

When an incident is created automatically from QRadar, email, or from some other source, its creator is the “integration account”.  

For team metrics, we need a way to record the user who was responsible for this update.  Ideally this should be displayable in the List Incidents view so that it can be easily exported for reporting and displayed in dashboards.  But that information may not be readily available from the source system.

One way to track this is by
* Who was the first person assigned a task?  (This should usually be the first analyst working on the incident).
* Who first wrote a note on the incident?  (For example the analyst recording triage).
* Who first edited the incident details?  __Note__ In v28 it is not yet possible to record the "user who edited an incident" directly using Scripts.  (That limitation should be addressed in future release).  But even when that becomes possible, we need to be careful to distinguish between the integration user and the editor!

This is done with a combination of rules and scripts.
First create a custom text field, `who_first_edited`.


### Note script and rule

* Make  a script, named `who_first_edited_note`,
  * Description: "Record the user who first added a note to the incident"
  * Object type: Note

```python
# Record the user who first added a note to the incident
#
# This script should be run from an Automatic rule on a Note.
#
# If the incident does not yet record a value for custom field "who_first_edited",
# record the note's "user_id" (the email address of the note author).

if not incident.properties.who_first_edited:
  incident.properties.who_first_edited = note.user_id
```

* Make an Automatic Rule, named `who_first_edited_note`,
  * Object type: Note
  * Condition: "Who First Edited" does not have a value.
  * Ordered Activity: Run Script "who_first_edited_note".


### Task script and rule

* Make  a script, named `who_first_edited_task`,
  * Description: "Record the user who was first assigned a task in the incident"
  * Object type: Task

```python
# Record the user who was first assigned a task in the incident
#
# This script should be run from an Automatic rule on a Task.
#
# If the incident does not yet record a value for custom field "who_first_edited",
# and if the task is assigned,
# record the task's "owner_id" (the email address of the task assignee).

if not incident.properties.who_first_edited:
  if task.owner_id:
    incident.properties.who_first_edited = task.owner_id
```

* Make an Automatic Rule, named `who_first_edited_task`,
  * Object type: Task
  * Condition: Task "Owner" was changed.
  * Ordered Activity: Run Script "who_first_edited_task".


Voilà!  Now the first analyst working on the incident can be tracked automatically.
