# Validating a Custom Artifact Value

Most of the built-in artifact types have some _value constraints_.  For example, you can't create an IP Address artifact that's not a valid IP address.  This is enforced by regular expressions in the Resilient server.

When you create a custom artifact type, you can add the same type of constraints, using script.

Here's an example using a company ID that must have 5 digits and alphanumeric format "AANNN" (two uppercase letters followed by three numbers).

## Custom Artifact

Customization Settings --> Artifacts --> Create a custom artifact.
* Name: "Company ID"
* Description: "A 5-digit company ID".

## Validation Script

Create a script
* Name: `validate_company_id`
* Object type: Artifact
```python
# Script for validating the value of a 'Company ID' artifact
import re

if len(artifact.value) != 5:
  helper.fail("Company ID must be exactly 5 characters.")

expr = re.compile('[A-Z]{2}\d{3}$')  # two letters, then three numbers, then end
if not expr.match(artifact.value):
  helper.fail("Company ID must be two letters followed by three numbers.")

```

## Validation Rule

Create a rule
* Name: `validate_company_id`
* Object type: Artifact
* Conditions: Type is equal to 'Company ID'
* Ordered Activities: run script 'validate_company_id'.

## Result

When adding a 'Company ID' artifact, if the value is not the correct format, it will fail.