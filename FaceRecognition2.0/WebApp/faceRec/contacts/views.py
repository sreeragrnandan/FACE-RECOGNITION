from django.shortcuts import render
from contacts.models import contact
from django.core.mail import send_mail
# Create your views here.


import pymysql
connection = pymysql.connect(host="localhost",port=3307, user="root", passwd="", database="face_recognition")
cursor = connection.cursor()
# queries for retrievint all rows
retriveNAME = "SELECT name FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
retriveCAM = "SELECT cam FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
#executing the quires
cursor.execute(retriveNAME)

Featched_name = cursor.fetchall()
obsName = ','.join(map(','.join,Featched_name))
camid = "c3"
retriveCAM = "SELECT cam FROM contacts_contact WHERE id=(SELECT max(id) FROM contacts_contact);"
cursor.execute(retriveCAM)
Featched_cam = cursor.fetchall()
cam = ','.join(map(','.join,Featched_cam))
#commiting the connection then closing it.



def contacts(request):
    con = contact.objects.order_by('id')
    date_dict = {'contact': con}
    send_mail(
    obsName + ' Spoted',
    'At camera ' + cam,
    'facerecogni2k18@gmail.com',
    ['sreerag.cs17@jecc.ac.in','sreeragraghunandan@gmail.com'],
    fail_silently=False
)

    return render(request, 'contacts/contacts.html', context=date_dict)
connection.commit()
connection.close()
# def index(request):
#     mydict  = {
#         'insert_me':"contect should be display here!"
#     }
#     return render(request, 'contacts/contacts.html', context=mydict)