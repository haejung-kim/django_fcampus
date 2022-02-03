from django.contrib import admin
from .models import Fcuser


class FcuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    # pass


admin.site.register(Fcuser, FcuserAdmin)

# Register your models here.
