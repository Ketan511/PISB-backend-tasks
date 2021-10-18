from django.core.validators import ip_address_validators
from django.shortcuts import render,redirect
import re   
from django.http import HttpResponse

from .forms import RegisterationForm

def emailvalidation(email):
    def check(email):  
        return re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)

    var1=check(email)
    if var1:
        print(email)
        
    else:
        print("Email is invalid")

def Date_finder(date):
    def check(date):
        return re.match(r'(\d{3}[1-9]|\d{2}[1-9]\d|\d[1-9]\d{2}|[1-9]\d{3})[-](0[1-9]|1[0-2])[-]([0-2][1-9]|2[0-9]|3[0-1])',date)

    
    var2=check(date)
    if var2:
        print(date)
    else:
        print("Date is incorrect")

def NumGreaterThan100(num):
    pattern=re.compile(r'[1-9][0-9][0-9]+')
    matches=pattern.findall(num)

    if matches:
        for match in matches:
            print(match)
    else:
        print("Not found")
def SingleQuote(string):
    pattern=re.compile(r"(?<=')[^']+(?=')")
    matches=pattern.findall(string)
    if matches:
        for match in matches:
            print(match)
    else:
        print("Not found")

def IpValidation(ip_address):
    ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

    ipv6 = '''(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|
        ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:)
        {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1
        ,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}
        :){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{
        1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA
        -F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a
        -fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0
        -9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,
        4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}
        :){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9
        ])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0
        -9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]
        |1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]
        |1{0,1}[0-9]){0,1}[0-9]))'''

    if re.match(ipv4, ip_address):
        print("ip address is correct and type ipv4")

    elif re.match(ipv6, ip_address):
        print("ip address is correct and type ipv6")

    else:
        print("ip address is incorrect ")



def MacValidate(mac):
    MacAddress = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

    if re.match(MacAddress, mac):
        print("Mac address is correct")
    else:
        print("Mac address is incorrect")


def CamelToSnake(camel):
    var=camel
    if var[0].isupper:
        var=var[0].lower()+var[1:]
        for i in var:
            if i.isupper():
                print("vallide")
        else:
            print("Invalid")
    else:
        print("vallide")


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










    



   

