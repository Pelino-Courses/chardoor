from django.contrib import admin
from .models import Customers, addUpComing, movies, addMessage, Profile

admin.site.register([Customers,addUpComing,movies,addMessage,Profile])