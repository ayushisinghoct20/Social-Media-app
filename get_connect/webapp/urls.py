from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'index'),
    path('settings' , views.settings , name = 'settings'),
    path('Like_post' , views.Like_post , name = 'Like_post'),
    path('follow' , views.follow , name = 'follow'),
    path('search' , views.search , name = 'search'),
    path('upload' , views.upload , name = 'upload'),
    path('profile/<str:pk>' , views.profile , name = 'profile'),
    path('signup' , views.signup , name = 'signup'),
    path('signin' , views.signin , name = 'signin'),
    path('logout' , views.signin , name = 'logout'),
    
]

   