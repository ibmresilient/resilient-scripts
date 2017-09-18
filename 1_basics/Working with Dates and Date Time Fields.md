# Working with Dates and Date Time Fields

Internally, Resilient stores date/time values as an integer value: milliseconds of epoch (January 1st 1970), UTC.

To use these within the in-product scripting context, they should be converted to a Java Date format.

### Reading a date value

```python
from java.util import Date

# Built-in date/time fields include: create_date, discovered_date, start_date, end_date
dt_raw = incident.discovered_date
log.info("Discovered date (raw value: epoch milliseconds): {}".format(dt_raw))

# Use the Java Date object to work with date and time values
dt_date = Date(incident.discovered_date)
log.info("Discovered date (millis): {}".format(dt_date))

year = dt_date.getYear() + 1900
log.info("Year: {}".format(year))

month = dt_date.getMonth()
log.info("Month: {}".format(month))

weekday = dt_date.getDay()
log.info("Day of week: {}".format(weekday))

day = dt_date.getDate()
log.info("Day of month: {}".format(day))

millis = dt_date.getTime()
log.info("Milliseconds timestamp: {}".format(millis))
```

### Calculating and saving date and time values

Simple time adjustments can be calculated by adding and subtracting from the 'milliseconds' value.

```python
from java.util import Date

# Get the current time
dt_now = Date()
log.info("Now: {}".format(dt_now))

# Calculate a time in the future
ONE_HOUR = 1000 * 60 * 60
ONE_DAY = ONE_HOUR * 24

dt_tomorrow = Date(dt_now.getTime() + ONE_DAY)
log.info("Now: {}".format(dt_tomorrow))

# Set the incident discovered-date
incident.discovered_date = dt_now

# Set the value of a custom date-time field
incident.properties.next_review = dt_tomorrow
```
