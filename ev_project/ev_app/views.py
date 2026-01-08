from django.shortcuts import render
from django.db.models import Avg

from .models import State, City, Vehicle, County, Model, Make, EVType, CAFVEligibility


def index(request):
    states = State.objects.all()[:20].values_list('id', 'name')
    countries = County.objects.all()[:20].values_list('id', 'state_id', 'name')
    cities = City.objects.all()[:20].values_list('id','county_id', 'name', 'postal_code')
    vehicles = Vehicle.objects.all()[:20].values_list(
        'vin_prefix', 'model_year', 'electric_range', 'legislative_district', 'city_id', 
        'model_id', 'ev_type_id', 'cafv_id'
    )
    models = Model.objects.all()[:20].values_list('id','make_id','name')
    makers = Make.objects.all()[:20].values_list('id', 'name')
    ev_types = EVType.objects.all()[:20].values_list('id', 'name')
    CAFV_Eligibilitys = CAFVEligibility.objects.all()[:20].values_list('id', 'status')

    context = {
        'states': states,
        'countries': countries,
        'cities': cities,
        'vehicles': vehicles,
        'models': models,
        'makers':makers,
        'ev_types': ev_types,
        'CAFV_Eligibilitys': CAFV_Eligibilitys,
        'vehicle_count': Vehicle.objects.count(),
        'avg_range': Vehicle.objects.aggregate(
            Avg('electric_range')
        )['electric_range__avg'],
    }

    return render(request, 'index.jinja', context, using='jinja2')
