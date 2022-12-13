from django.shortcuts import render
from .models import Quote

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def quotes_index(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', { "quotes": quotes })

def quotes_detail(request, goal_id):
  quote = Quote.objects.get(id=goal_id)
  return render(request, 'quotes/detail.html', { 'quote': quote})