from django.conf.urls import url
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token)

from users import views

urlpatterns = [

    url(r'^users/$', views.UserCreate.as_view(), name='user_create'),

    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),

    url(r'^user-auth/', obtain_jwt_token, name='user_auth'),

    url(r'^token-refresh/', refresh_jwt_token),

]
