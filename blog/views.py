# -*- coding:utf-8 -*-
import logging
from django.shortcuts import render
from django.conf import settings
from blog.models import *
# 导入分页的库及类
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

logger = logging.getLogger("blog.views")

# Create your views here.
def global_setting(request):
    return {
        "SITE_NAME":settings.SITE_NAME,
        "SITE_DESC" :settings.SITE_DESC,
        "WEIBO_SINA":settings.WEIBO_SINA,
        "WEIBO_TENCENT" :settings.WEIBO_TENCENT,
        "PRO_RSS":settings.PRO_RSS,
        "PRO_EMAIL":settings.PRO_EMAIL,
        }


def index(request):
    try:
        # 分类信息获取,(导航数据)
        category_list = Category.objects.all()[:2]
        # 广告数据(作业)
        # 最新文章数据
        article_list = Article.objects.all()
        paginator = Paginator(article_list,2)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except (EmptyPage,InvalidPage,PageNotAnInteger):
            article_list = paginator.page(1)
    except Exception as e:
        logger.error(e)
    context = {
        'category_list': category_list,
        'article_list':article_list,
    }
    return render(request,'index.html',context=context)