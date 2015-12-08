# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.contrib.admin  import TabularInline
from  pyzagu import settings
from PIL import Image
import os
import re

import rarfile

from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import pre_save
import os

# Create your models here.
class Articles(models.Model):
   title = models.CharField(max_length = 255)
   text = models.TextField()
   introtext = models.TextField()
   
   meta_keyword = models.CharField(max_length = 255, blank = True)
   meta_description = models.CharField(max_length = 255, blank = True)
   pub_date = models.DateTimeField('date published', auto_now = True )
   category = models.ForeignKey("Category")
   class Meta: 
      verbose_name=u'Статья'
      verbose_name_plural = u'Статьи'
   def __unicode__(o):
	  return o.title + " " + o.category.title

class Projects(models.Model):
   title = models.CharField(max_length = 255)
   text = models.TextField()
   meta_keyword = models.CharField(max_length = 255, blank = True)
   meta_description = models.CharField(max_length = 255, blank = True)
   pub_date = models.DateTimeField('date published', auto_now = True )
   class Meta: 
      verbose_name=u'Проект'
      verbose_name_plural = u'Проекты'

class Category(models.Model):
       title = models.CharField(max_length = 255)
       class Meta: 
	    verbose_name=u'Категория'
	    verbose_name_plural = u'Категории'
       def __unicode__(o):
	  return o.title  
  
class Audio(models.Model):
    title = models.CharField(max_length = 255, verbose_name = u"Аудио")
    audio = models.FileField(upload_to = "audio")
   
    class Meta: 
      verbose_name=u'Audio'
      verbose_name_plural = u'Audio'
      
    def __unicode__(o):
          return o.title    


class CustomMeta(models.Model):
    url = models.CharField(max_length = 255, verbose_name = u"Относительный url")
    meta_keyword = models.CharField(max_length = 255, blank = True)
    meta_description = models.CharField(max_length = 255, blank = True)   
    title = models.CharField(max_length = 255, verbose_name = u"Загаловок")
    class Meta: 
      verbose_name=u'Метоинформация'
      verbose_name_plural = u'Мета описание для Url'
      
    def __unicode__(o):
          return o.url 





TYPES = (
        ("yes", u'Опубликован'),
        ("no", u'Не опубликован')
        
        )




class Banner(models.Model):
        
    title = models.CharField(max_length = 255, verbose_name = u"Alt загаловок")
    img = models.ImageField(upload_to = 'banners_sq', verbose_name=u'Баннер')
    url = models.CharField(max_length=255,default="#",blank = True, null = True)
    is_pub =  models.CharField(max_length = 5,
                                        choices = TYPES,
                                        default = 'no', verbose_name = u"Опубликован")
    
    def get_thumbnail_url(self, prefix, width, height):
          src_path = settings.MEDIA_ROOT + "/" + str(self.img)
          thumb_url = None
          filename = str(self.img)
          R = filename.rindex("/")+1
          filename = filename[R:]
          path_to_thumbnail_dir =  "%sbanners_sq/%s" % (settings.MEDIA_ROOT, prefix)
          if not os.path.exists(path_to_thumbnail_dir):
                os.makedirs(path_to_thumbnail_dir)


          path_to_thumbnail = "%sbanners_sq/%s%s" % (settings.MEDIA_ROOT, prefix, filename)
          
          if not os.path.exists(path_to_thumbnail):
            #try:
                image = Image.open(self.img)
                image.thumbnail((width,"*"), Image.ANTIALIAS)
                image.crop( (0,0,width, height) )
                image.save(path_to_thumbnail, image.format, quality=95)
            #except:
                #return
          return "%sbanners_sq/%s%s" % (settings.MEDIA_URL, prefix, filename)
  
        ###to write more common method
    def get_small(self):
                 return  self.get_thumbnail_url("small")
             
    def get_tiny(self):
                 return  self.get_thumbnail_url("tiny",75, 75)
              
    def get_small(self):
                 return  self.get_thumbnail_url("small",150, 150)
                   

    def get_medium(self):
                return self.get_thumbnail_url("medium",410, 275)

    def get_big(self):
                return self.get_thumbnail_url("big",800, 800)

    def __unicode__(o):
          return  o.title 
    
    class Meta: 
        verbose_name=u'Баннер'
        verbose_name_plural = u'Баннеры'

  
  
