from django.contrib import admin
from contact.models import Contact
class contactadmin(admin.ModelAdmin):
    list_display=('fullname','fullemail1','fullmessage')
    
admin.site.register(Contact,contactadmin)

# Register your models here.
