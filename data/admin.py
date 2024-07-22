from django.contrib import admin
from .models import Car
from .models import Country
from .models import Parts

admin.site.register(Car)
admin.site.register(Country)
admin.site.register(Parts)
# Register your models here.
