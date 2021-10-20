from django.core.validators import ip_address_validators
from django.shortcuts import render,redirect
import re   
from django.http import HttpResponse

from .forms import RegisterationForm




def home(request):

    if request.method =='POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data['email']
            name=form.cleaned_data['name']
            # print(email,name)
            print(form.data["number"])
        else:
            form=RegisterationForm()
    
    form = RegisterationForm(request.POST)

    return render(request, 'task/home.html',{'forms':form})
        


# def home(request):
    

#     # return HttpResponse("Thank you")
#     return render(request,'task/home.html',{})

# def result(request):
#     context={}
#     value=request.POST['value']
#     choice=request.POST['select-btn']
#     if choice==1:
#         Date_finder(value)
#     elif choice==2:
#         emailvalidation(value)
#     elif choice==3:
#         NumGreaterThan100(value)
#     elif choice==4:
#         SingleQuote(value)
#     elif choice==5:
#         ip_address_validators(value)
#     elif choice==6:
#         MacValidate(value)
#     else:
#         CamelToSnake(value)

#     return HttpResponse("Thank you")










    



   

