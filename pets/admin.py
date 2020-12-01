from django.contrib import admin
from pets.models import Like, Pet


class LikeInlineAdmin(admin.TabularInline):
    model = Like


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'name')
    inlines = [
        LikeInlineAdmin,
    ]


admin.site.register(Like)
