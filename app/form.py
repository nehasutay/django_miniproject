from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import userdetail
from app.models import loanapply
from app.models import transaction,transactionhistory

class createuserform(UserCreationForm):
	class Meta:
		model=User
		fields=['username', 'email','password1','password2']

class memberform(ModelForm):
	class Meta:
		model=userdetail
		fields=['fullname','address','mobile','adhar_no']

class loanform(ModelForm):
	class Meta:
		model=loanapply
		fields=['name1','address','mobile','adhar_no','credit','loan_amount']


class transform(ModelForm):
 	class Meta:
 		model=transaction
 		fields=['start','end','paid','remaining','principal','interest']

class histform(ModelForm):
	class Meta:
 		model=transactionhistory
 		fields=['histdate','description','cheque','debit','credit','balance']
