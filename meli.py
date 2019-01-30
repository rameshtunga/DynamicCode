from tabula import read_pdf


import pandas as pd
import tabula
# files = "filename.pdf"
# path = 'C:\\Users\\Himanshu Poddar\\Desktop\\datathon\\Himachal\\'  + file
# df = tabula.read_pdf('http://investor.mercadolibre.com/static-files/113ee1f2-a6bd-40e1-a483-6cd185c01280',spreadsheet=True, pages = '4', multiple_tables = True)
# tabula.convert_into('http://investor.mercadolibre.com/static-files/113ee1f2-a6bd-40e1-a483-6cd185c01280', "output.csv",pages = '4', multiple_tables = True, output_format="csv")
# print(df)
# df = pd.DataFrame(df, columns=None)
# df.to_csv('test.csv')

# data = read_pdf('http://investor.mercadolibre.com/static-files/113ee1f2-a6bd-40e1-a483-6cd185c01280', pages=4)
# print(data)
# data.to_csv('meli.csv')


data = """
Consolidated Net Revenues,Q3�17,Q4�17,Q1�18,Q2�18,Q3�18
"",,,,,
Brazil,35%,37%,15%,25%,25%
Argentina,30%,42%,43%,14%,(8)%
Mexico,(3)%,48%,51%,62%,152%
"",Year-over-year Growth rates,,,
Consolidated Net Revenues,Q3�17 Q4�17,Q1�18,Q2�18,Q3�18
Brazil,31% 35%,19%,40%,56%
Argentina,51% 62%,80%,68%,68%
Mexico,(7)% 41%,39%,71%,168%
"""
import re
data = re.sub('\$ +', ' $', data)
formats = '[\$\d\.]'

lines = data.splitlines()
checkLines = []
for id, line in enumerate(lines):
    # splines = line.split()
    splines = re.split('[ ,]', line)
    if len(splines)>3:

        s1 = True if re.search(formats, splines[-1]) else False
        s2 = True if re.search(formats, splines[-2]) else False
        s3 = True if re.search(formats, splines[-3]) else False
        if s1 and s2 and s3:
            checkLines.append([id, splines])


startValue = 0
endValue = 0
found = True
dummyList = []
for id, ch in enumerate(checkLines):

        n1 = ch[0]+1
        try:
            n2 = checkLines[id+1][0]
        except:
            n2 = id
        if n1 == n2:
            if found:
                startValue = id
            found = False
        else:
            endValue = id
            found = True
            dummyList.append([id, checkLines[startValue:endValue+1]])

for mainId, k in enumerate(dummyList):
    tData = k[1]
    tableId = tData[0][0]
    firstRow = tData[0][1]
    secondRows = tData[1:]
    columnCount = 0
    for id, col in enumerate(firstRow[::-1]):
        colFound = 0
        for sec in secondRows:
            try:
                sec = sec[1]
                if re.search(formats, col) and re.search(formats, sec[-(id + 1)]):
                    colFound+=1
            except:
                pass

        if (len(secondRows)-2)<colFound:
            columnCount+=1

    tableResult = []
    for m in tData:
        text = [' '.join(m[1][:-columnCount])]
        text.extend(m[1][-columnCount:])
        tableResult.append(text)
        print(text)
    df = pd.DataFrame(tableResult, columns=None)
    df.to_excel('texxxx_'+str(mainId)+'.xlsx', index=False)

