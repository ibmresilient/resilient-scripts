# Helper Methods

These helper methods can be used in any script.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> createPlainText(text) </summary>

  Creates a plain text object that can be assigned to a field or added to a note.

  `text: string`

  Example:
  ```python
  incident.name = helper.createPlainText('Some plain text')
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> createRichText(text) </summary>

  Creates a rich text object that supports html. Can be assigned to rich text fields or added to notes.

  `text: html or string`

  Example:
  ```python
  exciting_text = """
  <h1> Title </h1></br>
  <bold> Hello </bold>
  <p style="color:red">some red text</p>
  """

  incident.addNote(helper.createRichText(exciting_text))
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> fail(message) </summary>

  Stops the script execution and will alert with a message if run interactively or with a menu item rule. This function is very helpful for user validation and can be combined with rules to ensure certain fields are properly completed.

  `message: string`

  Example:
  ```python
  if incident.resolution_summary is None:
    helper.fail('Please add a resolution summary before closing')
  else:
    incident.plan_status = 'C'
  ```
  </details>
  <!-- End of method -->

  <!-- Start of method -->
  <details><summary> findIncidents(query) </summary>

  Searches for incidents that match the query and returns them. This method can be very performance intensive and should be limited if possible by including date ranges.

  `query: queryBuilder object`

  Example:
  ```python
  import datetime

  me = principal.id
  last_week = datetime.datetime.now() - datetime.timedelta(days=7)
  last_week = last_week.timestamp() * 1000

  # This query searches for incidents owned by the current user
  query_builder.contains(fields.incident.owner_id, me)
  # Created after 1 week ago
  query_builder.isGreaterThan(fields.incident.create_date, last_week)
  query_builder.sortByAscending(fields.incident.id)
  query = query_builder.build()

  results = helper.findIncidents(query)

  if len(results) > 0:
    log.info('{} incidents created in the last week were assigned to this user'.format(len(results)))
    [log.info(result.name) for result in results]

  else:
    log.info('found no incidents in the last week')
  ```
  </details>
  <!-- End of method -->

<!-- End of section -->
</blockquote>
