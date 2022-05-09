from django.contrib import admin

# Register your models here.
from .models import MasterDegrees
from .models import Modules

admin.site.register(MasterDegrees)
admin.site.register(Modules)

# Our two Database Models 