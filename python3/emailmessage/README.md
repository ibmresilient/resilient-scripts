# Email Message

This page describes the methods and fields available for use on the object type `Email`. Each method has a simple example of how to use it.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> getBodyHtmlRaw() </summary>

  Returns the content of the email message, including the HTML markup. The returned string is a unicode string.

  Example:
  ```python
  from bs4 import BeautifulSoup

  soup = BeautifulSoup(emailmessage.getBodyHtmlRaw(), "html.parser")
  log.info(soup.prettify())
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> associateWithIncident(incident) </summary>

  Associates the email message with an incident returned by helper.findIncidents(). It does not return a value, but sets the top-level incident variable.

  Example:
  ```python
  query_builder.contains(fields.incident.name, "Existing Incident")
  query_builder.sortByAscending(fields.incident.id)
  query = query_builder.build()

  query_results = helper.findIncidents(query)

  if len(query_results) > 0:
    incident = query_results[0]
    emailmessage.associateWithIncident(incident)
  else:
    log.info('Could not find any incident to associate with')
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> createAssociatedIncident(name, owner_handle) </summary>

  Creates an incident based on the email message. It does not return a value, but sets the top-level incident variable.

  `name: string` provide a name for the incident

  `owner_handle: user or group` Specify the owner of the new incident. For an individual user, enter the user's ID or email address. For a group, enter the group's ID or name.

  Example:
  ```python
  owner = principal.id
  emailmessage.createAssociatedIncident(emailmessage.subject, owner)

  incident.description = helper.createRichText("This incident was created from an email")
  ```
  </details>
  <!-- End of method -->

<!-- End of section -->
</blockquote>

<br>

## Fields

These are the fields available on an EmailMessage Object Type.

<details>
<summary>Show all fields</summary>

| Name | Display Name | Type | Notes |
|---|:---|:---|:---|
| attachments | Attachments | nested_collection | Returns an array of attachment metadata objects, with each element containing the following properties: id, presented_filename, presented_content_type, suggested_filename, suggested_content_type, content_id, size, inline. The "presented_" prefix properties (which may have a value of None) reflect the file details as defined by the email headers. The "suggested_" prefix properties (which always have a value) reflect the file details as calculated upon inspection by the email ingester. The inline property indicates whether the attachment was found inline in the email body (True) or a separate file attachment (False). The attachment metadata objects are not visible in the script editor type ahead. |
| body | Body | textarea | Returns the content of the email body as plain text. Any HTML markup is removed. |
| cc | Cc | nested_collection | Returns an array of objects representing the recipients present in the CC or To field of the email. Each element defines a mandatory address value with an optional name value. |
| cc_address | Cc Address | collection_item_text |  |
| cc_name | Cc Name | collection_item_text |  |
| sender | From | nested_collection | Returns a single object representing the recipient in the From field of the email. This object defines a mandatory address value with an optional name value. |
| from_address | From Address | text |  |
| from_name | From Name | text |  |
| headers | Headers | nested_collection | Returns a map (dictionary) representation of the headers defined in the email. The header name acts as the map key and the corresponding value for each header key is an array that may contain none, one or multiple elements. Both the header name and the elements in the corresponding array of header values are all expressed as strings. |
| id | ID | number | Returns the ID number assigned to the email message, which is shown on the Mail Inbox page. |
| inbound_mailbox | Inbound Mailbox | select | Returns the name of the inbound email connection configured in the SOAR platform. You can view the inbound mailboxes in the Organization tab under Administrator Settings. |
| received_date | Received Date | datetimepicker | The date the email was received. |
| sent_date | Sent Date | datetimepicker | The date the email was sent. |
| subject | Subject | text | Returns the subject of the email message. |
| to | To | nested_collection |  |
| to_address | To Address | collection_item_text |  |
| to_name | To Name | collection_item_text |  |

</details>
