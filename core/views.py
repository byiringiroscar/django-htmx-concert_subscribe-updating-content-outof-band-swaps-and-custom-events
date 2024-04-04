from django.shortcuts import render, get_object_or_404
from core.models import Event

# Create your views here.
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context = {
        'event': event
    }
    return render(request, 'core/subscribe.html', context)


def subscribe(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.users.add(request.user)
    context = {
        'event': event
    }
    return render(request, 'core/partials/user_li.html', context)