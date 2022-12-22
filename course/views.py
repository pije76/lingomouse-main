from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from .models import *

from itertools import chain

class BulkLevelSet(View):
    def get(self, request):
        return JsonResponse({'message': 'Not implemented yet'})

    def post(self, request):
        words = request.POST.getlist('words[]')
        course_id = request.POST.get('course_id')
        level_id = request.POST.get('level_id')

        Word.objects.filter(id__in=words).update(level_id=level_id)

        return JsonResponse({'message': 'Success', 'data': course_id, 'words': words})


def course_index(request):
    page_title = _('Select course to change')

    context = {
        'title': page_title,
    }

    return render(request,'course/course_index.html', context)


def course_list(request):
    page_title = _('Select course to change')
    data_course =   Course.objects.all()

    context = {
        'title': page_title,
        'data_course': data_course,
    }

    return render(request,'course/course_list.html', context)


def level_list(request):
    page_title = _('Select level to change')
    data_level =   Level.objects.all()


    context = {
        'title': page_title,
        'data_level': data_level,
    }

    return render(request,'course/level_list.html', context)



def word_list(request):
    page_title = _('Select word to change')
    data_word =   Word.objects.all()


    context = {
        'title': page_title,
        'data_word': data_word,
    }

    return render(request,'course/word_list.html', context)
