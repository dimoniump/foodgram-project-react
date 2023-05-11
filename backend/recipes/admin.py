from django.contrib import admin
from .models import Recipe, Tag, Ingredient, RecipeIngredient
# Register your models here.


admin.site.register(Tag)
admin.site.register(RecipeIngredient)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags', 'ingredients']
    inlines = (RecipeIngredientInline, )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline, )
