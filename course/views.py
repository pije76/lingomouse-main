from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext_lazy as _
from django.views import View

from .models import *
from .forms import *
from .exim import *

from itertools import chain
from tablib import Dataset


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
	page_title = _('Course')

	context = {
		'title': page_title,
	}

	return render(request,'course/course_index.html', context)


########### COURSE VIEW ############
def course_list(request):
	page_title = _('Select course to change')
	list_course =   Course.objects.all()

	context = {
		'title': page_title,
		'list_course': list_course,
	}

	return render(request,'course/course_list.html', context)


def course_detail(request, pk):
	page_title = _('Change Course')
	course_detail = get_object_or_404(Course, id=pk)
	get_language = Language.objects.all()
	native_id = Course.objects.filter(id=pk).values_list("native", flat=True).first()
	foreign_id = Course.objects.filter(id=pk).values_list("foreign", flat=True).first()
	get_level = Level.objects.filter(course=pk)
	get_word = Word.objects.filter(course=pk)
	word_id = Course.objects.filter(id=pk).values_list("words")

	intial = {
		'id': course_detail.id,
		'name': course_detail.name,
		'native': course_detail.native,
		'foreign': course_detail.foreign,
		'description': course_detail.description,
		'img': course_detail.img,
		'is_active': course_detail.is_active,
	}

	# form = Word_ModelFormSet(prefix='course')

	if request.method == 'POST':
		form = Word_ModelFormSet(request.POST or None, request.FILES)
		word_formset = Word_ModelFormSet(request.POST or None)

		if form.is_valid():
			save_course = form.save(commit=False)
			save_course.id = form.cleaned_data['id']
			save_course.name = form.cleaned_data['name']
			save_course.native = form.cleaned_data['native']
			save_course.foreign = form.cleaned_data['foreign']
			save_course.description = form.cleaned_data['description']
			save_course.img = form.cleaned_data['img']
			save_course.is_active = form.cleaned_data['is_active']
			save_course.save()

			messages.success(request, _('Your course has been change successfully.'))
			return redirect('course:course_detail', id=save_course.id)
		else:
			messages.warning(request, form.errors)

	else:
		# form = Word_ModelFormSet()
		form = CourseModelForm(instance=course_detail)
		word_formset = Word_ModelFormSet()

	context = {
		'title': page_title,
		'form': form,
		'word_formset': word_formset,
		'course_detail': course_detail,
		'get_language': get_language,
		'native_id': native_id,
		'foreign_id': foreign_id,
		'get_level': get_level,
		'get_word': get_word,
		'word_id': word_id,
	}

	return render(request, 'course/course_detail.html', context)


