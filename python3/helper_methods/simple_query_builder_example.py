# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

# this query will return all existing incidents
query = query_builder.build()

# or you can filter and sort the incidents that are returned
# for example this query finds all incidents who's name contains the word 'Phishing' and sorts them by discovered_date
# query = query_builder.contains(fields.incident.name, 'Phishing').sortByAscending(fields.incident.discovered_date).build()

# Execute the query, this returns any matching incidents
incidents_array = helper.findIncidents(query)

# you can use slicing to get the first 10 incidents (or less if less than 10 were found)
# https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
first_10_incidents = incidents_array[:10]

# iterate over the incidents and access their data such as id, name etc
for i in first_10_incidents:
    log.debug(i.id)
    log.debug(i.name)