class ProductionMenu(models.Model):
  title = models.CharField(max_length = 255)
  ordering =  models.IntegerField(verbose_name = u"Сортировка", default = 0 )
  url_item =  models.CharField(max_length = 255, blank = True, null = True,
			       verbose_name = u"Url страницы")
  item = models.ForeignKey('Production', blank = True, null = True )
  
			       
  class Meta: 
        verbose_name=u'Элемент меню продукции'
        verbose_name_plural = u'Меню продукции'
  def __unicode__(o):
          return o.title

class ProductionMenuItem(models.Model):  
  title = models.CharField(max_length = 255, blank = True, null = True )
  root = models.ForeignKey(ProductionMenu)
  item = models.ForeignKey('Production', blank = True, null = True )
  url_item =  models.CharField(max_length = 255, blank = True, null = True,
			       verbose_name = u"Url страницы")
  ordering =  models.IntegerField(verbose_name = u"Сортировка", default = 0 )
  
  class Meta: 
        verbose_name=u'Элемент меню продукции'
        verbose_name_plural = u'Меню продукции'
  def __unicode__(o):
          return o.title

        
class ProductionMenuItemInline(TabularInline):
    model = ProductionMenuItem
    extra = 10
    

class AdminProductionMenu(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ ProductionMenuItemInline ]
  
  


class Banners(models.Model):
    title = models.CharField(max_length = 255)
    text = models.CharField(max_length = 255)
    path = models.ImageField(upload_to = 'banners', verbose_name=u'Баннер')
    ordering = models.IntegerField(verbose_name = u"Сортировка", default = 0 )
    
    def get_thumbnail_url(self, prefix):
          src_path = settings.MEDIA_ROOT + "/" + str(self.path)
          thumb_url = None
          filename = str(self.path)
          R = filename.rindex("/")+1
          filename = filename[R:] ##we can optimize it
          return "%sbanners/%s%s" % (settings.MEDIA_URL, prefix, filename)
    def get_filename(self):
            
          filename = str(self.path)
          R = filename.rindex("/")+1
          filename = filename[R:]
          return filename

        ###to write more common method
    def get_small(self):
                 return  self.get_thumbnail_url("small")
        
    def save_small(self, width, height): 
             prefix = "small"
             filename = self.get_filename()
             image = Image.open(self.path)
             image.thumbnail((width,"*"), Image.ANTIALIAS)
             image.crop( (0,0,width, height) )
             path_to_thumbnail = "%sbanners/%s%s" % (settings.MEDIA_ROOT, prefix, filename)
             #quality=95 to settings ??
             image.save(path_to_thumbnail, image.format, quality=95)


    class Meta: 
      verbose_name=u'Слайд'
      verbose_name_plural = u'Слайд - меню'
      
    def __unicode__(o):
          return o.title
    
CURRENCY = (
        ("UAH", u'ГРН'),
        ("USD", u'USD'),
        ("EUR", u'EUR')       
        )    

class Brands(models.Model):
   title = models.CharField(max_length = 255, verbose_name = u"Название")                  
   
   def __unicode__(o):
          return o.title
   class Meta: 
      verbose_name=u'Бренд'
      verbose_name_plural = u'Бренд'

class ProductionSimpleCatalogAdmin(admin.ModelAdmin):
    list_display = ['archive', 'brand', 'pub_date','status']        


class ProductionSimpleCatalog(models.Model):
    archive = models.FileField(upload_to = "catalogs", verbose_name = u"Rar  архив каталога")
    brand = models.ForeignKey( Brands, verbose_name = u"Бренд" )  
    pub_date = models.DateTimeField('date published', auto_now = True, blank = True  )
    status =  models.CharField(max_length = 5,
                                        choices = TYPES,
                                        default = 'no', verbose_name = u"Опубликован")
    
    @property
    def filename(self):
        return settings.MEDIA_ROOT +  str(self.archive)

    class Meta: 
        verbose_name=u'Каталог'
        verbose_name_plural = u'Каталоги'

    
   
   

class ProductionElecticSimple(models.Model):      
   title = models.CharField( max_length = 255, verbose_name = u"Название позиции")
   text = models.TextField( verbose_name = u"Описание", blank = True)
   brand = models.ForeignKey( Brands, verbose_name = u"Бренд" )  
   power = models.CharField( max_length = 40, verbose_name = u"потребляемая мощность", blank = True )  
   
   price  = models.DecimalField(verbose_name = u"Цена",default = 0,
                                max_digits = 18, decimal_places = 2 )
   currency  = models.CharField(max_length = 24,choices = CURRENCY,
                                                default = 'USD', verbose_name = u"Валюта")
   meta_keyword = models.CharField(max_length = 255, blank = True )
   meta_description = models.CharField(max_length = 255, blank = True)
   pub_date = models.DateTimeField('date published', auto_now = True, blank = True  )
   ordering = models.IntegerField(verbose_name = u"Сортировка", default = 0 )
   thumb = models.ForeignKey('ImagesSimple', verbose_name=u'Photo', blank = True, null = True)   
   
   class Meta: 
      verbose_name = u'Продукция вспомогательная'
      verbose_name_plural = u'Продукция вспомогательная'
   def __unicode__(o):
          return o.title


