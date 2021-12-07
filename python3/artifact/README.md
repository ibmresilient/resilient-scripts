# Artifact

This page describes the methods and fields available for use on the object type `artifact`. Each method has a simple example of how to use it.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> getParentObject() </summary>

  Returns the incident object that this artifact belongs to. The incident object can then be modified.

  Example:
  ```python
  incident = artifact.getParentObject()

  incident.addNote("Artifact type is: {}".format(artifact.type))
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> addHit() </summary>

  Adds a hit to an artifact that you provide. You must provide a name, value, and type for each property. The type must be a string, number, uri, ip, or lat_lng.    This operation does not support the Observed Data artifact type.

  Example:
  ```python
  hit =[
            {
                "name": "Behavior",
                "type": "string",
                "value": "Ransomware (document-network-get-exe)"
            }
       ]

  artifact.addHit("Hit added via in-product script", hit)
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> addTags() </summary>

  Adds one or more tags to an artifact, except for the Observed Data artifact type.

  Example:
  ```python
  artifact.addTags(['Tag1', 'Tag2'])
  ```
  </details>
  <!-- End of method -->
  
  <!-- Start of method -->
  <details><summary> getAllTags() </summary>

  Returns the artifact's tags, except for the Observed Data artifact type.

  Example:
  ```python
  artifact.getAllTags()
  ```
  </details>
  <!-- End of method -->
  
  <!-- Start of method -->
  <details><summary> containsTag() </summary>

  Returns those artifacts with the tags you specify. It does not return tags from artifacts with the type of Observed Data.

  Example:
  ```python
  artifact.containsTag("Tag1")
  ```
  </details>
  <!-- End of method -->
  
  <!-- Start of method -->
  <details><summary> removeTags() </summary>

  Deletes one or more tags to from artifact, except for the Observed Data artifact type.

  Example:
  ```python
  artifact.removeTags(['Tag1', 'Tag2'])
  ```
  </details>
  <!-- End of method -->
  
<!-- End of section -->
</blockquote>

<br>

## Fields

These are the fields available on the artifact context object. Not all of these fields are writable.

<details>
<summary>Show all fields</summary>

| Name | Display Name | Type | Notes |
|---|:---|:---|:---|
| attachment | Attachment | nested_collection |  |
| created | Date Created | datetimepicker |  |
| description | Description | textarea |  |
| global_info.first_associated_time | First seen | datetimepicker | First associated times is the First Seen properties |
| global_info.last_associated_time | Last seen | datetimepicker | Last associated times is the Last Seen properties |
| global_info.related_incident_count | Related incident count | number | Incident count shows the number of incidents that are impacted by the artifact |
| global_info.relating_incidents | Relating incidents | boolean | Relating incidents is the option to show or hide the related incidents |
| global_info.scan_option | Scan threat source | select | Scan option is the setting to send or not send the artifact to a threat source |
| global_info.summary | Summary | text | Summary is the text that describes the artifact |
| hits | Threat Source Hits | none | Returns the number of matches with intelligence threat feeds |
| id | Artifact ID | number |  |
| inc_id | Incident ID | number |  |
| ip.destination | Destination | boolean |  |
| ip.source | Source | boolean |  |
| last_modified_time | Last Modified | datetimepicker |  |
| relating | Relating | boolean | Returns true if the artifact is configured to show a relationship between incidents when they contain the same artifact |
| type | Type | select |  |
| value | Value | text |  |

</details>
