from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
from Work.models import *
# Create your views here.

def index(request):
	main = Main.objects.order_by("pk").filter(is_published=True).last()
	sections_list = Section.objects.filter(is_published=True)
	services_list = Services.objects.filter(is_published=True)
	years_list = Years.objects.order_by("-year").filter(is_published=True)
	skills_list = Skills.objects.filter(is_published=True)
	socials_list = Social.objects.filter(is_published=True)

	works_list = Work.objects.filter(is_published=True)
	paginator = Paginator(works_list, 5)
	page_number = request.GET.get('page', 1)
	works = paginator.page(page_number)
	
	context = {
		"main": main,
		"sections_list": sections_list,
		'sections': {section.slug: section for section in sections_list}, # секцій багато, вони розкидані, так можна звертатись по назві
		"services_list": services_list,
		"years_list": years_list,
		"skills_list": skills_list,
		"socials_list": socials_list,
		"works": works,
	}
	return render(request, 'index.html', context)