class ImagesSimple(models.Model):
        path = models.ImageField(upload_to = 'simple_catalog', verbose_name=u'Photo')
        order = models.IntegerField(default = 0, verbose_name=u'Сортировка', blank = True)
        article = models.ForeignKey(ProductionElecticSimple, null = True)
        title =   models.CharField(max_length = 255,blank = True)        
        def get_thumbnail_url(self, prefix, width, height):
          src_path = settings.MEDIA_ROOT + "/" + str(self.path)
          #if not os.path.exists(src_path):  return None
          thumb_url = None
          filename = str(self.path)
          R = filename.rindex("/")+1
          filename = filename[R:]
          #path_to_thumbnail_dir =  ProjectSettings.PATH_FOR_SAVE_THUMB
          #if not os.path.exists(path_to_thumbnail_dir):
          #os.makedirs(path_to_thumbnail_dir)

          path_to_thumbnail = "%sfiles/%s%s" % (settings.MEDIA_ROOT,prefix,filename)
          if not os.path.exists(path_to_thumbnail):
            #try:
                image = Image.open(self.path)
                image.thumbnail((width,"*"), Image.ANTIALIAS)
                image.crop( (0,0,width, height) )
                image.save(path_to_thumbnail, image.format, quality=95)
            #except:
                #return
          return "%sfiles/%s%s" % (settings.MEDIA_URL, prefix, filename)

        def get_small(self):
                 return  self.get_thumbnail_url("small",75, 75)
                   

        def get_medium(self):
                return self.get_thumbnail_url("medium",410, 275)

        def get_big(self):
                return self.get_thumbnail_url("big",800, 600)

        def __unicode__(o):
          return str( o.path )

  
  
  

class Production(models.Model):
   title = models.CharField(max_length = 255)
   text = models.TextField()
   meta_keyword = models.CharField(max_length = 255, blank = True)
   meta_description = models.CharField(max_length = 255, blank = True)
   pub_date = models.DateTimeField('date published', auto_now = True  )
   ordering = models.IntegerField(verbose_name = u"Сортировка", default = 0 )
   introtext = models.TextField()
   class Meta: 
      verbose_name=u'Продукция'
      verbose_name_plural = u'Продукция'
   def __unicode__(o):
          return o.title


class Images(models.Model):
        path = models.ImageField(upload_to = 'files', verbose_name=u'Photo')
        path_thumb = models.ImageField(upload_to = 'files/thumb', verbose_name=u'Small Photo',blank = True)
        order = models.IntegerField(default = 0, verbose_name=u'Сортировка',blank = True)
        article = models.ForeignKey(Production)
        title =   models.CharField(max_length = 255,blank = True)
        
        def get_thumbnail_url(self, prefix, width, height):
          src_path = settings.MEDIA_ROOT + "/" + str(self.path)
          #if not os.path.exists(src_path):  return None

          thumb_url = None
          filename = str(self.path)
          R = filename.rindex("/")+1
          filename = filename[R:]
          #path_to_thumbnail_dir =  ProjectSettings.PATH_FOR_SAVE_THUMB
          #if not os.path.exists(path_to_thumbnail_dir):
          #os.makedirs(path_to_thumbnail_dir)

          path_to_thumbnail = "%sfiles/%s%s" % (settings.MEDIA_ROOT,prefix,filename)
          if not os.path.exists(path_to_thumbnail):
            #try:
                image = Image.open(self.path)
                image.thumbnail((width,"*"), Image.ANTIALIAS)
                image.crop( (0,0,width, height) )
                image.save(path_to_thumbnail, image.format, quality=95)
            #except:
                #return
          return "%sfiles/%s%s" % (settings.MEDIA_URL, prefix, filename)

        def get_small(self):
		 return  self.get_thumbnail_url("small",75, 75)
                   

        def get_medium(self):
                return self.get_thumbnail_url("medium",410, 275)

        def get_big(self):
                return self.get_thumbnail_url("big",800, 600)

        def __unicode__(o):
          return str( o.path )




