from django.contrib import admin

from django.contrib import admin
from blogindex import models


admin.site.register(models.Author)
admin.site.register(models.Type)
admin.site.register(models.Article)
admin.site.register(models.LoginUser)
