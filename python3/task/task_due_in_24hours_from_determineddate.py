# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import datetime as dt

if incident.pii.determined_date:
    # incident.pii.determined date is a timestamp expressed in milliseconds, the datetime modules expects timestamps
    # to be expressed in seconds, therefore it needs to be divided by 1000
    determined_datetme = dt.datetime.fromtimestamp(
        incident.pii.determined_date/1000)
    day_ahead = determined_datetme + dt.timedelta(hours=24)
    task.due_date = day_ahead
