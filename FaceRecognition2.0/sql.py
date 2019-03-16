
import pymysql
#database connection
connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="face_recognition")
cursor = connection.cursor()

# queries for inserting values
retrive = "SELECT name FROM observations WHERE id=(SELECT max(id) FROM observations);"
#executing the quires

cursor.execute(retrive)
Featched_name = cursor.fetchall()

retriveCAM = "SELECT cam FROM observations WHERE id=(SELECT max(id) FROM observations);"
cursor.execute(retriveCAM)
Featched_cam = cursor.fetchall()
#commiting the connection then closing it.
connection.commit()
connection.close()
name ="sreerag"
camid = "c1"
print(Featched_cam)
cam = ','.join(map(','.join,Featched_cam))
print (cam)
obsName = ','.join(map(','.join,Featched_name))
print (obsName)
if name !="Unknown" and (name != obsName or camid != cam):
    print (obsName)
# result = re.sub('abc(def)ghi','',Featched_name )
# print (result)
# print re.sub('[^a-zA-Z]+', r'', Featched_name)