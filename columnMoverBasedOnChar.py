import pandas as pd
df = pd.read_excel(r'C:\Users\sairam\Downloads\rawData\rawData\MELI_86_10-Q_1.xlsx')

characterCheck = ['$', '(']
directions = dict()
for ch in characterCheck:
    dummyList = []
    for id, d in enumerate(df.columns):
        chaCount = 0
        dataCount = 0
        for k in df[d].values.tolist():

            try:
                if ch == k.strip():
                    chaCount+=1
                else:
                    dataCount+=1
            except:
                pass

        if chaCount>=1 and dataCount>=1:
            directions[id] = 'B'
        elif chaCount>=1 and dataCount==0:
            directions[id] = 'F'
        else:
            directions[id] = None



        print('===================================================')

    # for ch in characterCheck:
    # dummyList = []
    columns = df.columns.tolist()
    for colId, col in enumerate(columns):
        if directions[colId]:
            if directions[colId] == 'B':
                data = list(zip(df[columns[colId]].values.tolist(), df[columns[colId + 1]].values.tolist()))
                for dt_id, dt in enumerate(data):

                    try:
                        p1 = str(dt[0])
                        if p1 == 'nan':
                            p1 = ''
                    except:
                        p1 = ''
                    try:
                        p2 = str(dt[1])
                        if p2 == 'nan':
                            p2 = ''
                    except:
                        p2 = ''

                    p = p1+p2
                    data[dt_id] = p
                df[columns[colId]] = data
                df[columns[colId]+1] = None
            elif directions[colId] == 'F':
                data2 = list(zip(df[columns[colId]].values.tolist(), df[columns[colId + 1]].values.tolist()))
                for dt_id, dt in enumerate(data2):

                    try:
                        q1 = str(dt[0])
                        if q1=='nan':
                            q1 = ''
                    except:
                        q1 = ''
                    try:
                        q2 = str(dt[1])
                        if q2 == 'nan':
                            q2 = ''
                    except:
                        q2 = ''

                    q = q1 + q2
                    data2[dt_id] = q

                df[columns[colId+1]] = data2
                df[columns[colId]] = None





        print('===================================================')


#     df = pd.DataFrame(dummyList, columns=df.columns.tolist())
# print(directions)
# print(dummyList)
# df = pd.DataFrame(dummyList, columns=df.columns.tolist())
df.to_excel('kkrr.xlsx', index=False)
# print(df)

