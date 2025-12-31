from django.contrib import admin
from quizzes.tasks import parse_test_file
from quizzes.models import Test, Question, Answer

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'topic',
        'import_status',
        'is_active',
        'created_at',
    )
    list_filter = ('import_status', 'is_active', 'topic')
    search_fields = ('title',)
    readonly_fields = ('import_status', 'created_at', 'updated_at')

    fieldsets = (
        (None, {
            'fields': ('topic', 'title', 'description', 'is_active')
        }),
        ('Import', {
            'fields': ('source_file', 'import_status')
        }),
        ('Meta', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    actions = ['parse_file']

    def parse_file(self, request, queryset):
        for test in queryset.filter(import_status='pending'):
            parse_test_file.delay(test.id)

    parse_file.short_description = "Parse selected test files"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


        if obj.source_file and obj.import_status == 'pending':
            parse_test_file.delay(obj.id)
