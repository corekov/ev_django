from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg

from .models import (
    State,
    County,
    City,
    Vehicle,
    Model,
    Make,
    EVType,
    CAFVEligibility
)

from .forms import CountyForm

def home(request):
    return render(request, 'home.jinja', using='jinja2')


def index(request):
    states = State.objects.all().values_list('id', 'name')
    counties = County.objects.all().values_list('id', 'state_id', 'name')
    cities = City.objects.all().values_list(
        'id', 'county_id', 'name', 'postal_code'
    )
    vehicles = Vehicle.objects.all().values_list(
        'vin_prefix',
        'model_year',
        'electric_range',
        'legislative_district',
        'city_id',
        'model_id',
        'ev_type_id',
        'cafv_id'
    )
    models = Model.objects.all().values_list('id', 'make_id', 'name')
    makers = Make.objects.all().values_list('id', 'name')
    ev_types = EVType.objects.all().values_list('id', 'name')
    cafv_eligibilities = CAFVEligibility.objects.all().values_list('id', 'status')

    context = {
        'states': states,
        'countries': counties,
        'cities': cities,
        'vehicles': vehicles,
        'models': models,
        'makers': makers,
        'ev_types': ev_types,
        'CAFV_Eligibilitys': cafv_eligibilities,
        'vehicle_count': Vehicle.objects.count(),
        'avg_range': Vehicle.objects.aggregate(
            Avg('electric_range')
        )['electric_range__avg'],
    }

    return render(request, 'index.jinja', context, using='jinja2')

def county_list(request):
    counties = County.objects.select_related('state').all()
    return render(
        request,
        'county_list.jinja',
        {'counties': counties},
        using='jinja2'
    )

def county_create(request):
    if request.method == 'POST':
        form = CountyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('county_list')
    else:
        form = CountyForm()

    return render(
        request,
        'county_form.jinja',
        {
            'form': form,
            'title': 'Добавить округ'
        },
        using='jinja2'
    )


def county_update(request, pk):
    county = get_object_or_404(County, pk=pk)

    if request.method == 'POST':
        form = CountyForm(request.POST, instance=county)
        if form.is_valid():
            form.save()
            return redirect('county_list')
    else:
        form = CountyForm(instance=county)

    return render(
        request,
        'county_form.jinja',
        {
            'form': form,
            'title': 'Редактировать округ'
        },
        using='jinja2'
    )

def county_delete(request, pk):
    county = get_object_or_404(County, pk=pk)

    if request.method == 'POST':
        county.delete()
        return redirect('county_list')

    return render(
        request,
        'county_delete.jinja',
        {'county': county},
        using='jinja2'
    )
