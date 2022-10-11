from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib import admin

# Register your models here.
from .models import *

class UserCreationFormExtended(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super(UserCreationFormExtended, self).__init__(*args, **kwargs) 
        self.fields['email'] = forms.EmailField(label=("E-mail"), max_length=150)


UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ( 'username','email' ,'password1', 'password2',)
    }),
)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)