class PresentPartn(models.Model):
   title = models.CharField(max_length = 255)
   text = models.TextField()
   meta_keyword = models.CharField(max_length = 255, blank = True)
   meta_description = models.CharField(max_length = 255, blank = True)
   pub_date = models.DateTimeField('date published', auto_now = True )
   class Meta: 
      verbose_name=u'Презентация'
      verbose_name_plural = u'Презентации'
          
          
class PresentetionImages(models.Model):
        path = models.ImageField(upload_to = 'present_files', verbose_name=u'Photo')
        #path_thumb = models.ImageField(upload_to = 'projects_files/thumb', verbose_name=u'Small Photo',blank = True)
        order = models.IntegerField(default = 0, verbose_name=u'Сортировка',blank = True)
        article = models.ForeignKey(PresentPartn)     

        def get_thumbnail_url(self, prefix, width, height):
          src_path = settings.MEDIA_ROOT + "/" + str(self.path)
          #if not os.path.exists(src_path):  return None

          thumb_url = None
          filename = str(self.path)
          R = filename.rindex("/")+1
          filename = filename[R:]
          #path_to_thumbnail_dir =  ProjectSettings.PATH_FOR_SAVE_THUMB
          #if not os.path.exists(path_to_thumbnail_dir):
          #os.makedirs(path_to_thumbnail_dir)

          path_to_thumbnail = "%spresent_files/%s%s" % (settings.MEDIA_ROOT, prefix, filename)
          if not os.path.exists(path_to_thumbnail):
            #try:
                image = Image.open(self.path)
                image.thumbnail((width,"*"), Image.ANTIALIAS)
                image.crop( (0,0,width, height) )
                image.save(path_to_thumbnail, image.format, quality=95)
            #except:
                #return
          return "%spresent_files/%s%s" % (settings.MEDIA_URL, prefix, filename)

        def get_tiny(self):
                 return  self.get_thumbnail_url("tiny",75, 75)
              

        def get_small(self):
                 return  self.get_thumbnail_url("small",150, 150)
                   

        def get_medium(self):
                return self.get_thumbnail_url("medium",410, 275)

        def get_big(self):
                return self.get_thumbnail_url("big",800, 600)

        def __unicode__(o):
          return str( o.path )
          
#class for inline image
class PresentPartnImagesInline(TabularInline):
    model = PresentetionImages
    extra = 10

class AdminPresentPartn(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ PresentPartnImagesInline ]    
    




class Pictures(models.Model):
        
    title = models.CharField(max_length = 255, verbose_name = u"Alt загаловок")
    img = models.ImageField(upload_to = 'art_images', verbose_name=u'Картинка')
    
    def url(self):
	 return  settings.MEDIA_URL + str(self.img)
    
    def get_thumbnail_url(self, prefix, width, height):
          src_path = settings.MEDIA_ROOT + "/" + str(self.img)
          thumb_url = None
          filename = str(self.img)
          R = filename.rindex("/")+1
          filename = filename[R:]
          path_to_thumbnail_dir =  "%sart_images/%s" % (settings.MEDIA_ROOT, prefix)
          if not os.path.exists(path_to_thumbnail_dir):
                os.makedirs(path_to_thumbnail_dir)


          path_to_thumbnail = "%sart_images/%s%s" % (settings.MEDIA_ROOT, prefix, filename)
          
          if not os.path.exists(path_to_thumbnail):
            #try:
                image = Image.open(self.img)
                image.thumbnail((width,"*"), Image.ANTIALIAS)
                image.crop( (0,0,width, height) )
                image.save(path_to_thumbnail, image.format, quality=95)
            #except:
                #return
          return "%sart_images/%s%s" % (settings.MEDIA_URL, prefix, filename)
  
        ###to write more common method
    def get_small(self):
                 return  self.get_thumbnail_url("small")
             
    def get_tiny(self):
                 return  self.get_thumbnail_url("tiny",75, 75)
              
    def get_small(self):
                 return  self.get_thumbnail_url("small",150, 150)
                   

    def get_medium(self):
                return self.get_thumbnail_url("medium",410, 275)

    def get_big(self):
                return self.get_thumbnail_url("big",800, 800)

    def __unicode__(o):
          return  o.title 
    
    class Meta: 
        verbose_name=u'Картинку'
        verbose_name_plural = u'Картинки'

class AdminPictures(admin.ModelAdmin):
       list_display = ['title', 'url']



