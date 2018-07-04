from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

'''def index(request):
    #HttpResponse类存在django.http.HttpResponsez中，以字符串的形式传递给前端页面数据
    return HttpResponse("Hello Django!")'''

def index(request):
    #render函数，该函数的第一个参数是请求对象的，第二个参数返回一个index.html页面
    return  render(request,"index.html")

#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            #set_cookie(str,,)第一个参数"user"用于表示写入浏览器的Cookie名，username表示用户再登录页上输入的用户名
            #3600表示该cookie信息在浏览器中的停留时间，默认以秒为单位
            response.set_cookie('user',username,3600)#添加浏览器cookie
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})
    else:
        return  render(request,'index.html',{'error':'username or error'})

#发布会管理
def event_manage(request):
    #读取cookie名为“user"的值
    username = request.COOKIES.get('user','') #读取浏览器cookie

    return render(request,"event_manage.html",{"user":username})