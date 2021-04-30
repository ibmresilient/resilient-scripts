# Incident

This page describes the methods and fields available for use on the object type `incident`. Each method has a simple example of how to use it.

<details><summary> Methods </summary>
  <blockquote>
<!-- Start of secion -->
  <!-- Start of method -->
  <details><summary> addArtifact(type, value, description) </summary>

  Adds an artifact to the incident with the given type, value, and description. Returns an Artifact script object for further customization. Artifact types can be found in Customization Settings -> Artifact Types tab. Use the API Name.

  `type: string`

  `value: string`

  `description: string or TextObject`

  Example:
  ```python
  new_artifact = incident.addArtifact('DNS Name', 'www.github.com', 'github dns')
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> addEmailAttachment(id, filename, content_type) </summary>

  Attaches the email attachment to the incident and returns the attachment object to the incident. The returned attachment object can then be acted upon by other script operations. Can only be used in the context of an Email Message script.

  `id: int`

  `filename: string` (optional)

  `content_type: string` (optional)

  Example:
  ```python
  for attachment in emailmessage.attachments:
    incident.addEmailAttachment(attachment.id, attachment.presented_filename, attachment,presented_content_type)
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> addMilestone(title, description, date) </summary>

  Adds a milestone to the incident with the given title, description, and date. Returns a Milestone script object for further customization.

  `title: string`

  `description: string`

  `date: int` (millisecond timestamp)

  Example:
  ```python
  timestamp_millis = 1619785871000
  incident.addMilestone('Milestone title', 'example milestone', timestamp_millis)
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> addNote(text) </summary>

  Adds a note to the incident with the given text. Returns a Note script object for further customization.

  `text: string or TextObject`

  Example:
  ```python
  incident.addNote(helper.createRichText('<h1>HEY!<br>YOU</h1>'))
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> addRow(table_name) </summary>

  Adds a row to the named data table on the incident. Returns a Row script object for further customization.

  `table_name: string `

  Example:
  ```python
  new_row = incident.addRow('my_table')
  new_row['column_A'] = 'New value'
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> addTask(name, phase_id, instr_text) </summary>

  Adds an adhoc task to the incident with the given name, phase, and instructions. Returns a Task script object for further customization. phase_id sgould match the name of a phase from Customization Settings -> Phases & Tasks

  `name: string`

  `phase_id: string`

  `instr_text: str or TextObject`

  Example:
  ```python
  incident.addTask('New Task', 'Respond', 'do this please')
  ```
  </details>
  <!-- End of method -->

<!-- End of section -->
  </blockquote>
</details>



<details><summary> Fields </summary>

These are the built in fields of an incident taken from the types rest API. `name` is the programatic name used to access a field within a script. Not all fields are writable. 

Custom fields can be accesed using the `properties` attribute. For example, `incident.properties.mycustomfield`


| Name | Display Name | Type | Notes |
|---|:---|:---|:---|
| addr | Address | text | Physical location of the incident, if applicable |
| city | City | text |  |
| confirmed | Incident Disposition | boolean | Tag an issue as an unconfirmed (event) vs. a confirmed incident. |
| country | Country/Region | select |  |
| create_date | Date Created | datetimepicker | The date the incident was created. This field is read-only. |
| creator_id | Created By | select_owner |  |
| crimestatus_id | Criminal Activity | select |  |
| description | Description | textarea | A free form text description of the incident. |
| discovered_date | Date Discovered | datetimepicker | Date the incident was discovered/reported. |
| due_date | Next Due Date | datetimepicker | The nearest date for the next task due. This field is read-only. |
| employee_involved | Employee Involved | boolean |  |
| end_date | Date Closed | datetimepicker | The date the incident was closed. This field is read-only. |
| exposure_dept_id | Department | select |  |
| exposure_individual_name | Individual Name | text |  |
| exposure_type_id | Exposure Type | select | Origin source of the exposure |
| exposure_vendor_id | Vendor | select |  |
| gdpr.gdpr_breach_circumstances | GDPR Breach Circumstances | multiselect |  |
| gdpr.gdpr_breach_type | GDPR Breach Type | select |  |
| gdpr.gdpr_breach_type_comment | GDPR Breach Type Comment | textarea |  |
| gdpr.gdpr_consequences | GDPR Consequences | select |  |
| gdpr.gdpr_consequences_comment | GDPR Consequences Comment | textarea |  |
| gdpr.gdpr_final_assessment | GDPR Final Assessment | select |  |
| gdpr.gdpr_final_assessment_comment | GDPR Final Assessment Comment | textarea |  |
| gdpr.gdpr_identification | GDPR Identification | select |  |
| gdpr.gdpr_identification_comment | GDPR Identification Comment | textarea |  |
| gdpr.gdpr_personal_data | GDPR Personal Data | select |  |
| gdpr.gdpr_personal_data_comment | GDPR Personal Data Comment | textarea |  |
| gdpr.gdpr_subsequent_notification | GDPR Subsequent Notification | boolean |  |
| hard_liability | Assessed Liability | number |  |
| id | ID | number |  |
| inc_last_modified_date | Last Modified | datetimepicker | The date the incident was last modified.This field is read only. |
| inc_training | Simulation | boolean | Whether the incident is a simulation or a regular incident. This field is read-only. |
| incident_type_ids | Incident Type | multiselect | The type of incident |
| jurisdiction_name | Jurisdiction | text |  |
| members | Members | multiselect_members |  |
| name | Name | text | A unique name to identify this particular incident. |
| negative_pr_likely | Negative PR | boolean | If it is foreseeable that the incident might generate any negative public image or publicity for your company or organization. |
| nist_attack_vectors | NIST Attack Vectors | multiselect | NIST Attack Vectors the incident falls under, if applicable. |
| org_handle | Organization | select |  |
| owner_id | Owner | select_owner |  |
| phase_id | Phase | select | The phase of the incident. |
| pii.alberta_health_risk_assessment | Alberta Health Risk Assessment | boolean |  |
| pii.data_compromised | Was personal information or personal data involved? | boolean | Determine whether personal information/data was foreseeably involved, disclosed, compromised, accessed, altered, destroyed, damaged, lost or inaccessible. |
| pii.data_contained | Exposure Resolved | boolean | Whether the exposure has been addressed and rectified. |
| pii.data_encrypted | Data Encrypted | boolean | Whether the data in question was encrypted. Data should not be considered encrypted if the encryption keys were also breached. |
| pii.data_format | Data Format | select | Specify the format of the personal information involved. |
| pii.data_source_ids | Source of Data | multiselect | Original source of the data, such as the name of the database. |
| pii.dc_impact_likely | Impact Likely for District of Columbia | boolean |  |
| pii.determined_date | Date Determined | datetimepicker | Date you determined whether or not the incident involved a breach of personal information or personal data. Regulatory task timelines will be derived from this date and time. |
| pii.gdpr_harm_risk | Risk of Harm | select | Likelihood and severity of the risk to the rights and freedoms of the data subject, as defined by the GDPR. |
| pii.gdpr_lawful_data_processing_categories | Lawful Data Processing Categories | multiselect | Under the GDPR, processing of personal or sensitive data is only lawful if one or more of these categories applies. |
| pii.harmstatus_id | Is harm/risk/misuse foreseeable? | select | Different jurisdictions use harm, risk, misuse, ID theft, and other standards as safe harbors from notification. Interpretation of these terms has frequently been the subject of litigation. |
| pii.impact_likely | Impact Likely | boolean |  |
| pii.new_zealand_risk_assessment | New Zealand Risk Assessment | boolean |  |
| pii.ny_impact_likely | Impact Likely for New York | boolean |  |
| pii.or_impact_likely | Impact Likely for Oregon | boolean |  |
| pii.singapore_risk_assessment | Singapore Risk Assessment | boolean |  |
| pii.wa_impact_likely | Impact Likely for Washington | boolean |  |
| plan_status | Status | select |  |
| regulator_risk.pipeda_other_factors | PIPEDA Other Factors | select |  |
| regulator_risk.pipeda_other_factors_comment | PIPEDA Other Factors Comment | textarea |  |
| regulator_risk.pipeda_overall_assessment | PIPEDA Overall Assessment | select |  |
| regulator_risk.pipeda_overall_assessment_comment | PIPEDA Overall Assessment Comment | textarea |  |
| regulator_risk.pipeda_probability_of_misuse | PIPEDA Probability of Misuse | select |  |
| regulator_risk.pipeda_probability_of_misuse_comment | PIPEDA Probability of Misuse Comment | textarea |  |
| regulator_risk.pipeda_sensitivity_of_pi | PIPEDA Sensitivity of PI | select |  |
| regulator_risk.pipeda_sensitivity_of_pi_comment | PIPEDA Sensitivity of PI Comment | textarea |  |
| reporter | Reporting Individual | text | Name of person who reported the event, such as a device owner or his/her manager |
| resolution_id | Resolution | select | Select an option that accurately describes the reason for closing this incident. |
| resolution_summary | Resolution Summary | textarea | Enter a summary that describes how this incident was resolved. |
| sequence_code | Sequence Code | text | The Unique Incident Sequence Code. |
| severity_code | Severity | select | Your impression of the events relative severity vs. other events that may be entered into the system. |
| start_date | Date Occurred | datetimepicker | Date the incident occurred |
| state | State | select |  |
| workspace | Workspace | select |  |
| zip | Zip | text |  |

</details>
