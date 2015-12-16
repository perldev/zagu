# -*- coding: utf-8 -*-
# Create your views here.
import re

from django.template import Context, loader, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.http import last_modified


from main.models import Articles, Production, Images, ProjectsImages, Banners, PresentetionImages, Audio
from main.models import Banner, CustomMeta
from main.models import ProductionMenu, ProductionMenuItem, ProductionElecticSimple, Brands, ImagesSimple


def my_custom_404_view(request):
    t = loader.get_template('template404.html')
    Dict = setup_custom_meta(request, {})

    c = Context(
        Dict
    )

    return HttpResponse(t.render(c))


def sitemap(request):
    t = loader.get_template('sitemap.xml')
    c = Context(
        {}
    )
    Response = HttpResponse(t.render(c))
    Response['Content-Type'] = 'application/xml'

    return Response


def robots(request):
    t = loader.get_template('robots.txt')
    c = Context(
        {}
    )
    Response = HttpResponse(t.render(c))
    Response['Content-Type'] = 'text/plain'
    return Response


def send_feedback(request):
    Text = request.REQUEST.get('text', None)
    SendCopy = request.REQUEST.get('send_copy', None)
    SendCopyTo = request.REQUEST.get('send_copy_mail', None)

    if Text is None:
        return feedback(request, 'text_error')

    if validateEmail(SendCopyTo) == 0:
        return feedback(request, 'error_bad_email')

    Copy = None

    if SendCopy is None:
        Copy = ['sales@zagu.ua', 'info@zagu.ua']
    else:
        Copy = ['sales@zagu.ua', 'info@zagu.ua', SendCopyTo]


        # Ip = request.META['REMOTE_ADDR']
        # CRes = request.REQUEST.get('recaptcha_response_field',"")
        # Ch = request.REQUEST.get('recaptcha_challenge_field','')

        # Ret = my_connect( "http://www.google.com/recaptcha/api/verify",
        # {
        # "privatekey": "6LfofeQSAAAAAHXsCF8dfBzZS35zqz2Yy_oiKBRY" ,
        # "remoteip": Ip,
        # "challenge": Ch ,
        # "response" : CRes
        # }  )

        # if validateCaptcha1(Ret) :
        # return feedback(request, 'error_captcha')

    send_mail("zagu.ua feedback " + SendCopyTo, Text, 'robot@zagu.ua', Copy, fail_silently=False)

    t = loader.get_template('static_page.html')
    Dict = {
        "pagetitle": u"Ваша сообщение успешно отправлено",
        "text": u"Мы вам ответим в ближайшее время",
        "title": u"Ваша сообщение успешно отправлено"
    }
    Dict.update(csrf(request))
    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)
    Dict = setup_custom_meta(request, Dict)

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
    if ret.split("\n")[0] == "false":
        return True
    return False


def feedback(request, error=None):
    t = loader.get_template('feedback.html')
    Dict = {}
    Dict.update(csrf(request))

    if error is not None:
        Dict[error] = 1

    Dict = setup_bot_news(Dict, 2)
    Dict = setup_projects(Dict)
    Dict = setup_custom_meta(request, Dict)
    c = Context(
        Dict
    )
    return HttpResponse(t.render(c))


def googlever2(request):
    return HttpResponse("google-site-verification: googlee288c274f02aaeea.html")


def googlever(request):
    return HttpResponse("google-site-verification: googlecf83282b8297d084.html")


def get_project(request, item):
    context = dict()
    context["second_menu"] = []
    context["pagetitle"] = u"Наши проекты"
    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    projects_list = ProjectsImages.objects.all()
    context["projects_list"] = projects_list
    context["gallery_count"] = projects_list.count()
    current = ProjectsImages.objects.filter(article__url=item).first()
    if current:
        context["gallery_current_title"] = current.article.title
        context["gallery_current_desc"] = current.article.text
        context["gallery_current_big_img"] = current.get_big()
        context["gallery_current"] = current.article.id

    context = setup_custom_meta(request, context)

    return render_to_response('projects.html', context, context_instance=RequestContext(request))


