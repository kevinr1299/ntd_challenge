from django.contrib import admin

from planets.models import Planet


@admin.register(Planet)
class PlanteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "population",
        "terrains",
        "climates",
    )
    list_filter = ("name",)
