from django.shortcuts import render,HttpResponse

# Create your views here.

def login (request):
    #登录界面
    # request.method获取当前请求方式,并且是全大写的字符串形式
    # request.POST 获取用户当前提交的POST请求数据（不包含文件）
    if request.method == 'POST':
        name = request.POST.getlist('username')
        # get只会获取列表最后一个元素
        # getlist可以拿到全部
        # request.GET用法与POST一样
        print(type(name))
        print(name)
        password = request.POST.get('password')
        return HttpResponse('123')
    return render(request,'login.html')
   
    
    