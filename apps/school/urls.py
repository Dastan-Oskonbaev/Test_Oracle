from django.urls import path

from . import views
from global_login_required import login_not_required
from .views import TeacherRegistrationView, TeacherLogoutView, StudentDetailView, IndexView, \
    SchoolView, TeacherLoginView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('login/', login_not_required(TeacherLoginView.as_view()), name='login'),
    path('registration/', TeacherRegistrationView.as_view(), name='registration'),
    path('logout/', TeacherLogoutView.as_view(), name='logout'),
    path("school/", SchoolView.as_view(), name='school'),
    path('students/create/', views.student_create, name='student_create'),
    path('student/<int:student_id>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
