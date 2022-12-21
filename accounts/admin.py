from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class AccountAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','name','dept','gender', 'password1', 'password2'),
        }),
    )

    list_display = ("email","name","dept")
    ordering = ('dept',)
    
    filter_horizontal = ()
    list_filter = ()  
    fieldsets = ()



admin.site.register(Account, AccountAdmin)