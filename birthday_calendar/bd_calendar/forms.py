from django import forms
from bd_calendar.models import ImportantDate
class DateForm(forms.Form):
    event_date = forms.DateField(widget=forms.SelectDateWidget)
    name = forms.CharField(max_length=255)
    reminder_for = forms.CharField(max_length=20)
