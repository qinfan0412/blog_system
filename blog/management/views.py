from django.shortcuts import render
from django.core.paginator import Paginator
from blogindex.models import *
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import hashlib


# --------------------------密码加密
def setPassword(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result


# ----------------------登录装饰器，类似拦截器，不登录无法访问其他页面
def LoginDescribe(func):
    # 1.获取cookie中的email和session的email
    # 2.判断email是不是相等，成功跳转，失败返回登录页
    def inner(request, *args, **kwargs):
        cookie_email = request.COOKIES.get('email')
        session_email = request.session.get('email')
        if cookie_email == session_email and cookie_email and session_email:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('management//login/')

    return inner


# ---------------------------注册账户
def register(request):
    if request.method == 'POST':
        error_msg = ''
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if email:  # 判断邮箱是否存在
            loginuser = LoginUser.objects.filter(email=email).first()
            if not loginuser:  # 不存在，先判断两次密码是否相同，如果相同开始创建账户写入数据库
                if password == password2 and password != '':  # len(password)=0
                    LoginUser.objects.create(email=email, password=setPassword(password), username=username)
                    error_msg = '=============恭喜！注册成功！=============='
                else:
                    error_msg = '两次密码不一致,或者密码为空！'
            else:
                error_msg = '邮箱已被注册'
        else:
            error_msg = '邮箱不可以为空'
    return render(request, 'management/register.html', locals())


# ---------------------------------------登录页面
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_msg = ''
        if email:
            user = LoginUser.objects.get(email=email)
            if user.password == setPassword(password):
                # 密码成功跳转网页，并且设置cookie和session
                response = HttpResponseRedirect('/management/index/')
                response.set_cookie('email', email)
                request.session['email'] = user.email
                return response
            else:
                error_msg = '密码错误！请重新输入！'
        else:
            error_msg = '请输入账户后再登录！'

    return render(request, 'management/login.html', locals())


# ------------------------登出页面----------------
def logout(request):
    # 删除cookie和session
    response = HttpResponseRedirect('/management/login/')  # 返回登录页
    # response.delete_cookie('email')#删除一个cookie
    keys = request.COOKIES.keys()  # 删除多个cookie
    for i in keys:
        response.delete_cookie(i)
    del request.session['email']
    return response


# ----------------------------------首页和公共继承的父页面
@LoginDescribe
def index(request):
    return render(request, 'management/index.html')


def base(request):
    return render(request, 'management/base.html')


# ------------------------------------查看文章列表页面
def list(request, page=1):
    article = Article.objects.order_by('-date').all()
    paginator = Paginator(article, 6)
    paginator_list = paginator.page(page)
    # 如果删除文章，获取删除id
    del_id = request.GET.get('del_id')
    if del_id:
        article = Article.objects.get(id=del_id)
        article.delete()
    search_name=request.GET.get('search_name')
    print(search_name)
    return render(request, 'management/list.html', locals())


# ------------------------------------------文章添加
def article_add(request):
    type = Type.objects.all()
    author = Author.objects.all()
    if request.method == 'POST':
        article_title = request.POST.get('article_title')
        article_content = request.POST.get('article_content')
        article_description = request.POST.get('article_description')
        article_type_id = request.POST.get('article_type')
        article_author_id = request.POST.get('article_author')
        article_type = Type.objects.get(id=article_type_id)
        article_author = Type.objects.get(id=article_author_id)
        print(request.FILES.get('pic'))
        article = Article()
        article.title = article_title
        article.content = article_content
        article.description = article_description
        article.picture = request.FILES.get('pic')

        article.type = article_type
        article_author = article_author
        article.save()
    return render(request, 'management/article_add.html', locals())


# _--------------------------------------个人中心页
def personal_info(request):
    email = request.COOKIES.get('email')
    user = LoginUser.objects.get(email=email)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.age = request.POST.get('age')
        user.phone_number = request.POST.get('phone_number')
        user.gender = request.POST.get('gender')
        user.address = request.POST.get('address')
        user.photo = request.FILES.get('photo')
        user.save()

    return render(request, 'management/personal_info.html', locals())


# ---------------------------------------修改文章
def article_update(request):
    title = request.GET.get('update_title')
    article = Article.objects.filter(title=title).first()
    type = Type.objects.all()
    author = Author.objects.all()
    if request.method == 'POST':
        article_title = request.POST.get('article_title')
        article_content = request.POST.get('article_content')
        article_description = request.POST.get('article_description')
        article_type_id = request.POST.get('article_type')
        article_author_id = request.POST.get('article_author')
        article_type = Type.objects.get(id=article_type_id)
        article_author = Type.objects.get(id=article_author_id)
        print(request.FILES.get('pic'))
        article.title = article_title
        article.content = article_content
        article.description = article_description
        article.picture = request.FILES.get('pic')
        article.type = article_type
        article_author = article_author
        article.save()
    return render(request, 'management/article_update.html', locals())
