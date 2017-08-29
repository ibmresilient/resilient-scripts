# Conditionally-Required Fields

To make a field "conditionally required": create a script that produces an error, and run the script when the conditions should reject the value of your field.

## Simple Version
In the simple version, the script contains any complex validation conditions, and the failure message for this particular validation.  Then a rule triggers the script when appropriate.

For example,
* Make a script named 'Validate Incident Name', with script code to validate the field:
```python
# Validate that incident name does not contain 'X'
if 'X' in incident.name:
    helper.fail("The name must not contain 'X'.")
    
# Validate length of the incident name
if len(incident.name) > 100
    helper.fail("The name must be less than 100 characters.")
```
* Make a rule for your condition.  
    * Automatic rule for an Incident
    * Conditions: incident name is changed.
    * Ordered activity: run script "Validate Incident Name".
    
With this approach, you'll end up with one script for each specific field validation.  This can lead to more maintanance work,
but also allows each script to include advanced conditions that can't be expressed in
a rule.

## Generic Version
In the generic version, the script is completely general-purpose: it just produces an error.  The rules then contain **all** the validation conditions.  This can be much easier to maintain, if used consistently.

To do this,
* Make a custom text field named `validation_failure_message`.  (Don't add this to your layouts).
* Make a script named 'Validation Failure', which simply fails.  When it fails, this will show a dialog with the contents of the `validation_failure_message` field.
```python
# Fail, with an error message.
# The failure message is in the custom field 'validation_failure_message'
#
helper.fail(incident.properties.validation_failure_message)
```
* Make a rule for your condition.  For example,
    * Automatic rule for an Incident
    * Conditions: incident name contains X.
    * Ordered Activity #1: set field 'validation_failure_message' to: "The name must not contain X".
    * Ordered Activity #2: run script "Validation Failure".

Then you can repeat this style of rule for any other conditions you need, each with a custom message.

Note that the 'validation failure message' is never saved into the incident.  The script aborts saving before that happens!