import pandas as pd
from pandas_datareader import data, wb

import os

Location = os.getcwd()+'\\output\\23-08-2018'
EX = pd.ExcelFile(Location+'\\carRentalData.xlsx')
df = pd.read_excel(EX, 'Consolidated-Mario')

# # df = df.pivot_table('Rate Per Day', index=['Days','Company'], aggfunc='mean')
# df = df.pivot_table('Rate Per Day', index=['Days','Company'], aggfunc='mean').unstack()
# # df = pd.DataFrame(df.to_records())

df = df.pivot_table('Rate Per Day', index=['Days','Company'], aggfunc='mean').unstack()
# df = pd.DataFrame(df.to_records())
# df = df.reset_index().groupby(['Company', 'Days'])['Rate Per Day'].aggregate('first').unstack()
excel_file = 'uuuuu.xlsx'
sheet_name = 'Sheet1'

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
df.to_excel(writer, sheet_name=sheet_name)

# Access the XlsxWriter workbook and worksheet objects from the dataframe.
workbook  = writer.book
worksheet = writer.sheets[sheet_name]

chart = workbook.add_chart({'type': 'column'})
colors = ['#E41A1C', '#377EB8', '#4DAF4A', '#984EA3', '#FF7F00']

# Configure the series of the chart from the dataframe data.
i = 0
for col_num in range(1, 3):
    chart.add_series({
        'name':       ['Sheet1', 2+col_num, 0],
        'categories': ['Sheet1', 1,1,1,8],
        'values':     ['Sheet1', col_num+2, 1, col_num+2, 8],
        'fill':       {'color':  colors[i]},
        'overlap':    -10,
    })
    i+=1

# Configure the chart axes.
chart.set_x_axis({'name': 'Companies'})
chart.set_y_axis({'name': 'Farms', 'major_gridlines': {'visible': False}})

# Insert the chart into the worksheet.
worksheet.insert_chart('K2', chart)


# Close the Pandas Excel writer and output the Excel file.
writer.save()