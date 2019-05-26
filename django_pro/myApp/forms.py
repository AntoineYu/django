from django import forms

class RegistrerForm(forms.Form):
    name = forms.CharField(required=True,error_messages={'required': "Le nom d'utilisateur ne peut pas etre vide"})
    email = forms.EmailField(required=True,error_messages={'required': "Email ne peut pas etre vide",'invalid':"Le format de email est incorrect"})
    password = forms.CharField(min_length=6,required=True,error_messages={'required': "Password ne peut pas etre vide",'min_length': "Au moins six mots pour password"})

class LoginForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required': "Le nom d'utilisateur ne peut pas etre vide"})
    password = forms.CharField(required=True,error_messages={'required': "Password ne peut pas etre vide"})

class UserForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'required': "Email ne peut pas etre vide",'invalid': "Le format de email est incorrect"})