def for_partners(request, item=1):
    context = dict()
    context["second_menu"] = []
    context["pagetitle"] = u"Нашим партнерам"
    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    projects_list = PresentetionImages.objects.all()
    context["projects_list"] = projects_list
    context["gallery_count"] = projects_list.count()

    try:
        current = projects_list.get(id=item)
        context["gallery_current_title"] = current.article.title
        context["gallery_current_desc"] = current.article.text
        context["gallery_current_big_img"] = current.get_big()
        context["gallery_current"] = current.article.id
    except PresentetionImages.DoesNotExist:
        pass

    context = setup_custom_meta(request, context)

    return render_to_response('projects_partners.html', context, context_instance=RequestContext(request))


def catalog_item(request, url):
    item = get_object_or_404(ProductionElecticSimple, url=url)

    context = setup_item_menu({}, -1)
    context["pagetitle"] = item.title
    context["keywords"] = item.meta_keyword
    context["description"] = item.meta_description
    context["item"] = item
    context["additional_images"] = ImagesSimple.objects.filter(article=item)
    context = setup_custom_meta(request, context)

    return render_to_response('catalog-products-item.html', context, context_instance=RequestContext(request))


def catalog(request, url):
    brand = get_object_or_404(Brands, url=url)
    List = list(ProductionElecticSimple.objects.filter(brand=brand).order_by("ordering"))
    t = loader.get_template('catalog-products.html')
    Dict = setup_item_menu({}, -1)
    Dict["pagetitle"] = u"Каталог - %s" % (brand.title)
    Length = len(List)
    Dict["list1"] = List[:Length / 2]
    Dict["list2"] = List[Length / 2:]
    Dict = setup_custom_meta(request, Dict)

    c = Context(
        Dict
    )
    return HttpResponse(t.render(c))


def projects(request):
    context = dict()
    context["second_menu"] = []
    context["pagetitle"] = u"Наши проекты"
    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    projects_list = ProjectsImages.objects.all().order_by("order")
    context["projects_list"] = projects_list
    if projects_list.exists():
        context["gallery_current_title"] = projects_list[0].article.title
        context["gallery_current_desc"] = projects_list[0].article.text
        context["gallery_current_big_img"] = projects_list[0].get_big()
        context["gallery_current"] = projects_list[0].article.id
        context["gallery_count"] = projects_list.count()
    context = setup_custom_meta(request, context)

    return render_to_response('projects.html', context, context_instance=RequestContext(request))


def contacts(request):
    article = get_object_or_404(Articles, id=3)
    context = {
        "pagetitle": article.title,
        "text": article.text,
        "title": article.title,
        "keywords": article.meta_keyword,
        "description": article.meta_description,
        "id": article.id
    }
    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    context = setup_custom_meta(request, context)

    return render_to_response('static_page.html', context, context_instance=RequestContext(request))


def calc_soft(request):
    article = get_object_or_404(Articles, id=5)
    context = {
        "pagetitle": article.title,
        "text": article.text,
        "title": article.title,
        "keywords": article.meta_keyword,
        "description": article.meta_description,
        "id": article.id
    }
    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    context = setup_custom_meta(request, context)

    return render_to_response('static_page.html', context, context_instance=RequestContext(request))


def cabinet(request):
    article = get_object_or_404(Articles, id=4)
    context = {
        "pagetitle": article.title,
        "text": article.text,
        "title": article.title,
        "keywords": article.meta_keyword,
        "description": article.meta_description,
        "id": article.id
    }
    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    context = setup_custom_meta(request, context, extra_meta='<meta name="robots" content="NoIndex, NoFollow" />')

    return render_to_response('static_page.html', context, context_instance=RequestContext(request))


