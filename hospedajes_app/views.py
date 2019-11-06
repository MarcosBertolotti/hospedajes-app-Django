from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from hospedaje.settings import MEDIA_ROOT
from hospedajes_app.forms import PostForm
from hospedajes_app.models import Property, City


def index(request):
    properties = Property.objects.all()
    return render(request, 'hospedajes_app/index.html', {'properties': properties})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })


def property_form(request):
    error = ''
    cities = City.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        pax = request.POST['pax']
        daily_import = request.POST['daily']
        image = request.FILES['propertyImage']
        fk_city = request.POST['city']
        # fk_user = request.POST['fk_user']

        city = City.objects.get(id=fk_city)

        if title is not None:
            property = Property(title=title, pax=pax, description=description, daily_import=daily_import, city=city,
                                image=image, )
            property.save()
        else:
            error = 'La propiedad debe tener nombre'

    return render(request, 'hospedajes_app/forms/property_form.html', {'error': error, 'cities': cities})


def save_file(file, path=''):
    """ Little helper to save a file """
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()


def city_form(request):
    error = ''
    cities = City.objects.all()

    if request.method == 'POST':
        name = request.POST['name']

        if name is not None:
            city = City(name=name)
            city.save()
        else:
            error = 'La ciudad debe tener nombre'

    return render(request, 'hospedajes_app/forms/city_form.html', {'cities': cities, 'error': error})


def view_property(request, property_id):
    property = Property.objects.get(id=property_id)
    return render_to_response('hospedajes_app/view_property.html', {'property': property})



















def post_list(request):
    return render(request, 'hospedajes_app/post_list.html', {})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            property = form.save(commit=False)
            property.title = request.title
            property.description = request.description
            property.pax = request.pax
            property.daily_import = request.daily_import
            property.image = request.image
            property.fk_city = request.fk_city
            property.fk_user = request.fk_user
            property.save()
            return redirect('post_detail', pk=property.pk)
    else:
        form = PostForm()
    return render(request, 'hospedajes_app/post_edit.html', {'form': form})


def post_edit(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=property)
        if form.is_valid():
            property = form.save(commit=False)
            property.author = request.user
            property.published_date = timezone.now()
            property.save()
            return redirect('post_detail', pk=property.pk)
    else:
        form = PostForm(instance=property)
    return render(request, 'hospedajes_app/post_edit.html', {'form': form})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
