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
	user_list = models.UserInfo.objects.all() #取出该表所有的数据

	return render(request, 'show.html', {'user_list' : user_list})