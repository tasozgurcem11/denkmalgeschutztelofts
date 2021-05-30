from django.contrib import admin
from .models import Email, Kontakt
# Register your models here.


class UserInfo(admin.ModelAdmin):

    list_display = ("email", "created_at")

class KontaktInfo(admin.ModelAdmin):

    list_display = ("vorname", "nachname", "email", "quelle","created_at")


admin.site.register(Email, UserInfo)
admin.site.register(Kontakt, KontaktInfo)

