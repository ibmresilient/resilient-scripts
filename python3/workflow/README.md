# Workflow

This page describes the methods and fields available for use in scripts within a `Workflow`. This can be a standalone script or a pre/post process script.

NOTE Pre-Process scripts have limited functionality and are mainly used for setting function inputs. Any attempt to set incident fields or add workflow properties will fail silently.

## Methods
<blockquote>
<!-- Start of section -->
  <!-- Start of method -->
  <details><summary> addProperty(propertyName, propertyValue) </summary>

  Adds a key value property to a workflow. This property will persist for the duration of the workflow, so it can be accessed by any downstream functions or scripts. For example passsing the results of a function into a second function.

  `propertyName: string`

  `propertyValue: dict`

  Example:
  ```python
  props = {
    "name": "First Script",
    "count": 3,
    "results": [100, 200, 300],
    "nestedDict": {
      "key": "value"
    }
  }

  workflow.addProperty('scriptOutput', props)
  ```
  </details>
  <!-- End of method -->

<!-- End of section -->
</blockquote>

## Fields

In a workflow, the properties field is available to access previously stored workflow properties. In a Post-Process script, the results field is also available.

### - workflow.properties
Properties contains all of the previously added properties in a workflow. Access a specific property like so:

```python
# In a workflow script or pre/post process script following on from addProperty() example
prevOutput = workflow.properties.scriptOutput

incident.addNote('The previous script {} got the output {}'.format(prevOutput.name, prevOutput.results))
```

### - results
Results contains the output of a function. The format of this obeject will depend on the function being used, so refer to the function documentation if you are unsure. The results object has a success attribute so you can check if the function worked before attempting the rest of the script

```python
# In a Post-Process script
if results["success"]:
  artifact.description = helper.createRichText("The function succeeded with results {}".format(results["content"]))
else:
  artifact.description = helper.createRichText("The function did not succeed")

```