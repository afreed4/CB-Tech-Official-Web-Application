from django.contrib import admin
from django.urls import path
from cbtech_app import views,AdminViews,StaffViews,SearchViews,AccountantViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    # path('signup',views.register,name='signup'),
    path('adminlogin', views.loginadmin,name='loginadmin'),
    path('stafflogin', views.loginstaff,name='loginstaff'),
    path('accountantlogin', views.accountant_login,name='accountantlogin'),
    path('import',views.ImportEnquiryData,name='import'),
    path('enquiry',views.publicEnquiry,name='enquiry'),
  #  path('fetch_details_by_num',views.fetch_details_by_num,name='fetch_details_by_num'),
    path('register',views.Registerationform,name='StudentRegistration'),
    
    
    # Admin Paths
    path('admin-dash',views.admin_dash,name='admin-dash'),
    path('add_staff/', AdminViews.add_staff, name="add_staff"),
    path('add_staff_save/', AdminViews.add_staff_save, name="add_staff_save"),
    path('edit_staff/<int:staff_id>/', AdminViews.edit_staff, name="edit_staff"),
    path('edit_staff_save/<int:user_id>/', AdminViews.edit_staff_save, name="edit_staff_save"),
    path('delete_staff/<staff_id>/', AdminViews.delete_staff, name="delete_staff"),
    path('staff-dash',views.staff_dash,name='staffdash'),
    path('admin/', admin.site.urls),
    path('admin_profile/', AdminViews.admin_profile, name="admin_profile"),
    path('admin_home/', AdminViews.admin_home, name="admin_home"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('manage_staff/', AdminViews.manage_staff, name="manage_staff"),
    path('check_email_exist/', AdminViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', AdminViews.check_username_exist, name="check_username_exist"),
    path('add_course/', AdminViews.add_course, name="add_course"),
    path('add_course_save/', AdminViews.add_course_save, name="add_course_save"),
    path('manage_course/', AdminViews.manage_course, name="manage_course"),
    path('edit_course/<course_id>/', AdminViews.edit_course, name="edit_course"),
    path('edit_course_save/', AdminViews.edit_course_save, name="edit_course_save"),
    path('delete_course/<course_id>/', AdminViews.delete_course, name="delete_course"),
    path('add_enquiry/', AdminViews.add_Enquiry, name="add_enquiry"),
    path('add_enquiry_save/', AdminViews.add_enquiry_save, name="add_enquiry_save"),
    path('manage_enquiry/', AdminViews.manage_enquiry, name="manage_enquiry"),
    path('edit_enquiry/<int:enquiry_id>', AdminViews.edit_enquiry, name="edit_enquiry"),
    path('edit_enquiry_save/<int:enquiry_id>', AdminViews.edit_enquiry_save, name="edit_enquiry_save"),
    path('delete_enquiry/<enquiry_id>/', AdminViews.delete_enquiry, name="delete_enquiry"),
    path('manage_registeration/', AdminViews.manage_registeration, name="manage_registeration"),
    path('edit_registeration/<int:enquiry_id>', AdminViews.edit_registeration, name="edit_registeration"),
    path('edit_registeration_save/<int:enquiry_id>', AdminViews.edit_registeration_save, name="edit_registeration_save"),
    path('edit_self/', AdminViews.edit_self, name="edit_self"),
    path('update_enq_reg/', AdminViews.update_enq_reg, name="update_enq_reg"),
    path('update_cons_reg/', AdminViews.update_cons_reg, name="update_cons_reg"),
    path('repeated_user',AdminViews.repeated_user_view,name='repeated_user'),
    path('details/',AdminViews.get_staff_details,name='details'),

    #accounting paths
     path('accountant_manage/',AccountantViews.manage_enquiry, name="accountant_manage"),
     path('accountant_edit_enquiry/<enquiry_id>', AccountantViews.accountant_edit_enquiry, name="accountant_edit_enquiry"),
     path('accountant_edit_enquiry_save/<enquiry_id>', AccountantViews.accountant_edit_enquiry_save, name="accountant_edit_enquiry_save"),


    # Staff Paths
     path('staff_home/', StaffViews.staff_home, name="staff_home"),
     path('staff_add_enquiry/', StaffViews.staff_add_Enquiry, name="staff_add_enquiry"),
     path('staff_add_enquiry_save/', StaffViews.staff_add_enquiry_save, name="staff_add_enquiry_save"),
     path('staff_manage_enquiry/', StaffViews.staff_manage_enquiry, name="staff_manage_enquiry"),
     path('staff_edit_enquiry/<enquiry_id>', StaffViews.staff_edit_enquiry, name="staff_edit_enquiry"),
     path('staff_edit_enquiry_save/<enquiry_id>', StaffViews.staff_edit_enquiry_save, name="staff_edit_enquiry_save"),
     path('staff_update_password/', StaffViews.staff_update_password, name="staff_update_password"),
     path('staff_update_password_save/', StaffViews.staff_update_password_save, name="staff_update_password_save"),
     path('staff_add_course/', StaffViews.add_course, name="staff_add_course"),
     path('staff_add_course_save/', StaffViews.add_course_save, name="staff_add_course_save"),
     path('staff_manage_course/', StaffViews.manage_course, name="staff_manage_course"),
     path('staff_edit_course/<id>', StaffViews.edit_course, name="staff_edit_course"),
     path('staff_edit_course_save/', StaffViews.edit_course_save, name="staff_edit_save"),
     path('staff_import_enquiry/', views.staffImportEnquiryData, name="staff_import_enquiry"),
     path('take_attendance/<int:id>/',StaffViews.attendance_view,name='take_attendance'),
     path('attendance_report/<int:id>/', StaffViews.attendance_report_view, name='attendance_report'),
    # path('attendance_report/<id>/', StaffViews.attendance_report_view, name='attendance_report'),
     path('attendance/',StaffViews.attendance_report,name='attendance'),
     path('course_completion/',StaffViews.course_completion,name='course_completion'),

     # Search Path
    path('searchEnquiry/', SearchViews.searchEnquiry, name='searchEnquiry'),
    path('searchRegister/',SearchViews.searchRegisteration, name="searchRegister"),
    path('staffsearchEnquiry/', SearchViews.staffsearchEnquiry, name='staffsearchEnquiry'),
    path('accountantsearchRegister/',SearchViews.searchRegisterationAccountant, name='accountantsearchRegister'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
