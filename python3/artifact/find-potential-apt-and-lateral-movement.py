# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

from datetime import datetime, timezone

# Convert timestamp to datetime string
first_seen_utc = datetime.fromtimestamp((artifact.global_info.first_associated_time)/1000, timezone.utc)
last_seen_utc = datetime.fromtimestamp((artifact.global_info.last_associated_time)/1000, timezone.utc)

incident.addNote("Artifact: " + str(artifact.value) + "\n"
                              "First Seen is " + str(first_seen_utc) + "\n"
                              "Last Seen is " + str(last_seen_utc) + "\n"
                              "The Relate Case count is " + str(artifact.global_info.related_incident_count))

diff = artifact.global_info.last_associated_time - artifact.global_info.first_associated_time
# If the time gap is over 1 year
if diff > 31556926:
  artifact.addTags(["Potential_APT"])

# If the artifact is seen in multiple incidents
if artifact.global_info.related_incident_count > 3:
  artifact.addTags(["Lateral_Movement"])
  
if artifact.containsTag("Potential_APT") and artifact.containsTag("Lateral_Movement"):
  incident.severity_code = "High"
