# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

# Set the due date of the task to 7 days from the current time.
import datetime as dt
today = dt.datetime.now()
# Get a datetime of today + 7 days
week_ahead = today + dt.timedelta(days=7)

task.due_date = week_ahead
