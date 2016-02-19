from django.conf.urls import url

from users import views

urlpatterns = [

    url(r'^users/$', views.UserCreate.as_view()),

    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

]
