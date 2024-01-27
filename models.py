from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, password, **extra_fields)
    

    # def create_user_with_2fa(self, phone_number, password=None, **extra_fields):

    #     user = self.create_user(phone_number, password, **extra_fields)
    #     TwoFactorAuth.objects.create(user=user, secret_key="generated_secret_key")
    #     return user



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    id_photo_front = models.ImageField(upload_to='id_photo/', help_text=('Şəxsiyyət vəsiqəsi'), null=True)
    id_photo_back = models.ImageField(upload_to='id_photo/', help_text=('Şəxsiyyət vəsiqəsi 2'), null=True)
    reference_person = models.CharField(max_length=255)
    sv_finnish_code = models.CharField(max_length=20)
    emergency_contact = models.CharField(max_length=255)
    workplace = models.CharField(max_length=255)
    monthly_income = models.DecimalField(max_digits=5, decimal_places=2,null=True, blank=True)
    documents = models.FileField(upload_to='user_documents/', help_text=('Istifadəçi sənədləri'))
    balance = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True, blank=True)
    is_approved = models.BooleanField(default=False)

    objects = CustomUserManager()



class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=10)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class TwoFactorAuth(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    secret_key = models.CharField(max_length=16)
    is_activated = models.BooleanField(default=False)
    safe_devices = models.JSONField(default=list)


class CardInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bank_card = models.CharField(max_length=16)
    main_card = models.BooleanField(default=True)
    card_expiration_date = models.DateField(null=True, blank=True)

