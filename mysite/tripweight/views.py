from django.shortcuts import render
from .models import TruckTrip
from .forms import TruckTripForm


def table(request):  # Рисуем таблицу
    trips = TruckTrip.objects.all()
    form = TruckTripForm()

    if request.GET.get('truck_model'):
        truck_model = request.GET.get('truck_model')
        if truck_model == '10':  # Костыль - нужно добавить дополнительное поле в ModelForm "Все"
            trips = TruckTrip.objects.all()
        else:
            trips = trips.filter(truck_model=truck_model)
        form = TruckTripForm(request.GET)
    context = {
        'form': form,
        'trips': trips
    }
    return render(request, 'tripweight/index.html', context)