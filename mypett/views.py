from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, "mypett/index.html")


def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by("date_added")
    context = {'topic': topic}
    return render(request, "mypett/topic.html",context)
