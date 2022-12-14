from django.shortcuts import render, redirect
from .models import Quote
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .forms import DiscussionForm

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
  discussion_form = DiscussionForm()
  return render(request, 'quotes/detail.html', { 
    'quote': quote, 
    'discussion_form': discussion_form 
  })

def add_discussion(request, quote_id):
  form = DiscussionForm(request.POST)
  if form.is_valid():
    new_discussion = form.save(commit=False) # Take this from a django form object and turn it into an database object, but it wont save 
    new_discussion.quote_id = quote_id
    print(new_discussion)
    new_discussion.save()
  return redirect('detail', quote_id=quote_id)