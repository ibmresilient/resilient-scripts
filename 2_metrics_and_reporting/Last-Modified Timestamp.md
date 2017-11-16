# Last-Modified Timestamp

Use a script to capture the "last-modified" timestamp.

Out of the box, Resilient incidents do not have a 'last modified' field.  But this is a common requirement, for reporting, and for displaying in a list-view (e.g. so you can show incidents that haven't been touched in a while).

## Triggering the rule
Trigger this from an **automatic** rule, on an Incident, with no conditions.
Additionally you can execute the same rule from a Note, Task, etc. if you want to capture those events too.

In this script we use a custom field named `time_incident_modified`.  This should be a Date-Time field (not a text field)!

## Capture other timestamps in the same script
Because the incident was just modified, this is a good time to capture "the first time XXX happened" in additional timestamp-fields.  The example below shows how to do this for a few conditions:  the first time that the incident was set to severity 1, and so on.

## Capturing durations

Generally: don't store durations.  They're useless.

If you want "minutes since last modified": sorry, you can't do that.  The value of your minutes-since-last-modified field will only be updated when the incident is modified, which defeats the point.  You could use notifications to alert when not modified within a given period.

Displaying durations on the dashboard can be done easily with "date difference".  If you really really need to calculate and store a duration between two events, that's OK, but should only be done where "date difference" isn't good enough.


## Phase Change is different
You can use this to capture the timestamp of a phase change.  But phase change is done in two steps:  the tasks are marked complete or incomplete, and the system has an asynchronous background job that updates the Phase field to reflect the task completion.  These two steps make it possible to do some smarter stuff with phase change.  [[Rob-update-your-thing-here]].

---

```python
from java.util import Date
time_now = Date().time

# Capture the last modification timestamp
incident.properties.time_incident_modified = time_now

# In this example our severity code values are:
# 4 - Severe
# 3 - High
# 2 - Medium
# 1 - Low
log.info(incident.severity_code)

if incident.severity_code in [ "1 - Low", "2 - Medium" ]:
   if incident.properties.time_severity_1_or_2 is None:
      incident.properties.time_severity_1_or_2 = time_now

if incident.severity_code in [ "3 - High", "4 - Severe" ]:
   if incident.properties.time_severity_3_or_4 is None:
      incident.properties.time_severity_3_or_4 = time_now

```
