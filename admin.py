from django.contrib import admin
from user.models import CustomUser, Transaction

# Register your models here.

admin.site.register(CustomUser),
admin.site.register(Transaction)