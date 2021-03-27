from django.contrib import admin
from .models import Ad, Fav


class AdAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register the admin class with the associated model
admin.site.register(Ad, AdAdmin)
admin.site.register(Fav)
