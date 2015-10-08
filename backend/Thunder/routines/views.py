from __future__ import absolute_import

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.conf import settings
@login_required
def routineView(request):
    print(settings.STATIC_ROOT)
    return render(request, 'routines/routine.html')


@login_required
def routineAddView(request):
    print('hit')
    return render(request, 'routines/routine.html')
