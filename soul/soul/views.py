from django.shortcuts import render

# Create your views here.
def home(request):
     context = {}
     return render(request, 'soul/index.html', context)

def discover(request):
     context = {}
     return render(request, 'soul/discover.html', context)


