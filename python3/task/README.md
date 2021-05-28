# Task

This page describes the methods and fields available for use on the object type `Task`. Each method has a simple example of how to use it.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> addNote() </summary>

  Adds a note to the task.

  Example:
  ```python
  import datetime

  seven_days_from_now = datetime.datetime.now() + datetime.timedelta(days=7)

  task.due_date = seven_days_from_now
  task.addNote("Extended due date of task by 7 days")
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> getParentObject() </summary>

  Returns the incident object that this task belongs to. The incident object can then be modified.

  Example:
  ```python
  task.status = 'C'
  incident = task.getParentObject()
  incident.addNote("The task: {} has been closed.".format(task.name))
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
| active | Active | boolean |  |
| at_id | Automatic Task ID | number |  |
| attachments_count | Attachment count | number |  |
| cat_name | Category name | text |  |
| category_id | Category | select | The category of the task. |
| closed_date | Date Closed | datetimepicker |  |
| custom | Custom Task | boolean |  |
| description | Description | textarea |  |
| due_date | Due Date | datetimepicker |  |
| id | ID | number |  |
| inc_name | Incident name | text |  |
| init_date | Date Task Initiated | datetimepicker | Most recent date the task was added to an incident. |
| instr_text | Instructions (Deprecated) | textarea |  |
| instructions | Instructions | textarea |  |
| members | Members | multiselect_members |  |
| name | Name | text |  |
| notes_count | Notes count | number |  |
| owner_id | Owner | select_owner |  |
| phase_id | Phase | select | The phase of the task. |
| private | Private | boolean | Whether or not the task is private. |
| required | Required | boolean |  |
| status | Status | select |  |


</details>
