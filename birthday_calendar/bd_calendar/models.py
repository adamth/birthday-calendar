from django.db import models

# Create your models here.
class ImportantDate(models.Model):
    BIRTHDAY = 'Birthday'
    ANNIVERSARY = 'Anniversary'
    OTHER = 'Other'
    reminder_types = (
        (BIRTHDAY, BIRTHDAY),
        (ANNIVERSARY, ANNIVERSARY),
        (OTHER, OTHER)
    )

    event_date = models.DateField()
    name = models.CharField(max_length=255)
    reminder_for = models.CharField(default=BIRTHDAY, choices=reminder_types, max_length=20)

    def __str__(self):
        return f'{self.name}\'s {self.reminder_for} on {self.event_date}'

class Reminder(models.Model):
    important_date = models.ForeignKey('bd_calendar.ImportantDate', models.CASCADE)
    date_generated = models.DateField(auto_now=True)
    acknowledged = models.BooleanField(default=False)
    monthly_email_sent = models.BooleanField(default=False)
    weekly_email_sent = models.BooleanField(default=False)
    daily_email_sent = models.BooleanField(default=False)
