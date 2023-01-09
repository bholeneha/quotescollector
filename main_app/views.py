from django.shortcuts import render, redirect
from .models import Quote, Discussion, Tag
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic import ListView, DetailView
from .forms import DiscussionForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin 


def signup(request):
  error_message = ''
  if request.method == 'POST': # if the user submited a form 
    form = UserCreationForm(request.POST) # Making a new instance of the class, request.POST is the body of the form
    if form.is_valid(): # Validate it
      user = form.save() # If valid, save
      login(request, user)
      return redirect('index') # Redirect to indec
    else:
      print(form.errors) #not valid
      error_message = form.errors # error message
  form = UserCreationForm() #empty form 
  return render(request, 'registration/signup.html', {
    'form': form,
    'error_message': error_message
  }) # Send empty form and render for retry

class QuoteCreate(CreateView):
    model = Quote
    fields = ['quote', 'author']
  
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class QuoteUpdate(UpdateView):
    model = Quote
    fields = ['quote', 'author']

class QuoteDelete(DeleteView):
    model = Quote
    success_url = '/quotes/'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def quotes_index(request):
    quotes = Quote.objects.filter(user=request.user)
    return render(request, 'quotes/index.html', { "quotes": quotes })

@login_required
def quotes_detail(request, quote_id):
  quote = Quote.objects.get(id=quote_id)
  tags = Tag.objects.exclude(id__in = quote.tags.all().values_list('id'))
  discussion_form = DiscussionForm()
  return render(request, 'quotes/detail.html', { 
    'quote': quote, 
    'discussion_form': discussion_form,
    'tags': tags
  })

@login_required
def add_discussion(request, quote_id):
  form = DiscussionForm(request.POST)
  if form.is_valid():
    new_discussion = form.save(commit=False) # Take this from a django form object and turn it into an database object, but it wont save 
    new_discussion.quote_id = quote_id
    print(new_discussion)
    new_discussion.save()
  return redirect('detail', quote_id=quote_id)

@login_required
def add_tag(request, quote_id, tag_id):
  Quote.objects.get(id=quote_id).tags.add(tag_id)
  return redirect('detail', quote_id=quote_id)

@login_required
def remove_tag(request, quote_id, tag_id):
  Quote.objects.get(id=quote_id).tags.remove(tag_id)
  return redirect('detail', quote_id=quote_id)

class TagList(LoginRequiredMixin, ListView):
  model = Tag

class TagDetail(LoginRequiredMixin, DetailView):
  model = Tag

class TagCreate(LoginRequiredMixin, CreateView):
  model = Tag
  fields = ['name']

class TagUpdate(LoginRequiredMixin, UpdateView):
  model = Tag
  fields = ['name']

class TagDelete(LoginRequiredMixin, DeleteView):
  model = Tag
  success_url = '/tags/'