# TODO adding logic
def colors_config(request):
    context = setup_item_menu({}, -1)
    images = list(Images.objects.filter(article_id=1).filter().order_by("order"))
    result = []
    for item in images[2:]:
        result.append({"title": item.title, "path": item.path})

    context["pool_colors"] = result
    if len(result) > 1:
        context["pool_colors"][0]["color_config"] = "slon.png"
        context["pool_colors"][1]["color_config"] = "osen.png"
        context["pool_colors"][2]["color_config"] = "caprum.png"
        context["pool_colors"][3]["color_config"] = "patina.png"
        context["pool_colors"][4]["color_config"] = "darck_chock.png"

    context = setup_custom_meta(request, context)

    return render_to_response('color_config.html', context, context_instance=RequestContext(request))


def item_production(request, item=None):
    if item:
        product = get_object_or_404(Production, url=item)
    else:
        product = Production.objects.first()
    context = setup_item_menu({}, product.id)
    main_images = Images.objects.filter(article=context["current"]).order_by("order")[:2]
    images = Images.objects.filter(article=context["current"]).order_by("order")[2:]

    context["current"].product_img = settings.MEDIA_URL + str(main_images[0].path)
    context["current"].inter_img = settings.MEDIA_URL + str(main_images[1].path)

    for i in images:
        i.path = settings.MEDIA_URL + str(i.path)

    context["colors"] = images
    context = setup_custom_meta(request, context)

    return render_to_response('news-products.html', context, context_instance=RequestContext(request))


def latest_article(request):
    return Articles.objects.latest("pub_date").pub_date


#@last_modified(latest_article)
def home(request):
    context = {"sliders": Banners.objects.all().order_by("ordering"),}
    try:
        article = Articles.objects.all()[0]
        context["pagetitle"] = article.title
        context["text"] = article.introtext
        context["keywords"] = article.meta_keyword
        context["description"] = article.meta_description
        context["id"] = article.id
        context['article'] = article
    except Articles.DoesNotExist:
        pass
    try:
        banner = Banner.objects.get(is_pub="yes")
        context["banner"] = banner
    except Banner.DoesNotExist:
        pass

    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    context = setup_banner(context)
    context = setup_custom_meta(request, context)

    return render_to_response('index.html', context, context_instance=RequestContext(request))


def get_article(request, item):
    article = get_object_or_404(Articles, url=item)
    context = {
        "pagetitle": article.title,
        "title": article.title,
        "text": article.text,
        "keywords": article.meta_keyword,
        "description": article.meta_description
    }
    context = setup_content_menu(context, 3)  # means articles
    context = setup_custom_meta(request, context)

    return render_to_response('news-inside.html', context, context_instance=RequestContext(request))


def article_partners(request, item):
    article = get_object_or_404(Articles, url=item)
    context = {
        "pagetitle": article.title,
        "title": article.title,
        "text": article.text,
        "keywords": article.meta_keyword,
        "description": article.meta_description
    }
    context = setup_content_menu(context, 4)  # means for partners
    context = setup_custom_meta(request, context)

    return render_to_response('news-inside.html', context, context_instance=RequestContext(request))


def news_article(request, item):
    article = get_object_or_404(Articles, url=item)
    context = {
        "pagetitle": article.title,
        "title": article.title,
        "text": article.text,
        "keywords": article.meta_keyword,
        "description": article.meta_description,
        "another_news": Articles.objects.filter(category=article.category).exclude(url=item)
    }
    context = setup_content_menu(context, 2)  # means news
    context = setup_custom_meta(request, context)

    return render_to_response('news-inside.html', context, context_instance=RequestContext(request))


