from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='index'),
    path('ckeditor/upload/', views.ck_editor_5_upload_file, name='ck_editor_5_upload_file')
]
