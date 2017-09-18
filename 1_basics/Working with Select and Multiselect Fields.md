# Working with Select and Multiselect Fields

## Select Fields
A 'Select' field has a list of valid values.  The field can only take one of these values (or perhaps it can be blank).
For example, if the field's API name is "operating_system", then value can be set in a script:
```
incident.properties.operating_system = "Android"
```
This will fail if 'Android' is not in the list of choices for the 'operating_system' field.

If the field is optional, you can also clear its value:
```
incident.properties.operating_system = None
```

## Multi-Select Fields

A 'Multi-select' field has a list of valid choices, but the field can have more than one of those values.  This is an "unordered set": each value cannot occur more than once, and the order of the values is not important.

### Setting the value
To set a value in the field directly, you can just assign the field literally, as a tuple, set or a list.  This will overwrite any previous values!
```python
incident.nist_attack_vectors = ["Web", "E-mail"]
```

### Clearing the value
To clear the value of a multi-select field, set it to None, or equivalently to an empty list:
```python
incident.nist_attack_vectors = None
# or
incident.nist_attack_vectors = []
```

### Adding a new value to a multi-select field
There are several ways to do this.  One good way is to use an intermediate variable, because Python 'set' and 'list' operations don't always return the value you might be expecting.  To add a new value,
```python
values = list(incident.nist_attack_vectors)
values.append("Web")
incident.nist_attack_vectors = values
```
If you want something much more concise:  note the square brackets around the list of new values:
```python
incident.nist_attack_vectors = list(incident.nist_attack_vectors) + ["Web", "E-mail"]
```

### Removing a value from a multi-select field
The verbose way to remove a value will raise an exception if the value is not in the list:
```python
values = list(incident.nist_attack_vectors)
values.remove("Web")
incident.nist_attack_vectors = values
```

Using `set` is convenient here:  note the curly brackets around the values:
```python
incident.nist_attack_vectors = set(incident.nist_attack_vectors) - {"Web", "E-mail"}
```
