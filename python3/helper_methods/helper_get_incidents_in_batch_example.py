# (c) Copyright IBM Corp. 2023. All Rights Reserved.

# query to return existing incidents
#query = query_builder.build()

# or you can filter and sort the incidents that are returned
# for example this query finds all incidents which contains the word 'Phishing' in its name and sorts them by discovered_date
# if no sorting order specified, retuned results are sorted by the incident id

query = query_builder.contains(fields.incident.name, 'Phishing').sortByAscending(fields.incident.discovered_date).build()

# this returns the number of incidents matching the query
incidents_count = helper.getIncidentsCount(query)

# you can use the count to fetch the incident data in batches e.g., batch size 10 
batch_size = 10

# iterate over the incidents and access their data such as id, name, etc.,
batch_itr = range(0, incidents_count, batch_size)
for next in batch_itr:
  query_builder.start(next)
  query_builder.length(batch_size)
  query = query_builder.build()
  results = helper.findIncidents(query)
  for inc in results:
    log.info("incident id = {}, name = {}".format(inc.id, inc.name))

