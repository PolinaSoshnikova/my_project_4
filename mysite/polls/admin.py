from django.contrib import admin
from .models import Feedback
from .models import Product
from .models import Item

admin.site.register(Feedback)
# Register your models here.
admin.site.register(Item)
admin.site.register(Product)
