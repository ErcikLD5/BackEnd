from django.urls import path
from primera_app import views

urlpatterns = [
    path('', views.index),
    path('formpage/',views.form_user_view,name='form_user_view')
]
