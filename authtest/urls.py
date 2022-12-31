from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('<int:subject_id>/', views.detail, name='detail'),
    path('<int:subject_id>/update', views.update, name='update'),
    path('<int:subject_id>/delete', views.delete, name='delete'),
    path('<int:subject_id>/quiz', views.quiz, name='quiz'),
    path('<int:subject_id>/quiz/start', views.start, name='start'),
    path('<int:subject_id>/quiz/make', views.make, name='make'),
    path('<int:subject_id>/quiz/<int:quiz_id>', views.dt, name='dt'),
    path('<int:subject_id>/quiz/<int:quiz_id>/dl', views.dl, name='dl'),
    path('<int:subject_id>/quiz/<int:quiz_id>/ud', views.ud, name='ud'),
]