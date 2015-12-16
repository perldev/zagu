from django.contrib import admin

from main.models import Audio, Articles, Banner, Production, PresentPartn, Projects, Category, Banners, ProjectsImages
from main.models import Pictures, CustomMeta, ProductionMenuItem, ProductionMenu, PresentetionImages, Images
from main.models import ProductionElecticSimple, Brands, ProductionSimpleCatalog, ImagesSimple


class ProductionMenuItemInline(admin.TabularInline):
    model = ProductionMenuItem
    extra = 10


class AdminProductionMenu(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ProductionMenuItemInline]


class ProductionSimpleCatalogAdmin(admin.ModelAdmin):
    list_display = ['archive', 'brand', 'pub_date', 'status']


class PresentPartnImagesInline(admin.TabularInline):
    model = PresentetionImages
    extra = 10


class AdminPresentPartn(admin.ModelAdmin):
    list_display = ['title']
    inlines = [PresentPartnImagesInline]


class AdminPictures(admin.ModelAdmin):
    list_display = ['title', 'url']


class AdminBanners(admin.ModelAdmin):
    list_display = ['title']

    def save_model(self, request, obj, form, change):
        obj.save()
        obj.save_small(920, 400)  ##to settings ?


class ProjectsImagesInline(admin.TabularInline):
    model = ProjectsImages
    extra = 10


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 10


class ElectricImagesInline(admin.TabularInline):
    model = ImagesSimple
    extra = 10


class AdminProductionElecticSimple(admin.ModelAdmin):
    list_display = ['title', 'text', 'price']
    inlines = [ElectricImagesInline]


class AdminProduction(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ImagesInline]


class AdminProjects(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ProjectsImagesInline]


admin.site.register(PresentPartn, AdminPresentPartn)
admin.site.register(ProductionSimpleCatalog, ProductionSimpleCatalogAdmin)
admin.site.register(Banners, AdminBanners)
admin.site.register(Banner)
admin.site.register(Pictures, AdminPictures)
admin.site.register(CustomMeta)
admin.site.register(Articles)
admin.site.register(Category)
admin.site.register(Audio)
admin.site.register(Brands)

admin.site.register(Projects, AdminProjects)
admin.site.register(Production, AdminProduction)
admin.site.register(ProductionMenu, AdminProductionMenu)
admin.site.register(ProductionElecticSimple, AdminProductionElecticSimple)
