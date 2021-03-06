from django.db import models
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

class Users(User):

	class Meta:
			verbose_name = 'Users'


class Events(models.Model):
	def __unicode__(self):
	 		return self.title

	title= models.CharField(max_length=30)
	description= models.TextField(max_length=50)
	event_date=models.DateField()
	event_time= models.TimeField()
	# def __unicode__(self):
	# 		return self.content
	# def save(self, **kwargs):
	# 		super(Post, self).save(**kwargs)

class Front_Users(models.Model):
	def __unicode__(self):
	 		return self.name
	SALT_SIZE = 8

	name= models.CharField(max_length=100)
	email= models.CharField(max_length=50,unique=True)
	password=models.CharField(max_length=255)
	date_joined=models.CharField(max_length=50)
	key=models.TextField(max_length=255)
	

class Roles(models.Model):
	def __unicode__(self):
			return self.role

	
	role=models.CharField(max_length=100)


class User_roles(models.Model):
	
	user_id=models.ForeignKey(Front_Users,on_delete=models.CASCADE)
	role_id=models.ForeignKey(Roles,on_delete=models.CASCADE)
	sub_date=models.DateField(default=datetime.now)
	exp_date=models.DateField(default=datetime.now)
	amount=models.CharField(max_length=100,blank=True)
	tran_id=models.CharField(max_length=255,blank=True)	
	
class Subscription_log(models.Model):

	user_id=models.ForeignKey(Front_Users,on_delete=models.CASCADE)
	role_id=models.ForeignKey(Roles,on_delete=models.CASCADE)
	sub_date=models.CharField(max_length=100)
	exp_date=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)
	tran_id=models.CharField(max_length=255,blank=True)