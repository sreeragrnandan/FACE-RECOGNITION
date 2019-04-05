
import pymysql
#database connection
connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="face_recognition")
cursor = connection.cursor()
print("connection object")
print(connection)
print("cursor object")
print(cursor)
retriveNAME = "SELECT name FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
retriveCAM = "SELECT cam FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
#executing the quires
print("execute object")
print (cursor.execute(retriveNAME))

Featched_name = cursor.fetchall()
print("Featched_name")
print (Featched_name)
obsName = ','.join(map(','.join,Featched_name))
cursor.execute(retriveCAM)
print("Featched_cam")
Featched_cam = cursor.fetchall()
print(Featched_cam)
cam = ','.join(map(','.join,Featched_cam))


#commiting the connection then closing it.
connection.commit()
connection.close()

print("final result")


print (cam)
print (obsName)
