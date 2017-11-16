# Set Timestamp

The general flow here is:
* Add an automatic or menu-item rule with the appropriate conditions,
* Rule runs the script that captures the current timestamp into a custom Time-Date field.

In this example,
a rule "Escalate to SIEM Admin" does two things:
1. Sets the incident owner to "SIEM Admin",
2. Runs this script below, which sets the value of the 'time_escalated_siem_admin' custom field.

*Note*  If you're capturing the [[last-modified timestamp]], there's a more extensive pattern for that.

```python
from java.util import Date
#
# Sets the timestamp field to the current time.
# Only set the timestamp if it is NOT already set.
#
if incident.properties.time_escalated_siem_admin is None:
   incident.properties.time_escalated_siem_admin = Date().time 
```

Resulting Field Value:
_Time Escalated SIEM Admin 06/09/2017 12:55:46_

## Capturing Durations (Time to Escalate, etc)

For durations, the recommended approach is
* Capture the timestamp (if something happened, the timestamp when it occurred).  This provides a positive data fact that can be analysed in many different ways.
* Use the dashboard "Date Difference" facility to present durations.  This is ideal for presenting dashboard pie-charts and other dashboard graphs that show the important durations.
* If there is a firm requirement to display durations in a list-view or in some other way, then *derive the duration* from the timestamps, at the time you calculate the timestamp.  But this is **not** a replacement for capturing the timestamps.
