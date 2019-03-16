
import pymysql
import re
#database connection
connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="face_recognition")
cursor = connection.cursor()

# queries for inserting values
retrive = "SELECT name FROM observations WHERE id=(SELECT max(id) FROM observations);"
#executing the quires

cursor.execute(retrive)
Featched_name = cursor.fetchall()
#commiting the connection then closing it.
connection.commit()
connection.close()

str = ','.join(map(','.join,Featched_name))
print (str)
# result = re.sub('abc(def)ghi','',Featched_name )
# print (result)
# print re.sub('[^a-zA-Z]+', r'', Featched_name)