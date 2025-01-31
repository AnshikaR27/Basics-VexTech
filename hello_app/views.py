from django.shortcuts import render, HttpResponse
from .models import HomepageContent

# Create your views here.
def hello(request):
    content = HomepageContent.objects.last()
    return render(request, 'hello_app/home.html', {'content': content})