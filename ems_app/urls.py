from . import views
from django.urls import path
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    #index path
    path('',views.index,name='index'), #home Page
    #interns path
    path('signin',views.signin,name='signin'), #Intern Signin
    path('signup',views.signup,name='signup'), #Intern Signup
    path('internsdash',views.internsdash,name='internsdash'), #Intern dash
    path('ilogout',views.ilogout,name='ilogout'), #Intern Signout
    path('answersubmit/<int:moduleid>',views.answersubmit,name='answersubmit'), #Answer submit page
    path('ineditprofile/<int:id>',views.ineditprofile,name='ineditprofile'),


    #Employee path
    path('esignup',views.esignup,name='esignup'), #employee signup
    path('esignin',views.esignin,name='esignin'), #employee signin
    path('edash',views.edash,name='edash'), #employee dash
    path('elogout',views.ilogout,name='elogout'), #employee signout
    
    
    path('internlist',views.internlist,name='internlist'), #display internlist
    path('editdomain/<int:id>',views.editdomain,name='editdomain'),#Change domain for intern
    path('domaininternlist/<str:dname>',views.domaininternlist,name='domaininternlist'), #view interns list assigned to the different domain
    path('activate_account/<int:user_id>',views.activate_account,name='activate_account'), #to activate internaccount 
    path('deactivate_account/<int:user_id>',views.deactivate_account,name='deactivate_account'), #to deactivate internaccount

    path('createmodule',views.createmodule,name='createmodule'),# Creating module in domains
    path('modulelist/<str:dname>',views.modulelist,name='modulelist'), #list the module data 
    path('updatemodule/<int:id>',views.updatemodule,name='updatemodule'), #updating module
    path('deletemodule/<int:id>',views.deletemodule,name='deletemodule'), #deleting module

    path('modulecompletionstatus/<str:dname>',views.modulecompletionstatus,name='modulecompletionstatus'), # module completion status
    path('answer_detail/<int:intern_id>/<int:module_id>/', views.answer_detail, name='answer_detail'), # Showing  the answers of user
    path('empedit/<int:id>',views.empedit,name='empedit'), #edit profile of the employee

    path('password_reset/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'), #using django inbuild password reset method take to email input page
    path('password_reset_done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),# after email show message that it is sent to registered mail id
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'), #get specific url for reset password with two field of passwords
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),#password reseted and provide link to home page


]

