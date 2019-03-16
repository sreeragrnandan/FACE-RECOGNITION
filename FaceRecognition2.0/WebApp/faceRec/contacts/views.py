# Create your views here.
from django.shortcuts import render
from contacts.models import contact
def contacts(request):
    con = contact.objects.order_by('id')
    date_dict = {'contact': con}
    return render(request, 'contacts/contacts.html', context=date_dict)

# def index(request):
#     mydict  = {
#         'insert_me':"contect should be display here!"
#     }
#     return render(request, 'contacts/contacts.html', context=mydict)