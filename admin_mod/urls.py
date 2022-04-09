from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='index'),
    path('login_page',views.login_page,name='login_page'),
    path('login',views.login,name='login'),
    path('register_page',views.register_page,name='register_page'),
    path('register',views.register,name='register'),
    path('base_ext',views.base_ext,name='base_ext'),
    path('add_pro_form',views.add_pro_form,name='add_pro_form'),
    path('add_pro',views.add_pro,name='add_pro'),
    path('add_project_show',views.add_project_show,name='add_project_show'),
    path('edit/<int:projectid>',views.add_pro_edit,name='add_pro_edit'),
    path('update/<int:projectid>',views.update,name='update'),
    path('add_platform_show',views.add_platform_show,name='add_platform_show'),
    path('add_platform_form',views.add_platform_form,name='add_platform_form'),
    path('add_platform',views.add_platform,name='add_platform'),
    path('platformedit/<int:platformid>',views.add_platform_edit,name='add_platform_edit'),
    path('platformupdate/<int:platformid>',views.platform_update,name='platform_update'),
    path('project_delete/<int:projectid>',views.project_delete,name='project_delete'),
    path('platform_delete/<int:platformid>',views.platform_delete,name='platform_delete'),
    path('project_view',views.project_view,name='project_view'),
    path('add_mcq',views.add_mcq,name='add_mcq'),
    path('add_mcq_form',views.add_mcq_form,name='add_mcq_form'),
    path('mcq_form',views.mcq_form,name='mcq_form'),
    path('mcqedit/<int:mcqid>',views.add_mcq_edit,name='add_mcq_edit'),
    path('mcqupdate/<int:mcqid>',views.mcq_update,name='mcq_update'),
    path('mcq_delete/<int:mcqid>',views.mcq_delete,name='mcq_delete'),
    path('course',views.course,name='course'),
    path('add_course',views.add_course,name='add_course'),
    path('add_course_form',views.add_course_form,name='add_course_form'),
    path('course_show',views.course_show,name='course_show'),
    path('course_edit/<int:courseid>',views.course_edit,name='course_edit'),
    path('course_update/<int:courseid>',views.course_update,name='course_update'),
    path('course_delete/<int:courseid>',views.course_delete,name='course_delete'),
    
]
    
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
