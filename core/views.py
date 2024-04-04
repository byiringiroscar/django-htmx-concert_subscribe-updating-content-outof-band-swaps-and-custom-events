from django.shortcuts import render, get_object_or_404
from core.models import Event

# Create your views here.
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    print('-----------', event)
    context = {
        'event': event
    }
    return render(request, 'core/subscribe.html', context)