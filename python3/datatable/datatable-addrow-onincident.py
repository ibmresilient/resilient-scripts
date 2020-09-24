""" A script which is used to add a row to a datatable and then fill
    that datatable with values for each column.

    Available at all object types. 
    """

row = incident.addRow('<your_datatable_name>')
row['column1'] = 1
row['column2'] = "String field"
