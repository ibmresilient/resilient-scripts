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
| global_artifact.tags | Tags | multiselect_tagref |  |
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
