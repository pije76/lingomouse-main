from django import forms
from django.forms.models import BaseInlineFormSet
from django.utils.translation import gettext_lazy as _

import pycountry

from config.models import *

from .models import *


get_language = Language.objects.all().values_list("code", flat=True)
get_language = list(get_language)

obj = []

for item in get_language:
    # language = pycountry.languages.lookup(item)
    language = pycountry.languages.get(alpha_2=item)
    language = language.name
    if language and language not in obj:
        obj.append(language)

LANG_CHOICES = [(item.alpha_2, item.name) for item in pycountry.languages if hasattr(item, 'alpha_2')]

for item in get_language:
	LANG_CHOICES.append(item)
# LANG_CHOICES = [(language.alpha_2) for language in pycountry.languages]

# LANG_CHOICES = [(language.name)
#             for language in pycountry.languages]

# language_list = [item.alpha_3 for item in pycountry.countries]
# language_tuples = ((item, item) for item in language_list)

# for item in get_language:
# 	get_language.alpha_2
	# LANGUAGE_CHOICES = Language.objects.filter(code=item)

# list3 = set(obj) & set(LANG_CHOICES)
list3 = set(obj).intersection(set(LANG_CHOICES))
list3 = list(list3)

class CountryForm(forms.Form):
	# for item in get_language:
	# 	obj = pycountry.languages.get(alpha_2=item).name

	# languages.append(obj)
	# print(languages)


	id = forms.CharField(label=_(u''), required=True, max_length=200, widget=forms.TextInput(attrs={'class': "vTextField"}))
	name = forms.CharField(label=_(u''), required=True, max_length=200, widget=forms.TextInput(attrs={'class': "vTextField"}))
	description = forms.CharField(label=_(u''), required=False, max_length=1000, widget=forms.Textarea(attrs={'class': "vLargeTextField", 'cols': 40, 'rows': 10}))
	# native = forms.ChoiceField(label=_(u''), required=False, widget=forms.Select, choices=((x.id, x.name) for x in get_language))
	# native = forms.ChoiceField(label=_(u''), required=False, widget=forms.Select, choices=[(k, v) for k, v in COUNTRIES.items()])
	# native = forms.ChoiceField(choices=[(k, v) for k, v in get_language()],widget=Select2MultipleWidget)
	native = forms.ChoiceField(label=_(u''), required=False, choices=(LANG_CHOICES), widget=forms.Select)
	foreign = forms.ChoiceField(label=_(u''), required=False, choices=(get_language), widget=forms.Select)
	img = forms.ImageField(label=_(u''), required=False)
	is_active = forms.BooleanField(label=_(u'Is active?'), required=False, widget=forms.CheckboxInput(attrs={'checked': "checked"}))


class CountryModelForm(forms.ModelForm):
	class Meta:
		model = Country
		fields = '__all__'
		widgets = {
			# 'native': forms.HiddenInput(),
			# "native" : forms.ChoiceField(attrs={"class" : "form-control"}),
		}
		labels = {
            "id": _(""),
            "name": _(""),
            "native": _(""),
            "foreign": _(""),
            "description": _(""),
            "img": _(""),
            # "is_active": _(""),
        }

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.fields['id'].widget.attrs.update({'class': 'form-control'})
		# self.fields['name'].widget.attrs.update({'class': 'form-control'})
		# self.fields['description'].widget.attrs.update({'class': 'form-control text-area'})
		# self.fields['native'].widget.attrs.update({'class': 'form-control text-area'})

	'''Account form'''
	# id = forms.CharField(label=_(u''), required=True, max_length=200, widget=forms.TextInput(attrs={'class': "vTextField"}))
	# name = forms.CharField(label=_(u''), required=True, max_length=200, widget=forms.TextInput(attrs={'class': "vTextField"}))
	description = forms.CharField(label=_(u''), required=False, max_length=1000, widget=forms.Textarea(attrs={'class': "vLargeTextField", 'cols': 40, 'rows': 10}))
	# native = forms.ChoiceField(label=_(u''), required=False, widget=forms.Select)
	# is_active = forms.ChoiceField(label=_(u''), required=False, widget=forms.Select)


# Word Media Form
# class WordMediaForm(forms.ModelForm):
# 	""" If field type is field then add recorder to """
# 	media_type = forms.ChoiceField(choices=MEDIA_TYPE)
# 	path_to_file = forms.FileField(widget=MediaFileInput)


class LanguageChangeListForm(forms.ModelForm):
	""" Filter level by own course """
	def __init__(self, *args, **kwargs):
		super(LanguageChangeListForm, self).__init__(*args, **kwargs)

		if self.instance:
			_level_queryset = Level.objects.filter(course_id=self.instance.course.id)

			self.fields['level'].queryset = _level_queryset
			self.fields['level'].choices = [(level.id, level.name) for level in _level_queryset]


class LanguageForm(forms.Form):
	def __init__(self, *args, **kwargs):
	# def __init__(self, *args, parent_object, **kwargs):
		# self.parent_object = parent_object
		super(LanguageForm, self).__init__(*args, **kwargs)


class LanguageInlineForm(BaseInlineFormSet):
	""" Filter level by own course """
	def __init__(self, *args, **kwargs) -> None:
		super(LanguageInlineForm, self).__init__(*args, **kwargs)

		if self.instance:
			_level_queryset = Level.objects.filter(course_id=self.instance.id)

			for form in self.forms:
				form.fields['level'].queryset = _level_queryset
				form.fields['level'].choices = [(level.id, level.name) for level in _level_queryset]

	def get_form_kwargs(self, index):
		kwargs = super().get_form_kwargs(index)
		kwargs['parent_object'] = self.instance
		return kwargs