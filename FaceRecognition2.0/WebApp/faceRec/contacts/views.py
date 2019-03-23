from django.shortcuts import render
from contacts.models import contact
from django.core.mail import send_mail
# Create your views here.
import pymysql

def contacts(request):
    con = contact.objects.order_by('id')
    date_dict = {'contact': con}
    # if cam != EmailCam or obsEmail != obsName :
    return render(request, 'contacts/contacts.html', context=date_dict)
    
# def index(request):
#     mydict  = {
#         'insert_me':"contect should be display here!"
#     }
#     return render(request, 'contacts/contacts.html', context=mydict)