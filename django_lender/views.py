from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """Render the home route."""
    return render(request, 'generic/home.html', {'message': 'Click on Books on Loan to see your list of books.'})
