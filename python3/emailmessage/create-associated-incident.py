# Create a new associated incident
emailmessage.createAssociatedIncident("My new incident", "admin@co3sys.com")

# Incident can have further changes made to it.
incident.city = "Galway"

# You cannot call createAssociatedIncident twice
try:
    emailmessage.createAssociatedIncident(
        "My new incident 2", "admin@co3sys.com")
except Exception as e:
    log.info(
        "Scripting server caught the error as expected. Message {}".format(str(e)))
else:
    helper.fail("Associating with Incident called twice did not throw an error.")
