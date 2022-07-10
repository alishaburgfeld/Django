from xml.dom import ValidationErr
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def not_blank(name):
    if len(name)<1:
        raise ValidationErr('This field cannot be blank.')

def true_or_false(relay):
    if relay == None:
        raise ValidationErr("'None' value must be either True or False.")

def validate_stroke(stroke):
    valid_strokes=['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in valid_strokes:
        raise ValidationErr(_('%(stroke) is not a valid stroke'), params={'stroke':stroke},)

def validate_distance(distance):
    if distance < 50:
        raise ValidationErr("Ensure this value is greater than or equal to 50.")

def validate_date(date):
    if date > timezone.now():
        raise ValidationErr("Can't set record in the future.")

def validate_broken_date(record_date, record_broken_date):
    # super().clean
    if record_broken_date < record_date:
        raise ValidationErr("Can't break record before record was set.")

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255, validators=[not_blank])
    last_name = models.CharField(max_length=255, validators=[not_blank])
    team_name = models.CharField(max_length=255, validators=[not_blank])
    relay = models.BooleanField(validators=[true_or_false])
    stroke = models.CharField(max_length=11, validators=[validate_stroke])
    distance = models.IntegerField(validators=[validate_distance])
    record_date = models.DateTimeField(validators=[validate_broken_date])
    record_broken_date = models.DateTimeField(validators=[validate_broken_date])
