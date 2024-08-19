from django.contrib import admin
from rank.models import Category1, Category2, RankData


class Category1Admin(admin.ModelAdmin):
    list_display = ('category1',)
    list_filter = ['category1']
    search_fields = ['category1']


admin.site.register(Category1, Category1Admin)


class Category2Admin(admin.ModelAdmin):
    list_display = ('category1', 'category2')
    list_filter = ['category1', 'category2']
    search_fields = ['category1', 'category2']


admin.site.register(Category2, Category2Admin)


class RankDataAdmin(admin.ModelAdmin):
    list_display = ('category1', 'category2')
    list_filter = ['category1', 'category2']
    search_fields = ['category1', 'category2']


admin.site.register(RankData, RankDataAdmin)

