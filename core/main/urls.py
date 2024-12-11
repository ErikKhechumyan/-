from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('s/',views.service,name='Service'),
    path('a/',views.About,name='About'),
    path('p/',views.project,name='Project'),
    path('t/',views.testimonial,name='Testimonial'),
    path('c/',views.contact,name='Contact'),
    path('register/',views.register_request,name='register'),
    path('logout/',views.logout_request,name='logout'),
    path('login/',views.login_request,name='login'),
    path('job.html/', views.job, name='Job'),
]