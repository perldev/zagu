from main.models import Audio, Articles, Banner, Production, AdminProduction,PresentPartn, AdminPresentPartn,  Projects, AdminProjects, Category, Banners,AdminBanners
from main.models import Pictures, CustomMeta

from main.models import ProductionMenuItem, ProductionMenu, AdminProductionMenu, AdminPictures

from main.models import  ProductionElecticSimple, AdminProductionElecticSimple, Brands
from main.models import ProductionSimpleCatalog, ProductionSimpleCatalogAdmin
from django.contrib import admin


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


