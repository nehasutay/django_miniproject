from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userdetail(models.Model):

	fullname=models.CharField(max_length=140, null=True)
	address=models.CharField(max_length=30)
	mobile=models.IntegerField()
	adhar_no=models.IntegerField()
	#payment=models.IntegerField(max_length=30)
	#pending=models.IntegerField(max_length=30)
	#loan_details=models.IntegerField(max_length=30)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

class loanapply(models.Model):
	name1=models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	mobile=models.IntegerField()
	adhar_no=models.IntegerField()
	credit=models.IntegerField(null=True)
	loan_amount=models.IntegerField()
	member=models.ForeignKey(User,on_delete=models.CASCADE)

class transaction(models.Model):
	start=models.DateField()
	end=models.DateField()
	paid=models.IntegerField(null=True)
	remaining=models.IntegerField(null=True)
	principal=models.IntegerField(null=True)
	interest=models.IntegerField(null=True)
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

class transactionhistory(models.Model):
	histdate = models.DateField()
	description= models.CharField(max_length=30)
	cheque=models.IntegerField()
	debit=models.IntegerField()
	credit=models.IntegerField()
	balance=models.IntegerField()
	owner=models.ForeignKey(User,on_delete=models.CASCADE)

		


