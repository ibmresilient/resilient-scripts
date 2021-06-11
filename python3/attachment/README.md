# Attachment

This page describes the methods and fields available for use on the object type `attachment`. Each method has a simple example of how to use it.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> getParentObject() </summary>

  Returns the incident or task object that this artifact belongs to. The incident or task object can then be modified in the script.

  Example:
  ```python
  # close the task if the attachment is jpeg
  task = attachment.getParentObject()

  if 'jpeg' in attachment.content_type:
    task.status = 'C'
  ```
  </details>
  <!-- End of method -->

<!-- End of section -->
</blockquote>

<br>

## Fields

These are some of the fields available to an attachment. Depending on the parent object there may be additional fields. `log.info(attachment)` will display all available fields.

<details>
<summary>Show all fields</summary>

| Name | Display Name | Type | Notes |
|---|:---|:---|:---|
| content_type | Content Type | text |  |
| created | Date Created | datetimepicker | The date the attachment was created.  This field is read-only. |
| creator_id | Creator | select_user |  |
| name | Name | text |  |
| size | Size | number |  |

</details>
