# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

# Validate that incident name does not contain 'X'
if 'X' in incident.name:
    helper.fail("The name must not contain 'X'.")

# Validate length of the incident name
if len(incident.name) > 100:
    helper.fail("The name must be less than 100 characters.")
