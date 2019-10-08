# Create your views here.
from django.shortcuts import render
from blogindex.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator


def base(request):
    return render(request, 'blogindex/base.html')


def about(request):
    return render(request, 'blogindex/about.html')


def index(request):
    # 查询六条数据，查询推荐的7条数据，查询点击率排行榜9条数据
    article = Article.objects.order_by('-date')[:6]
    click_article = Article.objects.order_by('-click')[:9]
    return render(request, 'blogindex/index.html', locals())


def listpic(request):
    return render(request, 'blogindex/listpic.html')


def newslistpic(request, page=1):
    page = int(page)
    article = Article.objects.order_by("-date")
    name = request.GET.get('name')
    type_name = request.GET.get('type')
    print(name, type_name)
    # 如果输入框输入东西，则更新article
    if name:
        article = Article.objects.filter(title__contains=name).order_by("-date")
    if type_name:
        type = Type.objects.filter(name=type_name).first()
        article = Article.objects.filter(type=type).order_by("-date")

    paginator = Paginator(article, 4)  ##每页显示6条数据
    page_obj = paginator.page(page)
    ## 获取当前页
    current_page = page_obj.number
    start = current_page - 3
    if start < 1:
        start = 0
    end = current_page + 2
    if end > paginator.num_pages:
        end = paginator.num_pages
        start = end - 5
    if start == 0:
        end = 5
    page_range = paginator.page_range[start:end]
    return render(request, "blogindex/newslistpic.html", locals())


# -----------------------------文章详情页面
def articletails(request, id=2):
    # print(id)
    id = int(id)
    articletail = Article.objects.get(id=id)
    print(articletail.picture)
    return render(request, 'blogindex/articletails.html', locals())


# ------------------------分页-------------


def fytetx(request):
    aritcle = Article.objects.all().order_by('-date')
    # 每次显示五条数据
    paginator = Paginator(aritcle, 5)  # 设置每一页显示多少条
    print(paginator.count)  # 返回的总条数.
    print(paginator.page_range)  # 可迭代的页数
    print(paginator.num_pages)  # 最大页数

    page_obj = paginator.page(20)
    print(page_obj)  # 可以有的页数的数据  表示的当前对象  <Page 20 of 21>
    print(page_obj.number)  # 当前页数
    print(page_obj.has_next())  # 判断有没有下一页
    print(page_obj.has_other_pages())  # 判断是否有其他页
    print(page_obj.has_previous())  # 判断是否有上一页
    print(page_obj.next_page_number())  # 返回下一页的代码，如无下一页抛出异常
    print(page_obj.previous_page_number())  # 同上，上一页页码


# _-----------------------------------------请求测试
def reqtest(request):
    # 获取get请求的参数
    data = request.GET
    # 获取post请求的参数
    data = request.POST
    print(data)  # 查看post携带的参数
    print(data.get('name'))  # 获取地址栏的键值为name的值
    print(request.COOKIES)  # 用户的身份
    print(request.scheme)  # https还是http
    print(request.method)  # 查看请求的方式
    print(request.path)  # 查看请求的路径
    print(request.body)  # 查看请求的主体，返回一个字符串
    print(request.META)  # 包含了具体的请求数据，包含所有的http请求的信息信息
    print(request.META.get('OS'))  # 请求的系统
    print(request.META.get('HTTP_USER_AGENT'))  # 发出请求的浏览器的版本
    print(request.META.get('HTTP_HOST'))  # 请求的主机
    print(request.META.get('HTTP_REFERER'))  # 请求的来源

    return HttpResponse('请求测试')
