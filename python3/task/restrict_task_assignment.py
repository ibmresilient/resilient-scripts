# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

permitted_Groups = ["L1", "L2", "Threat Hunters"]
permitted = False
# For each permitted group
for group in permitted_Groups:
    if groups.findByName(group):
        log.info("you are member of {}".format(group))
        permitted = True
    else:
        log.info("you are not member of {}".format(group))


if permitted:
    log.info("You are allowed")
else:
    log.info("You are not allowed")
    helper.fail("You are not allowed")