def course_add(request):
	page_title = _('Add Course')
	# course = get_object_or_404(Course, id=pk)
	word = Word.objects.all()
	native_id = request.GET.get('get_selected_native', None)
	native_id = request.POST.get('get_selected_native', None)
	# print("native_id0", native_id)
	# print("native_id1", native_id)
	# get_language = Language.objects.filter().values("code")
	get_language = Language.objects.all().values_list("code", flat=True)
	# get_language = Course.objects.all().values_list("native", flat=True)
	# get_language = Language.objects.filter(book__title__startswith='hello')
	get_level = Level.objects.all().values_list("name", flat=True)

	# # get_language = len(get_language)
	# post.attending_set.all()

	# get_language = list(get_language)
	# # print("get_language", get_language)
	# print("get_language", get_language)

	# obj = []

	# for item in get_language:
	# 	language = pycountry.languages.lookup(item)
	# 	# language = pycountry.languages.get(alpha_2=item)
	# 	language = language.name
	# 	# print("language", language)
	# 	if language and language not in obj:
	# 		obj.append(language)

	# print("obj", obj)

	# language_list = [item.name for item in pycountry.languages]
	# language_tuples = ((item, item) for item in language_list)

	# list3 = []

	# for item in obj:
	# 	print("item", item)
	# 	if item and item in language_list:
	# 		# print("obj", obj)
	# 		# print("language_list", language_list)
	# 		list3.append(item)
	# 		print("item", item)


	# print("list3", list3)
	# print("language_tuples", language_tuples)
	# print("obj", type(obj))


	# for item in get_language:
	#     language = pycountry.languages.get(alpha_2=item).name
	#     languages.append(language)

	# for item in get_language:
	#     obj = pycountry.languages.get(alpha_2=item).name
	#     print("obj", obj)

	# LANG_CHOICES = [(language.alpha_2, language.name) for language in pycountry.languages if hasattr(language, 'alpha_2')]


	# LANG_CHOICES = [(language.name) for language in pycountry.languages]
	# LANG_CHOICES = [(item.alpha_2, item.name) for item in pycountry.languages if hasattr(item, 'alpha_2')]

	# print("LANG_CHOICES", LANG_CHOICES)
	# print("LANG_CHOICES", type(LANG_CHOICES))

	# # for y in LANG_CHOICES:
	# #     # print("y", y)
	# #     if get_language == y:
	# #         list3.append(y)

	# list3 = set(obj) & set(LANG_CHOICES)
	# list3 = set(obj).intersection(set(LANG_CHOICES))

	# # # print("obj", obj)
	# # # print("LANG_CHOICES", LANG_CHOICES)

	# list3 = list(list3)
	# print("list3", list3)
	# print("list3", type(list3))
	# # print("tuple1", tuple1)
	# print("tuple1", type(tuple1))



	if request.method == 'POST':
		form = CourseModelForm(request.POST or None, request.FILES)
		word_formset = Word_ModelFormSet(request.POST or None)
		native_id = request.GET.get('get_selected_native', None)
		native_id = request.POST.get('get_selected_native', None)

		if form.is_valid():
			# course = Course()
			course = form.save(commit=False)
			course.id = form.cleaned_data['id']
			course.name = form.cleaned_data['name']
			course.native = form.cleaned_data['native']
			# course.foreign = form.cleaned_data['foreign']
			course.description = form.cleaned_data['description']
			course.img = form.cleaned_data['img']
			course.is_active = form.cleaned_data['is_active']
			course.save()

			return redirect('course:course_list')
		else:
			messages.warning(request, form.errors)

		if word_formset.is_valid():
			get_admission_date_admission = Admission.objects.filter(patient=patients).values_list("date_admission", flat=True).first()

			for item in admision_formset:
				admision_formset_profile = Admission()
				admision_formset_profile.patient = patients
				admision_formset_profile.date_admission = get_admission_date_admission
				admision_formset_profile.time_admission = get_admission_time_admission
				admision_formset_profile.admitted_admission = str(get_admission_admitted_admission)
			return redirect('course:course_list')
		else:
			messages.warning(request, admision_formset.errors)

	else:
	# if request.method == 'GET':
		form = CourseModelForm()
		# form = CourseForm(prefix='course')
		word_formset = Word_ModelFormSet()
		# native_id = request.GET.get('get_selected_native', None)
		# native_id = request.POST.get('get_selected_native', None)

	context = {
		'title': page_title,
		'form': form,
		'word_formset': word_formset,
		'word': word,
		'get_level': get_level,
	}

	return render(request, 'course/course_add.html', context)


def course_delete(request, pk):
	course_data = get_object_or_404(Course, id=pk)
	course_data.delete()

	return redirect('course:course_list')


########### LEVEL VIEW ############
def level_list(request):
	page_title = _('Select level to change')
	list_level =   Level.objects.all()

	context = {
		'title': page_title,
		'list_level': list_level,
	}

	return render(request,'course/level_list.html', context)


def level_add(request):
	page_title = _('Change Course')
	# course = get_object_or_404(Course, id=pk)
	word = Word.objects.all()

	form = CourseForm()

	if request.method == 'POST':
		form = CourseForm(request.POST or None, instance=request.user)

		if form.is_valid():
			course = form.save(commit=False)
			course.full_name = form.cleaned_data['full_name']
			course.email = form.cleaned_data['email']
			course.ic_number = form.cleaned_data['ic_number']
			course.save()

			messages.success(request, _('Your course has been change successfully.'))
			return redirect('course:level_list')
		else:
			messages.warning(request, form.errors)

	else:
		form = CourseForm()

	context = {
		'title': page_title,
		'form': form,
		'word': word,
	}

	return render(request, 'course/level_add.html', context)


