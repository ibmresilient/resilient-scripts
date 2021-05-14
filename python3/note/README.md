# Note

This page describes the methods and fields available for use on the object type `note`. Each method has a simple example of how to use it.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> addNote(text) </summary>

  Adds a reply to the note with the given text. Returns a Note object for further customization.

  `text: string or TextObject`

  Example:
  ```python
  note.addNote(helper.createRichText('<h1>Rich text</h1></br>Newline'))
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> getParentObject() </summary>

  Returns the parent object that this note belongs to, incident or task. The parent object can then be modified.

  Example:
  ```python
  # gets the incident parent object and adds a new top level note
  incident = note.getParentObject()

  incident.addNote('New top level note')
  ```
  </details>
  <!-- End of method -->

<!-- End of section -->
</blockquote>

<br>

## Fields

These are the fields available on a Note Object Type.

<details>
<summary>Show all fields</summary>

| Name | Display Name | Type | Notes |
|---|:---|:---|:---|
| create_date | Date Created | datetimepicker | The date the note was created.  This field is read-only. |
| mentioned_users | Mentioned users | multiselect_members | returns a list of users mentioned in the note text as a list of email addresses |
| text | Text | textarea |  |
| user_id | User | select_user | The user who created the Note |

</details>
