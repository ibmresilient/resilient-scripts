# Incident "Closed By" Report

When closing an incident, it can be useful to save key data points for reporting.  In particular, it's often useful to report on closed incidents grouped by the user who closed them.

This information is available in the incident audit history and newsfeed, but is not easily available to the Analytics Dashboard.

The script and rule below show how to automatically record the person who closes an incident in a custom field.


## Create a Custom Field

In __Customization Settings__, add a new text field: "Closed By", with API name `closed_by`.

This field will be used to hold the user name for reporting.


## Create the Script

Create a script
* Name: `closed_by`
* Object type: Incident
```python
# Set the 'closed_by' field to the current user.
# Should be called from an automatic rule, when the incident is closed.

# Scripts that run from a timer will run as "system", ignore these
if principal.type != "user":
  log.error("Cannot run as '{}' {}".format(principal.type, principal.display_name))

else:
  # Set closed_by to the current user
  incident.properties.closed_by = principal.display_name
```

## Create an Automatic Rule

To use this script, create a rule that runs this script automatically when an incident is closed.
* Object type: Incident
* Condition: Status is changed to Closed
* Activity: Run Script


## Create the Dashboard

In __Dashboards > Analytics Dashboard__, add a Custom Incident Widget.  You can choose any type, for example a simple Pie Chart.

In the widget filters, select Status: Closed.  Drag the `closed_by` field into the appropriate axis, and save.