class ProjectsImages(models.Model):
        path = models.ImageField(upload_to = 'projects_files', verbose_name=u'Photo')
        #path_thumb = models.ImageField(upload_to = 'projects_files/thumb', verbose_name=u'Small Photo',blank = True)
        order = models.IntegerField(default = 0, verbose_name=u'Сортировка',blank = True)
        article = models.ForeignKey(Projects)     
        def url(self):
	    return  settings.MEDIA_URL +  str(self.path)
        
	def get_thumbnail_url(self, prefix, width, height):
          src_path = settings.MEDIA_ROOT +  str(self.path)
          #if not os.path.exists(src_path):  return None

          thumb_url = None
          filename = str(self.path)
          R = filename.rindex("/")+1
          filename = filename[R:]
          #path_to_thumbnail_dir =  ProjectSettings.PATH_FOR_SAVE_THUMB
          #if not os.path.exists(path_to_thumbnail_dir):
          #os.makedirs(path_to_thumbnail_dir)

          path_to_thumbnail = "%sprojects_files/%s%s" % (settings.MEDIA_ROOT, prefix, filename)
          if not os.path.exists(path_to_thumbnail):
            #try:
                image = Image.open(self.path)
                image.thumbnail((width,"*"), Image.ANTIALIAS)
                image.crop( (0,0,width, height) )
                image.save(path_to_thumbnail, image.format, quality=95)
            #except:
                #return
          return "%sprojects_files/%s%s" % (settings.MEDIA_URL, prefix, filename)

	def get_tiny(self):
		 return  self.get_thumbnail_url("tiny",75, 75)
              

        def get_small(self):
		 return  self.get_thumbnail_url("small",150, 150)
                   

        def get_medium(self):
                return self.get_thumbnail_url("medium",410, 275)

        def get_big(self):
                return self.get_thumbnail_url("big",800, 600)

        def __unicode__(o):
          return str( o.path )

class AdminBanners(admin.ModelAdmin):
       list_display = ['title']
       def save_model(self, request, obj, form, change):
            obj.save()
            obj.save_small(920,400)##to settings ?
       
       
       
def add_logo(sender, instance, created, **kwargs):
    add_log2image(instance.img)

def add_logo_proj(sender, instance, created, **kwargs):
    add_log2image(instance.path)
    
def add_logo_presen(sender, instance, created, **kwargs):
    add_log2image(instance.path)  

def add_logo_ban(sender, instance, created, **kwargs):
    add_log2image(instance.path)      
    
def add_logo_prod(sender, instance, created, **kwargs):
    add_log2image(instance.path)
    
signals.post_save.connect(add_logo, sender = Pictures)
signals.post_save.connect(add_logo_proj, sender = ProjectsImages)
signals.post_save.connect(add_logo_presen, sender = PresentetionImages)
#signals.post_save.connect(add_logo_ban, sender = Banners)
#signals.post_save.connect(add_logo_prod, sender = Images)
#signals.post_save.connect(add_logo_prod, sender = ImagesSimple)


       
##add logo to image       
def add_log2image(Path):
    Img = settings.MEDIA_ROOT +str(Path)
    baseim = Image.open( Img )
    logoim = Image.open(settings.LOGO) #transparent image
    width = logoim.size[0]
    height = logoim.size[1]
    #print "%i %i" % (width, height)
    NewWidth = baseim.size[0]/10 ##scale logo
    NewHeight = int(height*((1.0*NewWidth)/width))
    #print "%i %i" % (NewWidth, NewHeight)
    NewLogo =  logoim.resize((NewWidth, NewHeight), Image.ANTIALIAS) ## to new width
    
    baseim.paste(NewLogo, ( baseim.size[0]-NewLogo.size[0] - NewLogo.size[0]/3,
			    baseim.size[1]-NewLogo.size[1] - NewLogo.size[1]/3 ), NewLogo)
    baseim.save(Img, baseim.format)
    return Img
    

        


#class for inline image
class ProjectsImagesInline(TabularInline):
    model = ProjectsImages
    extra = 10


class ImagesInline(TabularInline):
    model = Images
    extra = 10

#class for inline image
class ElectricImagesInline(TabularInline):
    model = ImagesSimple
    extra = 10

class AdminProductionElecticSimple(admin.ModelAdmin):
    list_display = ['title','text','price']
    inlines = [ ElectricImagesInline ]    

class AdminProduction(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ ImagesInline ]
    
class AdminProjects(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ ProjectsImagesInline ]    
    
