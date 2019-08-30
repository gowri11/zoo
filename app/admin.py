from django.contrib import admin

from .models import AdminPersons,TicketManagers

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','sur_name','address','email','mobile_no','adhar_no']
admin.site.register(AdminPersons,PersonAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ['name','sur_name','address','email','mobile_no','adhar_no']
admin.site.register(TicketManagers,TicketAdmin)



# Register your models here. 


