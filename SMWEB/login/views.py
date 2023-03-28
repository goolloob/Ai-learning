from django.shortcuts import render,HttpResponse

# Create your views here.

def login (request):
    #登录界面
     # request.method获取当前请求方式,并且是全大写的字符串形式
    if request.method == 'POST':
        return HttpResponse('123')
    return render(request,'login.html')
   
    
    