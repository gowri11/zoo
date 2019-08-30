from django import forms

class UserRegistrationform(forms.Form):
    name = forms.CharField(max_length = 30)
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 20,widget=forms.PasswordInput)
    address = forms.CharField(max_length = 60)
    email = forms.EmailField()
    mobile_no = forms.CharField(max_length = 20)
    country = forms.CharField(max_length = 12)
    country_id = forms.CharField(max_length = 20)
    ctnid_no = forms.IntegerField()

class loginform(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 20,widget=forms.PasswordInput) 

class AdminPersonsform(forms.Form):
    name = forms.CharField(max_length = 30)
    sur_name = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30,widget=forms.PasswordInput)
    address = forms.CharField(max_length = 60)
    email = forms.EmailField()
    mobile_no = forms.CharField(max_length = 20)
    adhar_no = forms.CharField(max_length = 12)


class AdminLoginform(forms.Form):
    name = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30,widget=forms.PasswordInput)