from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *



# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Courses)
admin.site.register(Enquiry)
#admin.site.register(Attendence)
# @admin.register(Enquiry)
# class EnquiryAdmin(ImportExportModelAdmin):
#     list_display = ['name','email_id']
