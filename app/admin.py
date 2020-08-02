from django.contrib import admin
from app.models import userdetail
from app.models import loanapply
from app.models import transaction,transactionhistory

# Register your models here.
admin.site.register(userdetail)
admin.site.register(loanapply)
admin.site.register(transaction)
admin.site.register(transactionhistory)