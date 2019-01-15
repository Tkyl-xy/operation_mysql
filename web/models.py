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


class Addtime(models.Model):

    class Meta:
        db_table = 'add_time'
        verbose_name_plural = "日期及其他类型"

    name = models.CharField(max_length=30)
    ctime = models.DateTimeField(auto_now=True)
    uptime = models.DateTimeField(auto_now_add=True)
    info  = models.CharField(max_length=50)
    email = models.EmailField(max_length=30, null=True)
    email2 = models.EmailField(max_length=50, default='yang123@qq.com')
    ip = models.GenericIPAddressField(protocol="ipv4", null=True,blank=True)
    img = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
    	return self.info
        
    
class Choices(models.Model):

	class Meta:
		db_table = 'choices'
		verbose_name_plural = '下拉框样式'

	LIST = (
			(1, 'user'),
			(2, 'admin'),
			(3, 'like'),
		)
	user_type = models.IntegerField(choices=LIST, default=1, verbose_name='下拉选择')


class Game(models.Model):
	gname = models.CharField(max_length=30)

class Host(models.Model):
	hostname = models.CharField(max_length=30)
	#Foreignkey是一对多，在django2.0后面要加上on_delete=models.cascade
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
