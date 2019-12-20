from django.http import HttpResponse,JsonResponse

from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .forms import *
import json
from django.contrib.auth import login,authenticate
# Create your views here.
def Site(request):
    file = Notes.objects.all()
    return render(request, 'index.html', context={'product': file})


class Registration(View):
    def get(self, request):
        form_registr = registration()
        return render(request, 'blog/регистрация.html', context={'form': form_registr})

    def post(self, request):
        form_registr = registration(data=request.POST)
        if form_registr.is_valid():
            abament = form_registr.sign_up()
            return redirect(abament)
        return render(request, 'blog/регистрация.html', context={'form': form_registr})
class Auth(View):
    def get(self, request):
        return render(request, 'blog/авторизация.html')

    def post(self, request):
        auth_registr = auth(request.POST)
        if auth_registr.is_valid():
            user = auth_registr.sign_in()
            if user == 'profile':
                request.session['user'] = {'login': request.POST.get('login')}
            return redirect(user)
        return render(request, 'index.html', context={'form': auth_registr})

class logout(View):
    def get(self,request):
        user =Acconts.objects.filter(authecation=True).values()
        if user:
            user.update(authecation=False)
            return render(request,'index.html')
        return render(request,'index.html')
class Nots(View):
    def get(self,request):
        return render(request,'blog/Notion.html')
    def post(self,reguest):
        notions = notions1(reguest.POST)
        if notions.is_valid() and reguest.POST.get('Text'):
            notions2 =notions.create_notion()
            return  redirect('profile')
        return render(reguest,'blog/Notion.html')
class Profile(View):
    def get(self,request):
        user = Acconts.objects.filter(authecation=True).values()
        if user:
            nots = Notes.objects.filter(accounts=Acconts.objects.filter(authecation=True).get()).all()
            account = User.objects.filter(account=Acconts.objects.filter(authecation=True).get()).all()

            return render(request, 'blog/profile.html',context={'notes':nots,'name':account.values()[0]})
        return render(request, 'index.html')
    def post(self,request):
        pass
class Delete_notes(View):
    def post(self,request):
        id = request.POST.get('id')
        Notes.objects.filter(id=id).delete()
        return redirect('profile')
class Calendare(View):
    def get(self,request):
        return  render(request,'blog/calendare.html')
