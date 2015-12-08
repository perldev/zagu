# -*- coding: utf-8 -*-
# Create your views here.
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse 
from pyzagu import settings
from main.models import Articles,Production, Images, ProjectsImages, Banners, PresentetionImages, Audio
from main.models import Banner, CustomMeta
from main.models import ProductionMenu, ProductionMenuItem, ProductionElecticSimple, Brands, ImagesSimple
from django.contrib.auth.models import User

import django.contrib.auth
from django.core.mail import send_mail

import re
from MyHttp import my_connect
from django.core.context_processors import csrf

def my_custom_404_view(req):
    t = loader.get_template('template404.html')    
    Dict = setup_custom_meta(req, {})

    c = Context(
      Dict
    )

    return HttpResponse(t.render(c))

def sitemap(req):
    t = loader.get_template('sitemap.xml')    
    c = Context(
      {}
    )
    Response = HttpResponse(t.render(c))
    Response['Content-Type'] = 'application/xml'

    return Response

def robots(req):        
    t = loader.get_template('robots.txt')    
    c = Context(
      {}
    )
    Response = HttpResponse(t.render(c))
    Response['Content-Type'] = 'text/plain'
    return Response


def send_feedback(req):
    Text = req.REQUEST.get('text', None)
    SendCopy = req.REQUEST.get('send_copy', None)
    SendCopyTo = req.REQUEST.get('send_copy_mail', None)
    
    if  Text is None :
        return feedback(req, 'text_error')
    
    
    if  validateEmail( SendCopyTo ) == 0   :
        return feedback(req, 'error_bad_email')
    
    Copy = None
    
    if  SendCopy is  None :
        Copy = ['sales@zagu.ua','info@zagu.ua']
    else:
        Copy = ['sales@zagu.ua','info@zagu.ua', SendCopyTo ]
        
   
    #Ip = req.META['REMOTE_ADDR']
    #CRes = req.REQUEST.get('recaptcha_response_field',"")
    #Ch = req.REQUEST.get('recaptcha_challenge_field','')
    
    #Ret = my_connect( "http://www.google.com/recaptcha/api/verify", 
                                      #{ 
                                       #"privatekey": "6LfofeQSAAAAAHXsCF8dfBzZS35zqz2Yy_oiKBRY" ,
                                       #"remoteip": Ip,
                                       #"challenge": Ch ,
                                       #"response" : CRes
                                       #}  )
   
    #if validateCaptcha1(Ret) :
        #return feedback(req, 'error_captcha')    


    send_mail("zagu.ua feedback " + SendCopyTo, Text, 'robot@zagu.ua', Copy , fail_silently = False)

    t = loader.get_template('static_page.html')
    Dict =  {
        "pagetitle": u"Ваша сообщение успешно отправлено",
        "text": u"Мы вам ответим в ближайшее время",
        "title":u"Ваша сообщение успешно отправлено"      
    }
    Dict.update(csrf(req))
    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)    
    Dict = setup_custom_meta(req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))
    

def validateEmail(email):
        if len(email) > 7:
                if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                        return 1
        return 0    
    
    
    
 
def validateCaptcha(ret):
    if  ret.split("\n")[0] == "false":
        return True    
    return False

def feedback(req, error = None):
    t = loader.get_template('feedback.html')
    Dict = {}
    Dict.update(csrf(req))

    if error is not None:
        Dict[error] = 1  
    
    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)
    Dict = setup_custom_meta(req, Dict)
    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))

    


def googlever2(req):
        return HttpResponse("google-site-verification: googlee288c274f02aaeea.html")
    
def googlever(req):    
        return HttpResponse("google-site-verification: googlecf83282b8297d084.html")

def project(req, i):
    t = loader.get_template('projects.html')
    
    dict1 = {}
    dict1["second_menu"] = []
    dict1["pagetitle"] = u"Наши проекты"
    dict1 = setup_bot_news(dict1, 2)
    dict1 = setup_projects(dict1)
    l = ProjectsImages.objects.all()
    current = ProjectsImages.objects.filter(article = int(i)).first()
    dict1["projects_list"] = l
    dict1["gallery_current_title"] = current.article.title
    dict1["gallery_current_desc"] = current.article.text
    dict1["gallery_current_big_img"] = current.get_big() 
    dict1["gallery_current"] = current.article.id
    dict1["gallery_count"] = l.count()
    dict1 = setup_custom_meta(req, dict1)
    c = Context(
      dict1
    )
    return HttpResponse(t.render(c))  

