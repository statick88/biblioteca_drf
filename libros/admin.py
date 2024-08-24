from django.contrib import admin
from .models import Libro
from .models import Autor

admin.site.register(Libro)
admin.site.register(Autor)