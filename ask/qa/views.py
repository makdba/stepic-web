from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from qa.models import *

def test(request, *args, **kwargs):
	return HttpResponse('OK')

@require_GET
def question_info(request,q_id):
	question = get_odject_or_404(Question, q_id=q_id)
	return render(request, 'question_info.html', {
	'question': question,
	})

def paginate (request, qs):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10

	try:
		page = int(request.GET.get('page', 1))
	except ValueErrir:
		page = 1


	paginator = Paginator(qs, limit)
	try:
		page= paginator.page(page)
	except EmptyPage:
		page= paginator.page(paginator.num_pages)

	return page



@require_GET
def questions(request):
	page = paginate(request, Question.odjects.order_by('-added_at')) 
	return render(request, 'questions.html', {
		'page':page,
		'baseurl': '/?page=',
		'webpage_title': 'New questions',
	})


def popular_questions(request):
	page = paginate(request, Question.odjects.order_by('-rating')) 
	return render(request, 'questions.html', {
		'page':page,
		'baseurl':'/popular/?page=',
		'webpage_title':'Popular questions',
	})
	
