from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),
    path('student_details/', views.student_create_view, name='student_create'),
    path('ajax/load-course/', views.load_course, name='ajax_load_course'),
    path('student_info/<int:id>/', views.student_info, name='student_info')
]
