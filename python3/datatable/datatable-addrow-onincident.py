# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

""" A script which is used to add a row to a datatable and then fill
    that datatable with values for each column.

    Available with all object types.
    """

row = incident.addRow('<your_datatable_name>')
row['column1'] = 1
row['column2'] = "String field"
