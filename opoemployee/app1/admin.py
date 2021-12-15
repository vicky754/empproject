from django.contrib import admin
from app1.models import Employee





class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['name','password','email','phone_number']


admin.site.register(Employee,EmployeeAdmin)
