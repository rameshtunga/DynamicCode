import pandas as pd
from pandas_datareader import data, wb

import os

Location = os.getcwd()+'\\output\\23-08-2018'
EX = pd.ExcelFile(Location+'\\carRentalData.xlsx')
df = pd.read_excel(EX, 'Consolidated-Mario')

# # df = df.pivot_table('Rate Per Day', index=['Days','Company'], aggfunc='mean')
# df = df.pivot_table('Rate Per Day', index=['Days','Company'], aggfunc='mean').unstack()
# # df = pd.DataFrame(df.to_records())

df = df.pivot_table('Rate Per Day', index=['Days','Company'], aggfunc='mean')
df = pd.DataFrame(df.to_records())
df = df.reset_index().groupby(['Company', 'Days'])['Rate Per Day'].aggregate('first').unstack()
excel_file = 'jjjj.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook  = writer.book
worksheet = writer.sheets[sheet_name]

chart = workbook.add_chart({'type': 'column'})
colors = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00']

# Configure the series of the chart from the dataframe data.
for col_num in range(1, 3):
    chart.add_series({
        'name':       ['Sheet1', 0, col_num],
        'categories': ['Sheet1', 1, 0, 8, 0],
        'values':     ['Sheet1', 1, col_num, 8, col_num],
        'fill':       {'color':  colors[col_num - 1]},
        'overlap':    -10,
    })

# Configure the chart axes.
chart.set_x_axis({'name': 'Companies'})
chart.set_y_axis({'name': 'Farms', 'major_gridlines': {'visible': False}})

# Insert the chart into the worksheet.
worksheet.insert_chart('H2', chart)


# Close the Pandas Excel writer and output the Excel file.
writer.save()