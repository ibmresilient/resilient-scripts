# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import datetime as dt

if incident.pii.determined_date:
    determined_datetme = dt.datetime.fromtimestamp(
        incident.pii.determined_date/1000)
    day_ahead = determined_datetme + dt.timedelta(hours=24)
    task.due_date = day_ahead
