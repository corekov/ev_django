from django.db import models

class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class City(models.Model):
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Make(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.make} {self.name}"


class EVType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class CAFVEligibility(models.Model):
    status = models.CharField(max_length=128)

    def __str__(self):
        return self.status


class Vehicle(models.Model):
    vin_prefix = models.CharField(max_length=17, primary_key=True)
    model_year = models.IntegerField()
    electric_range = models.IntegerField()
    legislative_district = models.IntegerField()

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    ev_type = models.ForeignKey(EVType, on_delete=models.CASCADE)
    cafv = models.ForeignKey(CAFVEligibility, on_delete=models.CASCADE)
