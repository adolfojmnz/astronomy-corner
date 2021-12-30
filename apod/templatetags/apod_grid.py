from django import template

register = template.Library()


@register.simple_tag
def apod_grid(apod_list):
	for apod in apod_list:
		pass