def for_partners(req, i):
    t = loader.get_template('projects_partners.html')
    if int(i) == 0:
       i = 1    
    dict1 = {}
    dict1["second_menu"] = []
    dict1["pagetitle"] = u"Нашим партнерам"
    dict1 = setup_bot_news(dict1, 2)
    dict1 = setup_projects(dict1)
    l = PresentetionImages.objects.all()
    current = PresentetionImages.objects.get(id = i)
    dict1["projects_list"] = l
    dict1["gallery_current_title"] = current.article.title
    dict1["gallery_current_desc"] = current.article.text
    dict1["gallery_current_big_img"] = current.get_big() 
    dict1["gallery_current"] = current.article.id
    dict1["gallery_count"] = l.count()
    dict1 = setup_custom_meta(req, dict1)
    c = Context(
      dict1
    )
    return HttpResponse(t.render(c))  

def catalog_item(Req, Id):
    Id = int(Id)
   
    try :
        item =  ProductionElecticSimple.objects.get(id = Id)
    except :
        return my_custom_404_view(Req)   
    
    t = loader.get_template('catalog-products-item.html')
    Dict = setup_item_menu({}, -1 )
    Dict["pagetitle"] = u"%s" % (item.title)
    Dict["keywords"] = item.meta_keyword
    Dict["description"] = item.meta_description
    Dict["item"] = item
    Dict["additional_images"] = ImagesSimple.objects.filter(article = item)
    Dict = setup_custom_meta(Req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))    
        

def catalog(Req, Id):
    Id = int(Id)
    brand = Brands.objects.get(id = Id)    
    List =  list(ProductionElecticSimple.objects.filter(brand = brand).order_by("ordering") )   
    t = loader.get_template('catalog-products.html')
    Dict = setup_item_menu({}, -1 )
    Dict["pagetitle"] = u"Каталог - %s" % (brand.title)
    Length = len(List)
    Dict["list1"] = List[:Length/2]
    Dict["list2"] = List[Length/2:]   
    Dict = setup_custom_meta(Req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))

    
    
def projects(req):
  
    t = loader.get_template('projects.html')
    
    dict1 = {}
    dict1["second_menu"] = []
    dict1["pagetitle"] = u"Наши проекты"
    dict1 = setup_bot_news(dict1, 2)
    dict1 = setup_projects(dict1)
    l = ProjectsImages.objects.all().order_by("order")
    dict1["projects_list"] = l
    dict1["gallery_current_title"] = l[0].article.title
    dict1["gallery_current_desc"] = l[0].article.text
    dict1["gallery_current_big_img"] = l[0].get_big() 
    dict1["gallery_current"] = l[0].article.id
    dict1["gallery_count"] = l.count()
    dict1 = setup_custom_meta(req, dict1)

    c = Context(
      dict1
    )
    return HttpResponse(t.render(c))    
  
#class Images(models.Model):
        #path = models.ImageField(upload_to = 'files', verbose_name=u'Photo')
        #path_thumb = models.ImageField(upload_to = 'files/thumb', verbose_name=u'Small Photo',blank = True)
        #order = models.IntegerField(default = 0, verbose_name=u'Сортировка',blank = True)
        #article = models.ForeignKey(Production)
        #title =   models.CharField(max_length = 255,blank = True)
def contacts(req):
    t = loader.get_template('static_page.html')
    article = Articles.objects.get(id=3)
    Dict =  {
	"pagetitle": article.title,
	"text": article.text,
	"title":article.title,
	"keywords": article.meta_keyword,
	"description": article.meta_description,
	"id":article.id
      
    }
    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)
    Dict = setup_custom_meta(req, Dict)
    
    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))
  
def calc_soft(req):
    t = loader.get_template('static_page.html')
    article = Articles.objects.get(id=5)
    Dict =  {
	"pagetitle": article.title,
	"text": article.text,
	"title":article.title,
	"keywords": article.meta_keyword,
	"description": article.meta_description,
	"id":article.id
      
    }
    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)
    Dict = setup_custom_meta(req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))



def cabinet(req):
    t = loader.get_template('static_page.html')
    article = Articles.objects.get(id=4)
    Dict =  {
	"pagetitle": article.title,
	"text": article.text,
	"title":article.title,
	"keywords": article.meta_keyword,
	"description": article.meta_description,
	"id":article.id
      
    }
    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)
    Dict = setup_custom_meta(req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))


