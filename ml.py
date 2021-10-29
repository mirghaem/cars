from sklearn import tree
from sklearn import preprocessing
import mysql.connector

x = []
y = []
name_list = []
mile_list = []
year_list = []
prise_list = []


my_sql= mysql.connector.connect(user='root',
                                password = '13141516',
                                host='127.0.0.1',
                                database='firstghaem')
cursor = my_sql.cursor()
query = ('SELECT * FROM ml')
cursor.execute(query)
for name,mile,year, prise in cursor:
    name_list.append(name)
    mile_list.append(mile)
    year_list.append(year)
    prise_list.append(prise)



le = preprocessing.LabelEncoder()
clf = tree.DecisionTreeClassifier()
le.fit(name_list)


x_data = list(zip(le.transform(name_list),mile_list,year_list))
clf = clf.fit(x_data,prise_list)

new_data = [[le.transform(['Ford F-150']), 20000, 2015]]
answer = clf.predict(new_data)
print (answer)






cursor.close()
my_sql.close()



