from django.forms import ModelForm, ModelChoiceField
from .models import TruckTrip


class TruckTripForm(ModelForm):
    class Meta:
        model = TruckTrip
        fields = ['truck_model']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['truck_model'].label = "Модель"
        self.fields['truck_model'].empty_label = None


