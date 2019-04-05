
import pymysql
#database connection
connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="face_recognition")
cursor = connection.cursor()

retriveNAME = "SELECT name FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
retriveCAM = "SELECT cam FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
#executing the quires
cursor.execute(retriveNAME)

Featched_name = cursor.fetchall()
obsName = ','.join(map(','.join,Featched_name))
cursor.execute(retriveCAM)
Featched_cam = cursor.fetchall()
cam = ','.join(map(','.join,Featched_cam))
#commiting the connection then closing it.

# # queries for retrievint email datasheet
# retriveMAIL = "SELECT Name FROM contacts_contact WHERE id=(SELECT max(id) FROM email);"

# CamName = "SELECT cam FROM email WHERE id=(SELECT max(id) FROM email);"
# #executing the quires
# cursor.execute(retriveMAIL)
# Featched_email = cursor.fetchall()
# obsEmail = ','.join(map(','.join,Featched_email))

# cursor.execute(CamName)
# Featched_ECam = cursor.fetchall()
# EmailCam = ','.join(map(','.join,Featched_ECam))


#commiting the connection then closing it.
connection.commit()
connection.close()
name ="sreerag"
camid = "c1"
# print(Featched_cam)
# cam = ','.join(map(','.join,Featched_cam))
# print(EmailCam)

# obsName = ','.join(map(','.join,Featched_name))
# print (obsEmail)
print (cam)
# if name !="Unknown" and (name != obsName or camid != cam):
print (obsName)
# result = re.sub('abc(def)ghi','',Featched_name )
# print (result)
# print re.sub('[^a-zA-Z]+', r'', Featched_name)