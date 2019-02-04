import pandas as pd


def makeNone(x):
    if isinstance(x, str):
        if len(x.strip()) < 2:
            return None
        else:
            return x
    else:
        return x

def makeNan(x):
    print('============================')
    print(x)
    if isinstance(x, str):
        if len(x.strip()) < 2:
            return None
        else:
            return x
    elif x is 0 or isinstance(x, float):
        try:
            x = float(x)
            if x==0:
                return None
            else:
                return x
        except:
            return None

        return None
    else:
        return x

def columnAdjuster(fileName=None, checkRow=1, headerJoinCharacter='@'):
    if not fileName:
        return None
    df = pd.read_excel(fileName)
    print(df.columns.tolist())
    for k in df.columns.tolist():
        df[k] = df[k].apply(makeNone)

    df = df.dropna(axis=1, how='all', inplace=False)
    df = df.fillna(0)
    data = df.values.tolist()
    check = data[checkRow]
    result = []
    result.append(data[0])
    result.append(check)
    print(check)
    for d in data[checkRow+1:]:
        print(d)

        dummyList = []
        for id, value in enumerate(d):

            if check[id] is not None:

                if value is 0:
                    try:
                        if check[id + 1] is 0:
                            # print(d[id+1])
                            d[id] = d[id + 1]
                            d[id + 1] = None
                            dummyList.append(d)
                    except:
                        pass
                        # dummyList.append(d)
        result.append(d)


    df = pd.DataFrame(result, columns=None)

    for k in df.columns.tolist():
        df[k] = df[k].apply(makeNan)
    df = df.dropna(axis=1, how='all', inplace=False)
    df = df.ffill(limit=1, axis=1)
    v = df.values.tolist()
    v1 = v[0]
    v2 = v[1]
    v4 = []
    for id, kk in enumerate(zip(v1,v2)):
        k1 = kk[0]
        k2 = kk[1]
        k1 = k1+headerJoinCharacter if isinstance(k1, str) else ''
        k2 = k2 if isinstance(k2, str) else str(id)
        k = k1 + k2
        v4.append(k if len(k.strip())>=1 else str(id))

    v = v[checkRow+1:]
    v.insert(0, v4)
    colms = v[0]
    colms[0] = 'Name_'
    df = pd.DataFrame(v[1:], columns=colms)
    return df.to_dict('records')

data = columnAdjuster('text.xlsx')
print(data)
