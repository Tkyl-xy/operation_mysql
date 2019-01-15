from django.contrib import admin

# Register your models here.
from web import models
#把models创建的表，添加到admin后台中
admin.site.register(models.UserInfo)
admin.site.register(models.Addtime)
admin.site.register(models.Choices)
admin.site.register(models.Game)
admin.site.register(models.Host)