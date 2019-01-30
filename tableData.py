import re
import pandas as pd
def tableDataExtractor(table, WithLink = None):
    try:
        if table.find_all('tr'):
            # print('found')
            # table = table.find('table')

            trs = table.find_all('tr')
            nooftd = 0
            for tr in trs:
                tds = tr.find_all(re.compile('th|td'))
                if len(tds) > nooftd:
                    nooftd = len(tds)
            trList = []
            for tr in trs:
                tds = tr.find_all(re.compile('th|td'))
                tdList = []
                for td in tds:
                    colspan = 0
                    try:
                        colspan = int(td['colspan'])
                    except:
                        pass
                    if colspan != 0:
                        a = td.text.strip()
                        a = None if len(a)==0 else a
                        tdList.append(a)
                        for k in range(colspan - 1):
                            tdList.append(None)
                    else:
                        if WithLink:
                            link = td.find('a')['href'] if td.find('a') else None
                            tdList.append([td.text.strip(), link])
                        else:
                            b = td.text.strip()
                            b = re.sub(r'[^\x00-\x7F]', '', b)
                            b = re.sub(' +', ' ', b).strip()
                            b = None if len(b)==0 else b
                            tdList.append(b)
                trList.append(tdList)

            result = trList
            col = []
            for id, k in enumerate(result[0]):
                a = 'Col_' + str(id)
                col.append(a)
            df = pd.DataFrame(result, columns=col)
            df = df[df['Col_0'] != None]
            df = df[df['Col_0'] != None]
            df = df.dropna(axis=1, how='all', inplace=False)
            df = df.dropna(axis=0, how='all', inplace=False)

            # Filter Extra Columns Data And Remove Empty Columns
            data = df.values.tolist()
            # checkFound = False
            # for id, k in enumerate(data[0]):
            #     if k is None and not isinstance(data[1][id], str):
            #         checkFound = True
            # if checkFound:
            #     return data
            check = data[0]
            result = []
            result.append(check)
            for d in data[1:]:
                # print(d)
                dummyList = []
                for id, value in enumerate(d):

                    if check[id] is not None:

                        if value is None:
                            try:
                                if check[id + 1] is None:
                                    # print(d[id+1])
                                    d[id] = d[id + 1]
                                    d[id + 1] = None
                                    dummyList.append(d)
                            except:
                                pass
                                # dummyList.append(d)
                result.append(d)

            df = pd.DataFrame(result, columns=df.columns.tolist())
            df = df.dropna(axis=1, how='all', inplace=False)
            df = df.dropna(axis=0, how='all', inplace=False)
            finalResult = df.values.tolist()
            return finalResult

            # return trList
    except:
        return None