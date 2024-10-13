from django.db import models
from django.core.exceptions import ValidationError

# Общие настройки сайта
class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    banner_image = models.ImageField(upload_to='banners/', blank=True, null=True)
    header_title = models.CharField(max_length=255, blank=True, null=True)
    header_description = models.TextField(blank=True, null=True)

    telegram_link = models.URLField(max_length=255, blank=True, null=True)
    telegram_icon = models.ImageField(upload_to='icons/', blank=True, null=True)

    instagram_link = models.URLField(max_length=255, blank=True, null=True)
    instagram_icon = models.ImageField(upload_to='icons/', blank=True, null=True)

    whatsapp_link = models.URLField(max_length=255, blank=True, null=True)
    whatsapp_icon = models.ImageField(upload_to='icons/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError("You can only create one instance of SiteSettings.")
        return super(SiteSettings, self).save(*args, **kwargs)

    def __str__(self):
        return "Site Settings"


# Таблица направлений
class Direction(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='directions/', verbose_name='Изображение')
    url = models.URLField(verbose_name='Ссылка на направление', max_length=255)

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.title