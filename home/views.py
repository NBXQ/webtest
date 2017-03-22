# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from home.models import User

def add(request):
	name=request.GET['name']
	age=request.GET['age']
	hobby=request.GET['hobby']

	test1=User(name=name,age=age,hobby=hobby)
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")

def update(request):
	name=request.GET['name']
	age=request.GET['age']
	hobby=request.GET['hobby']	
	User.objects.filter(name=name).update(age=age,hobby=hobby)
	return HttpResponse("<p>数据库更新成功</p>")

def delete(request):
	name=request.GET['name']
	User.objects.filter(name=name).delete()
	return HttpResponse("<p>数据删除成功</p>")

def add2(request,name,age,hobby):
	test1=User(name=name,age=age,hobby=hobby)
	test1.save()
	return HttpResponse("<p>数据添加成功！</p>")
