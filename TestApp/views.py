from django.shortcuts import render
from . import forms


# Create your views here.

def Studentregisteration_view(request):
    # create object Here
    form = forms.StudentForm()
    my_dict = {'form':form}
    return render(request,'Testapp/Register.html',context=my_dict)
