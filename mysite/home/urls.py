from django.urls import path


from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='homepage'),
    path('student/', views.index1, name='student'),
    path('teacher/', views.index2, name='teacher'),
    path('login/', views.index3, name='login'),
    path('edit/', views.index4, name='edit'),
]