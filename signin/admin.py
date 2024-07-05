from django.contrib import admin
from signin.models import Signin
class signinadmin(admin.ModelAdmin):
    list_display=('username1','email','password1')
    
admin.site.register(Signin,signinadmin)

