from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, dept, gender, phone,password=None):
        if not email:
            raise ValueError('User must have an Email')

        user = self.model( 
            email = self.normalize_email(email),
            name = name,
            dept = dept,
            gender = gender,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, dept,  password, gender, phone):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            name = name,
            dept = dept,
            gender = gender,
            phone = phone,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

DEPARTMENTS = (
    ("CIVIL","CIVIL"),
    ("CSE","CSE"),
    ("ECE","ECE"),
    ("EEE","EEE"),
    ("MECH","MECH"),
    ("HBS","HBS"),
    ("DIPLOMA","DIPLOMA"),
    ("ADMIN","ADMIN"),
)
GENDERs = (
    ("MALE", 'MALE'),
    ("FEMALE", 'FEMALE')
)

class Account(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=20, choices=DEPARTMENTS)
    gender = models.CharField(max_length=10 ,choices=GENDERs, null=True)
    phone = models.CharField(max_length=10, null=True)

    #required  
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'name', 'dept', "gender", 'phone']


    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


