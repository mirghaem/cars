import requests
import mysql.connector
from bs4 import BeautifulSoup

my_sql = mysql.connector.connect(user='root', password='13141516',
                                host= '127.0.0.1',
                                database= 'firstghaem')
cursor = my_sql.cursor()
query= ('CREATE TABLE ml ( name VARCHAR(50),mileage VARCHAR(15),year VARCHAR(6),prise VARCHAR(15))')
cursor.execute(query)
my_sql.commit()

for i in range(1,20):
    url = requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page={}'.format(i))

    ss = BeautifulSoup(url.text,'html.parser')
    cars = ss.findAll('div',attrs={'class':"card-content vehicle-card-body order-3"})
    for ii in cars:
        name = ii.find('span',attrs={'class':"vehicle-header-make-model text-truncate"}).text

        mileage = ii.find('div', attrs={'data-test':"vehicleMileage"}).text
        mileage = mileage.replace('miles','')
        mileage = mileage.replace(',','')

        year = ii.find('span',attrs={'class':"vehicle-card-year font-size-1"}).text
        prise = ii.find('div', attrs={'data-test':"vehicleCardPricingBlockPrice"}).text
        prise = prise.replace('$','')
        new_query = ('INSERT INTO ml VALUE("{}","{}","{}","{}")'.format(name,mileage,year,prise))
        cursor.execute(new_query)
        my_sql.commit()
        # print (prise)

# for i in car:
#     print (i.text)












cursor.close()
my_sql.close()

