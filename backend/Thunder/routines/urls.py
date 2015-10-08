from __future__ import absolute_import
from django.conf import settings
from django.conf.urls import url

from . import views

urlpatterns = [

    # url(r'^.*$', views.routineView, name='routine'),
    url(r'^$', views.routineView, name='routine'),

    url(r'add', 'django.contrib.staticfiles.views.serve', kwargs={
            'path': 'partials/routine/routine_add_routine.html', 'document_root': settings.STATIC_ROOT})

    # url(r'add', views.routineAddView, name='add')
]



# if settings.DEBUG:
#     urlpatterns += url(
#         r'^$', 'django.contrib.staticfiles.views.serve', kwargs={
#             'path': 'index.html', 'document_root': settings.STATIC_ROOT}),
