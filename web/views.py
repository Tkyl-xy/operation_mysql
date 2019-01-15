from django.shortcuts import render
from web import models

# Create your views here.
def index(request):
	pass


def son(request):
	pass


def login(request):
	pass



# 这里是增加数据库的方式
# def show(request):
# 	if request.method == 'POST':
# 		a_user = request.POST['a_user']
# 		a_pwd = request.POST['a_pwd']
# 		#第一种增加数据方式
# 		# models.UserInfo.objects.create(user=a_user, opwd=a_pwd)

# 		#第二种增加数据方式
# 		# obj = models.UserInfo(user=a_user, opwd=a_pwd)
# 		# obj.save()

# 		#第三种增加数据的方式
# 		dic = {'user':a_user, 'opwd':a_pwd}
# 		models.UserInfo.objects.create(**dic)


# 	user_list = models.UserInfo.objects.all() #取出该表所有的数据

# 	return render(request, 'show.html', {'user_list' : user_list})
'''
#这里是删除数据的方式
def show(request):

	if request.method == 'POST':
		a_user = request.POST['a_user']
		a_pwd = request.POST['a_pwd']

		#删除数据
		models.UserInfo.objects.filter(user=a_user).delete()

	user_list = models.UserInfo.objects.all()
	return render(request, 'show.html', {'user_list' : user_list})
'''

#这里是修改数据库里的数据方式
def show(request):
	if request.method == 'POST':
		a_user = request.POST['a_user']
		a_pwd = request.POST['a_pwd']

		#这里是第一种修改数据的方式
		# models.UserInfo.objects.filter(user=a_user).update(opwd=a_pwd)

		#这里是第二种修改数据的方式
		obj = models.UserInfo.objects.get(user=a_user)
		obj.opwd = a_pwd
		obj.save()


	user_list = models.UserInfo.objects.all()
	return render(request, 'show.html', {'user_list' : user_list})


def home(request):
	if request.method == 'POST':
		a_name = request.POST['a_name']
		
		models.Addtime.objects.create(name = a_name)

	
	result = models.Addtime.objects.all()
	return render(request, 'home.html', {'result' : result})