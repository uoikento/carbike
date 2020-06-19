from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PhotoForm
from .models import Photo

def index(request):
  template = loader.get_template('carbike/index.html')
  context = {'form':PhotoForm()}
  return HttpResponse(template.render(context, request))

def predict(request):
  if not request.method == 'POST':
    return
    redirect('carbike:index')

  form = PhotoForm(request.POST, request.FILES)
  if not form.is_valid():
    raise ValueError('Formが不正です')

  photo = Photo(image=form.cleaned_data['image'])
  predict, percentage = photo.predict()

  return HttpResponse("")