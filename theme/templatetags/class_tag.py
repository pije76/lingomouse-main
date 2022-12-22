from django import template

from itertools import chain

from config.models import *
from course.models import *

register = template.Library()

@register.simple_tag
def app_list():

	course_course = Course.objects.all()
	course_level = Level.objects.all()
	course_word = Word.objects.all()

	course_list = config_country | config_language

	config_country = Country.objects.all()
	config_language = Language.objects.all()

	config_list = config_country | config_language

	# app_list = course_list | config_list

	app_list = chain(course_course, course_level, course_word, config_country, config_language)

	return app_list


@register.filter
# @register.filter(name='get_class')
def get_class(value):
    return value.__class__.__name__
    # return value._meta.model.__name__