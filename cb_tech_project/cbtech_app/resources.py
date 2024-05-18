from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Enquiry

class EnquiryResource(resources.ModelResource):
    class Meta:
        model = Enquiry

class EnquiryAdmin(ImportExportModelAdmin):
    resource_class = EnquiryResource
    # Fields to display in the admin interface (optional)
    list_display = ['enquiry_id', 'name', 'phone_no', 'email_id']

admin.site.register(Enquiry, EnquiryAdmin)
