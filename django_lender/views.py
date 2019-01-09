from django.shortcuts import render

def home(request):
    """Render the home route."""
    return render(request, 'generic/home.html', {'message': 'Hello World'})
