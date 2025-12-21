from django.db import models
from django.db.models import PositiveIntegerField, Max
from django.utils.text import slugify


class SlugMixin(models.Model):
    slug = models.SlugField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def generate_slug(self, source_field: str, scope_field=None):
        """
        Генерує унікальний slug на основі source_field.
        Якщо scope_field заданий, перевірка унікальності обмежується його значенням.
        """
        base_slug = slugify(getattr(self, source_field))
        slug = base_slug
        counter = 1

        ModelClass = self.__class__
        filter_kwargs = {}
        if scope_field:
            filter_kwargs[scope_field] = getattr(self, scope_field)

        while ModelClass.objects.filter(slug=slug, **filter_kwargs).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        return slug

    def save(self, *args, **kwargs):
        if not self.slug:
            # scope_field=None для глобального slug, або 'module' для локального
            scope = 'module' if hasattr(self, 'module') else None
            self.slug = self.generate_slug('title', scope_field=scope)
        super().save(*args, **kwargs)

    def __str__(self):
        return getattr(self, 'title', self.slug)


class Module(SlugMixin, models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Topic(SlugMixin, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    order = PositiveIntegerField(blank=True, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='topics')

    class Meta:
        ordering = ('order',)
        unique_together = (('module', 'slug'),)

    def save(self, *args, **kwargs):
        # Автоматичне присвоєння порядку, якщо не задано
        if self.order is None:
            last_order = Topic.objects.filter(module=self.module).aggregate(Max('order'))['order__max'] or 0
            self.order = last_order + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
