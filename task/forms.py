from django import forms
from django.contrib.auth.models import User
from django.core import validators
import re


def emailvalidation(email):
    def check(email):  
        return re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)

    var1=check(email)
    if var1:
        print(email)
        raise forms.ValidationError("Email is valid")
    else:
        raise forms.ValidationError("Email is invalid")

def Date_finder(date):
    def check(date):
        return re.match(r'(\d{3}[1-9]|\d{2}[1-9]\d|\d[1-9]\d{2}|[1-9]\d{3})[-](0[1-9]|1[0-2])[-]([0-2][1-9]|2[0-9]|3[0-1])',date)
    
    var2=check(date)
    if var2:
        print(date)
        raise forms.ValidationError("Date is valid")
    else:
        raise forms.ValidationError("Date is invalid")

def NumGreaterThan100(num):
    pattern=re.compile(r'[1-9][0-9][0-9]+')
    matches=pattern.findall(num)

    if matches:
        for match in matches:
            print(match)
        raise forms.ValidationError("Number greater than 100 is present")
    else:
        raise forms.ValidationError("Number greater than 100 is not present")
        
def SingleQuote(string):
    pattern=re.compile(r"(?<=')[^']+(?=')")
    matches=pattern.findall(string)
    if matches:
        for match in matches:
            print(match)
        raise forms.ValidationError("String is found")
    else:
        raise forms.ValidationError("String is not found")

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
        raise forms.ValidationError("Ip address is valid and of type Ipv4")
    elif re.match(ipv6, ip_address):
        raise forms.ValidationError("Ip address is valid and of type Ipv6")
    else:
        raise forms.ValidationError("Ip address is invalid")


def MacValidate(mac):
    MacAddress = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

    if re.match(MacAddress, mac):
        raise forms.ValidationError("mac address is valid ")
    else:
        raise forms.ValidationError("mac address is invalid ")

def CamelToSnake(camel):
    var=camel
    if var[0].isupper:
        var=var[0].lower()+var[1:]
        for i in var:
            if i.isupper():
                raise forms.ValidationError("Correct")
        else:
            raise forms.ValidationError("Incorrect form of camelcase")
    else:
        raise forms.ValidationError("Incorrect form of camelcase")
    

class RegisterationForm(forms.Form):
    date=forms.CharField(validators=[Date_finder])
    email = forms.EmailField(validators=[emailvalidation])
    number=forms.CharField(validators=[NumGreaterThan100])
    string=forms.CharField(validators=[SingleQuote])
    IpAdress=forms.CharField(validators=[IpValidation])
    MacAdress=forms.CharField(validators=[MacValidate])
    camelcase=forms.CharField(validators=[CamelToSnake])