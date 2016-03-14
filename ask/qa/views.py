from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

def test(request, *args, **kwargs):
	return HttpResponse('OK')

@require_GET
def question_info(request,q_id):
	question = get_odject_or_404(Question, q_id=q_id)
	return render(request, 'question_info.html', {
	'question': question,
	})

