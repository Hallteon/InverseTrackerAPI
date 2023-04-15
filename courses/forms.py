from django import forms 
from courses.models import Schedule


class ScheduleForm(forms.ModelForm):
    time = forms.TimeField(input_formats=['%H:%M'], label='Время проведения')

    class Meta:
        model = Schedule
        fields = '__all__'