def level_detail(request, pk):
	page_title = _('Change Level')
	form = CourseForm()
	level = get_object_or_404(Level, id=pk)

	if request.method == 'POST':
		form = CourseForm(request.POST or None, instance=request.user)

		if form.is_valid():
			level = form.save(commit=False)
			level.full_name = form.cleaned_data['full_name']
			level.email = form.cleaned_data['email']
			level.ic_number = form.cleaned_data['ic_number']
			level.save()

			messages.success(request, _('Your level has been change successfully.'))
			return redirect('course:level_list')
		else:
			messages.warning(request, form.errors)

	else:
		form = CourseForm()

	context = {
		'title': page_title,
		'form': form,
		'level': level,
	}

	return render(request, 'course/level_detail.html', context)


def level_delete(request, pk):
	level_data = get_object_or_404(Level, id=pk)
	level_data.delete()

	return redirect('course:level_list')


########### WORD VIEW ############
def word_list(request):
	page_title = _('Select word to change')
	course_id = request.POST.get('course')
	list_word =   Word.objects.all()
	get_level = Level.objects.all()

	context = {
		'title': page_title,
		'list_word': list_word,
		'get_level': get_level,
	}

	return render(request,'course/word_list.html', context)


def word_detail(request, pk):
	page_title = _('Change Word')
	form = CourseForm()
	word = get_object_or_404(Word, id=pk)

	if request.method == 'POST':
		form = CourseForm(request.POST or None, instance=request.user)

		if form.is_valid():
			word = form.save(commit=False)
			word.full_name = form.cleaned_data['full_name']
			word.email = form.cleaned_data['email']
			word.ic_number = form.cleaned_data['ic_number']
			word.save()

			messages.success(request, _('Your word has been change successfully.'))
			return redirect('course:word_list')
		else:
			messages.warning(request, form.errors)

	else:
		form = CourseForm()

	context = {
		'title': page_title,
		'form': form,
		'word': word,
	}

	return render(request, 'course/word_detail.html', context)


def word_add(request):
	page_title = _('Change Course')
	# word = get_object_or_404(Course, id=pk)
	word = Word.objects.all()

	form = CourseForm()

	if request.method == 'POST':
		form = CourseForm(request.POST or None, instance=request.user)

		if form.is_valid():
			word = form.save(commit=False)
			word.full_name = form.cleaned_data['full_name']
			word.email = form.cleaned_data['email']
			word.ic_number = form.cleaned_data['ic_number']
			word.save()

			messages.success(request, _('Your word has been change successfully.'))
			return redirect('course:word_list')
		else:
			messages.warning(request, form.errors)

	else:
		form = CourseForm()

	context = {
		'title': page_title,
		'form': form,
		'word': word,
	}

	return render(request, 'course/word_add.html', context)


def word_delete(request, pk):
	word_data = get_object_or_404(Word, id=pk)
	word_data.delete()

	return redirect('course:word_list')


def word_export(request):
	word_resource = WordResource()
	dataset = word_resource.export()
	response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
	response['Content-Disposition'] = 'attachment; filename="words.xls"'
	return response


def word_import(request):
	page_title = _('Select word to import')

	if request.method == 'POST':
		word_resource = WordResource()
		dataset = Dataset()
		new_words = request.FILES['myfile']

		imported_data = dataset.load(new_words.read())
		result = word_resource.import_data(dataset, dry_run=True)  # Test the data import

		if not result.has_errors():
			word_resource.import_data(dataset, dry_run=False)  # Actually import now

			context = {
				'title': page_title,
			}

		return render(request, 'course/word_import.html', context)



	else:
		context = {
			'title': page_title,
		}

		return render(request, 'course/word_import.html', context)


