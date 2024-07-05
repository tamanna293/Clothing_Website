from django.contrib import admin
from login.models import Login
from login.models import Join
class loginadmin(admin.ModelAdmin):
    list_display=('username','password')
    
admin.site.register(Login,loginadmin)

# Register your models here.

class loginadmin(admin.ModelAdmin):
    list_display=('Namej','Instaj','Bdatej','Numberj','Emailj')
    
admin.site.register(Join,loginadmin)