##TODO adding logic 
def colors_config(req):
    t = loader.get_template('color_config.html')
    Dict = setup_item_menu({}, -1 )
    images = list( Images.objects.filter(article = 1 ).filter().order_by("order") )
    result = []
    for item in images[2:] :
        result.append({"title":item.title, "path": item.path })
    
    Dict["pool_colors"] = result
    Dict["pool_colors"][0]["color_config"] = "slon.png"
    Dict["pool_colors"][1]["color_config"] = "osen.png"
    Dict["pool_colors"][2]["color_config"] = "caprum.png"
    Dict["pool_colors"][3]["color_config"] = "patina.png"
    Dict["pool_colors"][4]["color_config"] = "darck_chock.png"

    Dict = setup_custom_meta(req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))   
  
        
def item_production(req, i):
    t = loader.get_template('news-products.html')
    Dict = setup_item_menu({}, int(i) )
    main_images = Images.objects.filter(article = Dict["current"] ).order_by("order")[:2]
    images = Images.objects.filter(article = Dict["current"] ).order_by("order")[2:]

    Dict["current"].product_img = settings.MEDIA_URL + str(main_images[0].path)
    Dict["current"].inter_img = settings.MEDIA_URL + str(main_images[1].path)
    
    
    for i in images :
	i.path = settings.MEDIA_URL + str(i.path)
	
    Dict["colors"] = images    
    Dict = setup_custom_meta(req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))
    
    
  
def production(req):
    return HttpResponseRedirect("/item_production/1")
    

def home(req):
    t = loader.get_template('index.html')
    article = Articles.objects.get(id=1)
    Dict =  {
	"pagetitle": article.title,
	"text": article.introtext,
	"keywords": article.meta_keyword,
	"description": article.meta_description,
	"id":article.id,
	"sliders": Banners.objects.all().order_by("ordering")
    }
    try:
        banner = Banner.objects.get(is_pub="yes")
        Dict["banner"] = banner
    except:
        pass    
    
    
    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)
    Dict = setup_banner(Dict)
    Dict = setup_custom_meta(req, Dict)

    c = Context(
      Dict
    )
    return HttpResponse(t.render(c))


def article(req, i):
  
    article = Articles.objects.get( id = int(i) )
    Dict =  {
	"pagetitle": article.title,
	"title": article.title,
	"text": article.text,
	"keywords": article.meta_keyword,
	"description": article.meta_description
      
    }
    NewContext = setup_content_menu(Dict, 3)#means articles  
    NewContext = setup_custom_meta(req, NewContext)

    c = Context(
	  NewContext
    )
    
    t = loader.get_template('news-inside.html')
    return HttpResponse(t.render(c))
  
def article_partners(req, i):
  
    article = Articles.objects.get( id = int(i) )
    Dict =  {
	"pagetitle": article.title,
	"title": article.title,
	"text": article.text,
	"keywords": article.meta_keyword,
	"description": article.meta_description
      
    }
    NewContext = setup_content_menu(Dict, 4)#means for partners    
    NewContext = setup_custom_meta(req, NewContext)

    c = Context(
	  NewContext
    )
    
    t = loader.get_template('news-inside.html')
    return HttpResponse(t.render(c))  
  
  
def news_article(req, i):
  
    article = Articles.objects.get( id = int(i) )
    Dict =  {
	"pagetitle": article.title,
	"title": article.title,
	"text": article.text,
	"keywords": article.meta_keyword,
	"description": article.meta_description
      
    }
    NewContext = setup_content_menu(Dict, 2)#means news    
    NewContext = setup_custom_meta(req, NewContext)

    c = Context(
	NewContext
    )
    t = loader.get_template('news-inside.html')
    return HttpResponse(t.render(c))	  

