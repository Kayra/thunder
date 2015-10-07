from __future__ import absolute_import

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def routineView(request):
    return render(request, 'routines/routine.html')
