from django.db import models
from django.db.models import PositiveIntegerField
from django.utils.text import slugify


class Module(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # генеруємо slug лише якщо він порожній
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Module.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    order = PositiveIntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='topics')

    class Meta:
        ordering = ('order',)
        unique_together = (('module', 'slug'),)

    def __str__(self):
        return self.title
