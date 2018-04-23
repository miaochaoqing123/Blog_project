from django.contrib import admin
from blog.models import *

# Register your models here.
class AtrticleAdmin(admin.ModelAdmin):

    # 只显示这些内容
    # fields = ("title","desc","content")
    # 除开这些内容外
    # exclude = ("title","desc","content")

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,AtrticleAdmin)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
