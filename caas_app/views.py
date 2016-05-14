from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from colorful.widgets import ColorFieldWidget

# Create your views here.

from .models import Led_State

def main(request):
    state = get_object_or_404(Led_State, pk = 1)
    if request.method == "POST" and 'choice' in request.POST and 'color' in request.POST:
	state.mode = request.POST['choice']
	if request.POST['color']:
	    state.color = request.POST['color']
	state.save()
    selected_mode = state.mode
    return render(request, 'caas_app/main.html',
		  {'state': state,
		   'selected_mode': selected_mode,
		   'color_html': ColorFieldWidget().render('color', state.color)})

def state(request):
    state = get_object_or_404(Led_State, pk = 1)
    response_data = {}
    response_data['mode'] = state.mode
    response_data['color'] = state.color
    return JsonResponse(response_data)
