from __future__ import absolute_import

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Routine, Exercise


@login_required
def routineListView(request):
    return render(request, 'routines/routine_list.html')


@login_required
def routineAddEditView(request):
    return render(request, 'routines/routine_add_edit.html')


@login_required
def routineUseView(request):
    return render(request, 'routines/routine_use.html')
