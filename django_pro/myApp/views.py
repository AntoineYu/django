from django.shortcuts import render,render_to_response
from django.views import View
from .forms import RegistrerForm,LoginForm,UserForm
from .models import User
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
class RegistrerView(View):
     def get(self,request):
         registrer_form = RegistrerForm()
         return render(request,'registrer.html',{'registrer_form':registrer_form})

     def post(self,request):
         registrer_form = RegistrerForm(request.POST)
         if registrer_form.is_valid():
             name = request.POST['name']
             email = request.POST['email']
             password = request.POST['password']
             isMatch = User.objects.filter(uname=name)

             if isMatch:
                 return render(request,'registrer.html',{'registrer_form':registrer_form})
             user = User()
             user.uemail = email
             user.uname =  name
             user.upwd = password
             user.save()
             return render(request,'login.html')
         else:
             return render(request,'registrer.html',{'registrer_form':registrer_form})


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        login_form = LoginForm(request.POST)
        user = User()
        if login_form.is_valid():
            name = request.POST['name']
            password = request.POST['password']
            result = User.objects.filter(uname=name,upwd=password).exists()
            if result:
                response = HttpResponseRedirect('/login/user/')
                response.set_cookie('username', name, 3600)
                return response
            else:
                return render(request,'login.html',{'msg':"Le nom d'utilisateur ou le mot de passe est incorrect"})
        else:
            return render(request,'login.html',{'login_form':login_form})


def get(request):
    username = request.COOKIES.get('username', '')
    email = User.objects.get(uname=username).uemail
    return render_to_response('user.html', {'username': username,'email':email})

def ajax(request):
        # username = request.COOKIES.get('username', '')
        # email = User.objects.get(uname=username).uemail
    if request.is_ajax():
        # user_form = UserForm(request.POST)
        username = request.COOKIES.get('username', '')
        useremail = request.POST.get("mail")
        user = User.objects.get(uname=username)
        user.uemail = useremail
        user.save()
        return HttpResponse(useremail)
    else:
        return render(request,"user.html")

def logout(request):
    username = request.COOKIES.get('username', '')
    if username:
        response = HttpResponseRedirect('/login/')
        response.delete_cookie('username', username, 3600)
        return response
    else:
        return HttpResponse('Veuillez vous connecter d\'abord')

