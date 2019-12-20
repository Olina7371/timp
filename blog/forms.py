from django.views.generic import View
from django import forms
from .models import *
from django.core.exceptions import ValidationError
class registration(forms.Form):
    # file = forms.FileField(
    #     widget=forms.FileInput(attrs={"type": "file", "class": "form-control-file", "id": "exampleFormControlFile1"}))
    Name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "block6", "type": "text", "name": "name", "placeholder": "ФИО"}))
    login = forms.CharField(
        widget=forms.TextInput(attrs={"class": "block6", "type": "text", "name": "login", "placeholder": "Login"}))
    Email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "block6", "type": "email", "name": "Email", "placeholder": "Email"}))
    Phone = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "block6", "type": "text", "name": "number phone", "placeholder": "Номер телефона"}))
    Password = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "block6", "type": "password", "name": "password", "placeholder": "Пароль"}))
    Password_return = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "block6", "type": "password", "name": "password_return",
                   "placeholder": "Повторите пароль"}))
    def clean_Password_return(self):
        pas = self.cleaned_data
        pas0 = pas['Password']
        pas1 = pas['Password_return']
        if pas0 != pas1:
            raise ValidationError('asd')
        else:
            return '200'
    def clean_login(self):
        login = self.cleaned_data
        login_ac = Acconts.objects.filter(login=login['login']).values()
        if login_ac:
            raise ValidationError('Такой пользователь есть')
        else:
            return login['login']
    def sign_up(self):
        new_user = self.cleaned_data
        print(new_user)
        name = new_user['Name']
        login = new_user['login']
        password = new_user['Password']
        phone = new_user['Phone']
        password_return = new_user['Password_return']
        email = new_user['Email']
        contacts = Contacts.objects.create(phone_number=phone,email=email)
        contacts.save()
        print(contacts)
        accontw= Acconts.objects.create(login=login,password=password)
        accontw.save()
        print(accontw)
        user = User.objects.create(Name=name, contact=contacts,account=accontw)
        user.save()

        return 'site'
class auth(forms.Form):
    def sign_in(self):
        user = self.data
        login = user.get('login')
        pas = user.get('password')
        ac = Acconts.objects.filter(login=str(login)).values()
        if  ac:
            passw=ac[0].get('password')
            if str(passw) == str(pas):
                ac.update(authecation=True)
                return 'profile'
        else:
            return 'site'
class notions1(forms.Form):
    def create_notion(self):
        text = self.data
        ac = Acconts.objects.filter(authecation=True).get()
        notes1 = Notes.objects.create(inform=text['Text'],accounts=ac)
        notes1.save()
