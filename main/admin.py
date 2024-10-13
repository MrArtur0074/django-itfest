from django.contrib import admin
from .models import SiteSettings
from .models import Direction

class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Проверяем, есть ли уже объект SiteSettings
        count = SiteSettings.objects.all().count()
        if count >= 1:
            return False  # Запрещаем добавление нового объекта
        return True

admin.site.register(SiteSettings, SiteSettingsAdmin)

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')