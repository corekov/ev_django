import csv
from django.core.management.base import BaseCommand
from ev_app.models import (
    State,
    County,
    City,
    Make,
    Model,
    EVType,
    CAFVEligibility,
    Vehicle,
)


class Command(BaseCommand):
    help = "Load Electric Vehicle data from CSV file"

    def handle(self, *args, **kwargs):
        with open('Electric_Vehicle_Population_Data.csv', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            for row in reader:
                state, _ = State.objects.get_or_create(
                    name=row['state']
                )

                county, _ = County.objects.get_or_create(
                    name=row['county'],
                    state=state
                )

                city, _ = City.objects.get_or_create(
                    name=row['city'],
                    county=county,
                    postal_code=row['postal_code']
                )

                make, _ = Make.objects.get_or_create(
                    name=row['make']
                )

                model, _ = Model.objects.get_or_create(
                    name=row['model'],
                    make=make
                )

                ev_type, _ = EVType.objects.get_or_create(
                    name=row['electric_vehicle_type']
                )

                cafv, _ = CAFVEligibility.objects.get_or_create(
                    status=row['cafv_eligibility']
                )

                vin=row['vin_prefix']

                if not Vehicle.objects.filter(vin_prefix=vin).exists():
                    Vehicle.objects.create(
                        vin_prefix=vin,
                        model_year=int(row['model_year']) if row['model_year'] else None,
                        electric_range=int(row['electric_range']) if row['electric_range'] else 0,
                        legislative_district=int(row['legislative_district']) if row['legislative_district'] else 0,
                        city=city,
                        model=model,
                        ev_type=ev_type,
                        cafv=cafv
                    )
        self.stdout.write(
            self.style.SUCCESS('Данные успешно загружены')
        )
