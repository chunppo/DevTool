from django.contrib import admin
from .models import ServerGroup
from .models import ServiceServer

admin.site.register(ServerGroup)
admin.site.register(ServiceServer)
