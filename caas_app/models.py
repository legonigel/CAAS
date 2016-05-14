from __future__ import unicode_literals

from django.db import models
from colorful.fields import RGBColorField

# Create your models here.

class Led_State(models.Model):
    RAINBOW = 'R'
    RAINBOW_CYCLE = 'RC'
    CHASE = 'C'
    CHASE_RAINBOW = 'CR'
    COLOR_WIPE = 'W'
    SOLID_COLOR = 'S'
    CNU = 'CNU'

    MODE_CHOICES = (
	(RAINBOW, 'Rainbow'),
	(RAINBOW_CYCLE, 'Rainbow Cycle'),
	(CHASE, 'Chase'),
	(CHASE_RAINBOW, 'Chase Rainbow'),
	(COLOR_WIPE, 'Color Wipe'),
	(SOLID_COLOR, 'Solid Color'),
	(CNU, 'CNU'),
    )

    #Modes with a color option
    COLOR_MODES = [CHASE, COLOR_WIPE, SOLID_COLOR]

    mode = models.CharField(max_length = 10,
			    choices = MODE_CHOICES,
			    default = SOLID_COLOR)
    color = RGBColorField()
