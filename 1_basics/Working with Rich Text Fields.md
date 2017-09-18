# Working with Rich Text Fields

A rich-text field in Resilient, such as the incident description, has two parts: its *format* and *content*.  The format can be either 'text' or 'html'.  The content then is plain text, or HTML-formatted rich text.

Here are some example scripts that show reading and editing the rich-text content of the incident description.

### Reading the description
If the format is 'text', the content will be plain-text.  If the format is 'html', the content will be HTML, including formatting tags, and character entities such as '&quot;' for quotation-marks.

Caution - the description might be empty (`None`), in which case you can't access its `format` and `content`!
```python
s = incident.description
if s is None:
  log.info("No description.")
elif s.format == "text":
  log.info("Description is text: {}".format(s.content))
else:
  log.info("Description is HTML: {}".format(s.content))
```

### Setting plain-text value
Use the `createPlainText` helper function to create a plain-text value for a rich-text field:
```python
f = helper.createPlainText("This is a plaintext description, with no formatting.")
incident.description = f
```

### Setting HTML rich-text value
Use the `createRichText` helper function to create an HTML value for a rich-text field.  Not all HTML tags are supported; for example, tables and scripts will be stripped.
```python
f = helper.createRichText("This is a &quot;rich text&quot; description, with <i>HTML</i> formatting.")
incident.description = f
```
