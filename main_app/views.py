from django.shortcuts import render
from .models import Quote
from django.views.generic.edit import CreateView, UpdateView, DeleteView 

class QuoteCreate(CreateView):
    model = Quote
    fields = '__all__'

class QuoteUpdate(UpdateView):
    model = Quote
    fields = '__all__'

class QuoteDelete(DeleteView):
    model = Quote
    success_url = '/quotes/'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def quotes_index(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', { "quotes": quotes })

def quotes_detail(request, quote_id):
  quote = Quote.objects.get(id=quote_id)
  return render(request, 'quotes/detail.html', { 'quote': quote})