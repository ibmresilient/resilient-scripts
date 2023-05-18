# (c) Copyright IBM Corp. 2023. All Rights Reserved.

# query to return the first 10 existing incidents 
# results returned are limited to the server configured maximum retuned incidents (e.g., 1000) if length is not specified or less than 0 
# returns error if length value is greater than the server configured maximum retuned incidents value
query_builder = query_builder.start(0)
query_builder.length(10)

# or you can filter and sort the incidents that are returned
# for example this query finds all incidents which contains the word 'Phishing' in its name and sorts them by discovered_date
# if no sorting order specified, results retuned are sorted by the incident id
# query = query_builder.contains(fields.incident.name, 'Phishing').sortByAscending(fields.incident.discovered_date).build()

query = query_builder.build()

## Execute the query, this returns any matching incidents
incidents_array = helper.findIncidents(query)

# iterate over the incidents and access their data such as id, name etc
for inc in incidents_array:
  log.info("incident id = {}, name = {}".format(inc.id, inc.name))
    
# this query will return 2 matching incidents starting from 10.
query_builder = query_builder.start(10)
query_builder.length(2)

incidents_array = helper.findIncidents(query)

# iterate over the incidents and access their data such as id, name etc
for inc in incidents_array:
  log.info("incident id = {}, name = {}".format(inc.id, inc.name))

