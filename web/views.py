from django.shortcuts import render
from web import models

# Create your views here.
def index(request):
	pass


def son(request):
	pass


def login(request):
	pass


def show(request):
	if request.method == 'POST':
		a_user = request.POST['a_user']
		a_pwd = request.POST['a_pwd']
		#第一种增加数据方式
		# models.UserInfo.objects.create(user=a_user, opwd=a_pwd)

		#第二种增加数据方式
		# obj = models.UserInfo(user=a_user, opwd=a_pwd)
		# obj.save()

		#第三种增加数据的方式
		dic = {'user':a_user, 'opwd':a_pwd}
		models.UserInfo.objects.create(**dic)


	user_list = models.UserInfo.objects.all() #取出该表所有的数据

	return render(request, 'show.html', {'user_list' : user_list})