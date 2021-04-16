from django.urls import path
from . import views
from .views import SignUpView #, ProfileUpdate, profile


app_name = 'accounts'

urlpatterns = [
    path('register/' , SignUpView.as_view(), name='register'),
    #path('profile/' , ProfileUpdate.as_view(), name='profile'),

    #path('test/' , views.profile, name='test'),
    #path('test/<int:id>/', )
    #path('register/' , register , name='register') , 
    # path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change') , 
    # path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done') , 
    # path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset') , 
    # path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done') , 


# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

]


# from django.urls import path

# from . import views

# app_name = 'polls'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     ...
# ]