from selenium import webdriver
import time
from bs4 import BeautifulSoup

Result = []
driver = webdriver.Ie(executable_path=r'C:\Users\doddsai.BU1-D2208N62\Downloads\IEDriverServer_x64_2.39.0\IEDriverServer.exe')
for k in range(33):
    driver.get('https://www.internationalusedtrucks.com/inventory/?/listings/trucks/for-sale/list/category/27/trucks?dgn=internationalutc&dlr=1&sfc=0&ssc=0&snai=0&manu=International&page='+str(k+1))
    time.sleep(20)
    # ss = driver.execute_script ('return window.Highcharts.charts[0].series[0].options.data')
    # print(driver.page_source)

    data = driver.page_source

    jsoup = BeautifulSoup(data)
    Div = jsoup.find('div', attrs={'class':'listings-list'})

    for div in Div.find_all('div', attrs={'id':'ListListing_'}):
        dummyDict = dict()
        print(div)
        name = div.find('div', attrs={'class':'listing-name'})
        if name:
            name = name.text
        dummyDict['Name'] = name

        description = div.find('div', attrs={'class':'employee-category bold m-bottom-6'})
        if description:
            description = description.parent.text
        dummyDict['description'] = description

        StockNumber = div.find('span', text='Stock Number:')
        if StockNumber:
            StockNumber = StockNumber.parent.text.split(':')[1]
        dummyDict['StockNumber'] = StockNumber

        Mileage = div.find('span', text='Mileage:')
        if Mileage:
            Mileage = Mileage.parent.text.split(':')[1]
        dummyDict['Mileage'] = Mileage

        EngineManufacturer = div.find('span', text='Engine Manufacturer:')
        if EngineManufacturer:
            EngineManufacturer = EngineManufacturer.parent.text.split(':')[1]
        dummyDict['EngineManufacturer'] = EngineManufacturer
        Horsepower = div.find('span', text='Horsepower:')
        if Horsepower:
            Horsepower = Horsepower.parent.text.split(':')[1]
        dummyDict['Horsepower'] = Horsepower

        price = div.find('span', attrs={'class':'listing-price-label bold'})
        if price:
            price = price.parent.text.split(':')[1]
        dummyDict['price'] = price

        dealer = div.find('div', attrs={'class':'col dealer-info cf'})
        if dealer:
            dealer = dealer.text
        dummyDict['dealer'] = dealer

        Updated = div.find('span', text='Updated:')
        if Updated:
            Updated = Updated.parent.text.split(':')[1]
        dummyDict['Updated'] = Updated
        Result.append(dummyDict)

import pandas as pd
df = pd.DataFrame(Result)
df.to_excel('truckData.xlsx', index=False)
print(Div)
