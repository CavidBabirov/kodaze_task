from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    id_photo_front = models.ImageField(upload_to='id_photo/')
    id_photo_back = models.ImageField(upload_to='id_photo/')
    reference_person = models.CharField(max_length=255)
    sv_finnish_code = models.CharField(max_length=20)
    bank_card = models.CharField(max_length=16)
    main_card = models.BooleanField(default=True)
    card_expiration_date = models.DateField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=255)
    workplace = models.CharField(max_length=255)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    documents = models.FileField(upload_to='user_documents/')
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.0, null=True, blank=True)
    is_approved = models.BooleanField(default=False)



class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=10)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
