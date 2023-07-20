from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
def form(request):
    UMF=Userform()
    PMF=Profileform()
    d={'UMF':UMF,'PMF':PMF}
    if request.method=='POST' and request.FILES:
        UMFD=Userform(request.POST)
        PMFD=Profileform(request.POST,request.FILES)
        if UMFD.is_valid() and PMFD.is_valid():
            NUMFD=UMFD.save(commit=False)
            submittedpassword=UMFD.cleaned_data['password']
            NUMFD.set_password(submittedpassword)
            NUMFD.save()
            NPMFD=PMFD.save(commit=False)
            NPMFD.username=NUMFD
            NPMFD.save()
            send_mail('Registration',
                    'Ur Registration is Successfull',
                      'sivanandana2001@gmail.com',
                      [NUMFD.email],
                      fail_silently=True)
    return render(request,'form.html',context=d)