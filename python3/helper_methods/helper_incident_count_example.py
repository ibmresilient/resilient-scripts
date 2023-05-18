# (c) Copyright IBM Corp. 2023. All Rights Reserved.

# query to get all existing incidents count 
query = query_builder.build()

# or you can build a query with filter/criteria
# for example this query finds all incidents which contains the word 'Phishing' in its name
#query = query_builder.contains(fields.incident.name, 'Phishing').build()

# returns the number of incidents matching the query
incidents_count = helper.getIncidentsCount(query)
log.info("incidents count = {}".format(incidents_count))