def setup_item_menu(Context, Current):
    Objects = ProductionMenu.objects.all().order_by("-ordering")
    for i in Objects:
        # try :
        Sub_menu = ProductionMenuItem.objects.filter(root=i).order_by("-ordering")
        for sub_item in Sub_menu:
            if hasattr(sub_item, 'item') and sub_item.item is not None and sub_item.item.id == Current:
                i.current = 1
                Context["current"] = sub_item.item
            if hasattr(sub_item, 'item') and sub_item.item is not None:
                sub_item.url_item = "/production/" + str(sub_item.item.url)
                if sub_item.title == "":
                    sub_item.title = str(sub_item.item)

            if sub_item.url_item == "":
                sub_item.url_item = "#"
        if i.url_item == "":
            i.url_item = "#"
        i.sub_items = Sub_menu
    # except :
    # i.sub_items = []

    # color_current = None
    # if	Current == -1:
    # color_current = 1;
    # Objects.append({'url_item':"/colors_config","name":u"Подобрать цвет","title":u"Подобрать цвет","current": color_current })

    Context["second_menu"] = Objects
    Context["pagetitle"] = u"Продукция Zagu"
    Context = setup_bot_news(Context, 2)
    Context = setup_projects(Context)

    return Context


def articles(request, page=None):
    return list_of_content(request, 3, page)


def news(request, page=None):
    return list_of_content(request, 2, page)


def setup_banner(Dict):
    return Dict


def setup_projects(Dict):
    objs = ProjectsImages.objects.all().order_by("-id")[:4]
    audio = Audio.objects.all()

    Dict["MEDIA_URL"] = settings.MEDIA_URL
    Dict["projects"] = objs
    Dict["audio_file"] = audio

    return Dict


def setup_bot_news(context, page):
    context['bot_news'] = get_articles(2, 0, page, 0)  # type news, page = 0, count page = 2
    return context


def list_of_content(request, type, page=0, limit=0):
    base = {2: "/news/",
            3: "/articles/",
            4: "/for-partners/"
            }

    t = loader.get_template('news.html')
    if page is None:
        page = 0
    page = int(page)
    items_per_page = 10
    objects = get_articles(type, page, items_per_page, limit)
    tmp_c = setup_content_menu({}, type)
    tmp_c["content_objects"] = objects
    if page != 0:
        tmp_c["prev_page"] = base[type] + str(page - 1)

    if len(objects) == items_per_page:
        tmp_c["next_page"] = base[type] + str(page + 1)
    Dict = setup_custom_meta(request, tmp_c)

    c = Context(
        Dict
    )
    return HttpResponse(t.render(c))


def get_articles(type, page, count, greater):
    offset = page * count
    limit = offset + count
    objects = Articles.objects.filter(category_id=type, id__gt=greater).order_by("-pub_date")[offset:limit]
    link = "/news_article/"
    if type == 3:
        link = "/article/"
    if type == 4:
        link = "/article-partners/"
    for item in objects:
        item.link = link + str(item.url)
    return objects


def setup_content_menu(context, selected_menu):
    menu_list = None
    if selected_menu == 3:  ##it link to category table
        menu_list = [{"title": u"Новости", "url_item": "/news/"},
                    {"title": u"Статьи", "url_item": "/articles/", "current": 1},
                    {"title": u"Партнерам", "url_item": "/for-partners/"}]
        title = u""  # u"Zagu Статьи"
    if selected_menu == 2:
        menu_list = [{"title": u"Новости", "url_item": "/news/", "current": 1},
                    {"title": u"Статьи", "url_item": "/articles/"},
                    {"title": u"Партнерам", "url_item": "/for-partners/"}]
        title = u"Zagu Новости"
    if selected_menu == 4:
        menu_list = [{"title": u"Новости", "url_item": "/news/"},
                    {"title": u"Статьи", "url_item": "/articles/"},
                    {"title": u"Партнерам", "url_item": "/for-partners/", "current": 1}]
        title = u"Zagu партнерам"
    context["second_menu"] = menu_list
    context["pagetitle"] = title
    context = setup_bot_news(context, 2)
    context = setup_projects(context)
    return context


def setup_custom_meta(request, context, extra_meta=None):
    path = request.get_full_path()
    try:
        custom_meta = CustomMeta.objects.get(url=path)
        context["pagetitle"] = custom_meta.title
        context["description"] = custom_meta.meta_description
        context["keywords"] = custom_meta.meta_keyword
        if extra_meta:
            context['extra_meta'] = extra_meta
    except CustomMeta.DoesNotExist:
        pass
    return context
