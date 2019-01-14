from django.db import models


# Create your models here.
class UserInfo(models.Model):

    class Meta:
        db_table = 'userinfo'
        verbose_name_plural = "添加用户和密码"

    user = models.CharField(max_length=30)
    opwd = models.CharField(max_length=30)
    title = models.CharField(default='添加用户的信息', max_length=50)


    def __str__(self):
    	return self.title