def setup_item_menu(Context, Current):
    Objects = ProductionMenu.objects.all().order_by("-ordering")
    #Objects = list(Production.objects.all().order_by("-ordering"))
    for i in Objects:
	#try : 
	  Sub_menu = ProductionMenuItem.objects.filter(root = i).order_by("-ordering")
	  for sub_item in Sub_menu:
	    if hasattr(sub_item, 'item')and sub_item.item is not None  and sub_item.item.id == Current :
	      i.current = 1
	      Context["current"] = sub_item.item
	    if hasattr(sub_item, 'item') and sub_item.item is not None :
	      sub_item.url_item = "/item_production/" + str(sub_item.item.id)   
	      if  sub_item.title == "" :
		  sub_item.title =  str(sub_item.item)
		  
	    if sub_item.url_item =="":
	      sub_item.url_item = "#"
	  if i.url_item =="":
	      i.url_item = "#"     
	  i.sub_items = Sub_menu
	#except :
	  #i.sub_items = [] 
    
    #color_current = None    
    #if	Current == -1:
      #color_current = 1; 
    #Objects.append({'url_item':"/colors_config","name":u"Подобрать цвет","title":u"Подобрать цвет","current": color_current })

    Context["second_menu"] = Objects
    Context["pagetitle"] = u"Продукция Zagu"
    Context = setup_bot_news(Context, 2)
    Context = setup_projects(Context)
    
    return Context

def articles(req, page):
    return list_of_content(req,  3, page)
  

def news(req, page):
     return list_of_content(req,  2, page)
  

def setup_banner(Dict):
    return Dict
  
def setup_projects(Dict):
    objs = ProjectsImages.objects.all().order_by("-id")[:4]
    audio = Audio.objects.all()
    
    
    Dict["MEDIA_URL"] =  settings.MEDIA_URL
    Dict["projects"] = objs
    Dict["audio_file"] = audio
    
    return Dict

def  setup_bot_news(Dict ,page):
    Dict['bot_news'] = get_articles(2, 0, page, 0) #type news, page = 0, count page = 2
    
    return Dict
  
def list_of_content(req,  Type, page, limit = 0):
    base = { 2:"/news/",
             3:"/articles/",
             4:"/for_partners/"
        }
    
    t = loader.get_template('news.html')    
    page = int(page)
    ItemsPerPage  = 2
    objects = get_articles(Type, page, ItemsPerPage, limit)
    tmp_c  = setup_content_menu({}, Type)    
    tmp_c["content_objects"] = objects
    if page != 0:
	tmp_c["prev_page"] = base[Type] + str( page - 1)

    if len(objects) ==  ItemsPerPage:
        tmp_c["next_page"] = base[Type] + str( page + 1 )
    Dict = setup_custom_meta(req, tmp_c)

    c = Context(
	Dict
    )
    return HttpResponse(t.render(c))
  
def get_articles(Type, page, Count, Greater):
        Offset = page*Count
        Limit = Offset + Count
	objects = Articles.objects.filter(category = Type, id__gt = Greater ).order_by("-pub_date")[Offset:Limit]
	link ="/news_article";
	if Type  == 3 :
	    link ="/article"
	if Type == 4 :
	     link ="/article_partners"
	for item in objects :
		item.link = link + "/" + str(item.id)
	return objects
  
def setup_content_menu(Context, SelectedMenu ):
    MenuList = None
    if SelectedMenu == 3: ##it link to category table 
	  MenuList = [ {"title": u"Новости","url_item": "/news/0" },
			{"title": u"Статьи", "url_item": "/articles/0","current":1},
			{"title": u"Партнерам","url_item": "/for_partners/0" }]
	  Title = u"" #u"Zagu Статьи"
    if SelectedMenu == 2:
	  MenuList = [ {"title": u"Новости","url_item": "/news/0" ,"current":1},
			{"title": u"Статьи", "url_item": "/articles/0"},
			{"title": u"Партнерам","url_item": "/for_partners/0" }]
	  Title = u"Zagu Новости"
    if SelectedMenu == 4:
	  MenuList = [ {"title": u"Новости","url_item": "/news/0" },
			{"title": u"Статьи", "url_item": "/articles/0"},
			{"title": u"Партнерам","url_item": "/for_partners/0","current":1 }] 
	  Title = u"Zagu партнерам"
    Context["second_menu"] = MenuList
    Context["pagetitle"] = Title
    Context = setup_bot_news(Context, 2)
    Context = setup_projects(Context)
    return  Context
      
      
def setup_custom_meta(req, NewContext):
        Path = req.get_full_path()
        try :
             custom_meta =  CustomMeta.objects.get(url = Path)
             NewContext["pagetitle"] = custom_meta.title 
             NewContext["description"] = custom_meta.meta_description
             NewContext["keywords"] = custom_meta.meta_keyword
             return NewContext
        except :
             return NewContext
        

  