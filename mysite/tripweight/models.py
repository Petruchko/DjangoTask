from django.db import models


class TruckModel(models.Model):
    name = models.CharField('Модель самосвала', max_length=200, default='', null=True)
    capacity = models.IntegerField('Максимальная грузоподъемность', default=0, null=True)

    def __str__(self):
        return self.name


class Truck(models.Model):
    name = models.CharField('Название самосвала', max_length=200, default='', null=True)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE, default='', null=True)

    def __str__(self):
        return self.name


class TruckTrip(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, default='', null=True)
    truck_model = models.ForeignKey(TruckModel, db_column='Модель', on_delete=models.CASCADE, default='', null=True)
    weight = models.IntegerField('Текущий вес', default=0)

    def calculate_overweight(self):
        if self.weight > self.truck_model.capacity:
            return round((self.weight - self.truck_model.capacity) / self.truck_model.capacity * 100, 2)
        else:
            return 0

    def __str__(self):
        return self.truck.name + ": " + self.truck_model.name
