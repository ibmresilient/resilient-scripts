# Milestone

This page describes the methods and fields available for use on the object type `Milestone`. Each method has a simple example of how to use it.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> getParentObject() </summary>

  Returns the incident object that this milestone belongs to. The incident object can then be modified.

  Example:
  ```python
  incident = milestone.getParentObject()

  incident.addNote("Milestone title is: {}".format(milestone.title))
  ```
  </details>
  <!-- End of method -->

<!-- End of section -->
</blockquote>

<br>

## Fields

placeholder

<details>
<summary>Show all fields</summary>

| Name | Display Name | Type | Notes |
|---|:---|:---|:---|
| date | Date | datetimepicker |  |
| description | Description | textarea |  |
| title | Title | text |  |

</details>
