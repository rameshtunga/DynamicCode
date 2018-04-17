
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
page = requests.get('https://aws.amazon.com/marketplace/search/results?page=1&filters=regions&regions=us-east-1&searchTerms=')

# tree = html.fromstring(str(BeautifulSoup(page.content)))
#
# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')

# print(buyers)

def getProductDetails(pathList,htmlList):
    from lxml import html
    Excel_Table = []
    Excel_dict = []
    for li in htmlList:
        tree = html.fromstring(str(li))
        productList = []
        productDict = dict()
        for path in pathList.keys():
            a = tree.xpath(pathList[path])
            if len(a)!=0:
                productDict[path] = a[0]
                productList.append(a[0])
            else:
                productDict[path] = None
                productList.append(None)

        Excel_Table.append(productList)
        Excel_dict.append(productDict)
    return Excel_Table,Excel_dict



pathList = {'Name':"div[2]/div/h1/a/text()",
            'Description':'div[2]/p[2]/text()',
            'Rating':'div[2]/ul/li[1]/a/text()'
            }

lis = BeautifulSoup(page.content, 'html.parser').find_all('article', attrs={'class':'row products'})
ExcelTable = getProductDetails(pathList,lis)
print(ExcelTable[1])
print(tabulate(ExcelTable[0]))


#=======================================single Line=============================================================
pathList = {'Name':'//*[@id="Adding_Deleting_and_Moving_Lines.xml"]/text()',
            'Apr':'//*[@id="delete"]/text()'
            }
productDict = dict()
for key in pathList:
    a = tree.xpath(pathList[key])
    if len(a)!=0:
        productDict[key] = a[0]
    else:
        productDict[key] = None
print(productDict)

