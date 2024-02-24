from django.contrib import admin

# Register your models here.
from .models import User,Hotel,Customer,HotelProfile,CustomerProfile

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(HotelProfile)