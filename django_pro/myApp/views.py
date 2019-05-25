from django.shortcuts import render,render_to_response
from django.views import View
from .forms import RegistrerForm,LoginForm
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

class UserView(View):
    def get(self,request):
        username = request.COOKIES.get('username', '')
        email = User.objects.get(uname=username).uemail
        return render_to_response('user.html', {'username': username,'email':email})
    # def post(self,request):
    #     if request.is_ajax():
    #         useremail = request.POST.get("mail")
    #         return HttpResponse(useremail)
    #     else:
    #         return render(request,"user.html")
    def ajax(self,request):
        # username = request.COOKIES.get('username', '')
        # email = User.objects.get(uname=username).uemail
        if request.is_ajax():
            useremail = request.POST.get("mail")
            return render('user.html', {'email':useremail})
        else:
            return render(request,"user.html")

# Ajax post请求的后端处理函数
# class TryView(View):
#     def get(self,request):
#         return render(request,"try.html")

    # Ajax get请求的后端处理函数
class TryView(View):
    def get(self,request):
        return render(request, "try.html")
    def comments_upload(self,request):
        if request.method == 'POST':
            print("it's a test")  # 用于测试
            print(request.POST['name'])  # 测试是否能够接收到前端发来的name字段
            print(request.POST['password']) # 用途同上
            return HttpResponse("表单测试成功")  # 最后返会给前端的数据，如果能在前端弹出框中显示我们就成功了
        else:
            return HttpResponse("<h1>test</h1>")
