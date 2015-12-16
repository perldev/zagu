import shutil
import zipfile
import os
import sys
import mimetypes

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from main.models import ProductionSimpleCatalog, ImagesSimple, ProductionElecticSimple


class Command(BaseCommand):
    args = '<Stock Title ...>'
    help = 'every minute upload  one catalog from uploaded of it is existed'

    def handle(self, *args, **options):
        Item = None
        try:
            Item = ProductionSimpleCatalog.objects.filter(status="no")[:1][0]
        except:
            pass
        FileName = Item.filename
        print "reading %s" % (FileName)

        shutil.copyfile(FileName, "/tmp/catalog.zip")
        os.chdir("/tmp/")
        rf = zipfile.ZipFile("catalog.zip")
        # rf = rarfile.RarFile('catalog.zip')
        shutil.rmtree('Product')
        rf.extractall()
        read_catalog("Product", Item)
        Item.status = "yes"


def read_catalog(Start, Catalog):
    Ordering = 0
    ProductionElecticSimple.objects.filter(brand=Catalog.brand).delete()

    for path in os.listdir(Start):
        print path + ":"
        ImagesFromPdf = None
        TitleImage = None
        Object = None
        Ordering = Ordering + 1
        for PreItem in os.listdir(Start + "/" + path):
            item = Start + "/" + path + "/" + PreItem
            if ('application/pdf', None) == mimetypes.guess_type(item):
                print "pdf  - " + item
                ImagesFromPdf = read_image_from_pdf(Start + "/" + path, item)

            if ('text/plain', None) == mimetypes.guess_type(item):
                with open(item) as f:  # Use file to refer to the file object
                    Description = ""
                    MetaDescription = ""
                    for line in f:
                        line = line.decode('cp1251').encode('utf8')
                        Description = Description + "<p>"
                        Description = Description + line
                        MetaDescription = MetaDescription + line
                        Description = Description + "</p>"
                meta_keys = ",".join(MetaDescription.split())
                Object = ProductionElecticSimple(title=path,
                                                 text=Description,
                                                 meta_description=MetaDescription,
                                                 ordering=Ordering,
                                                 brand=Catalog.brand,
                                                 meta_keyword=meta_keys
                                                 )

            if ('image/jpeg', None) == mimetypes.guess_type(item):
                f = open(item)
                NewObject = ImagesSimple(order=0)

                NewObject.path.save(PreItem, File(f))
                NewObject.save()
                TitleImage = NewObject

        save_catalog_position(PreItem, Object, TitleImage, ImagesFromPdf)


def save_catalog_position(PreItem, Object, TitleImage, ImagesFromPdf):
    if Object is None:
        print "do not find any position %s " % (PreItem)
        return False

    Object.save()
    if TitleImage is not None:
        TitleImage.article = Object
        Object.thumb = TitleImage
        Object.save()

    if ImagesFromPdf is not None:
        for item in ImagesFromPdf:
            item.article = Object
            item.save()


def read_image_from_pdf(Path, FileName):
    pdf = file(FileName, "rb").read()
    startmark = "\xff\xd8"
    startfix = 0
    endmark = "\xff\xd9"
    endfix = 2
    i = 0
    njpg = 0
    Images = []
    while True:
        istream = pdf.find("stream", i)
        if istream < 0:
            break
        istart = pdf.find(startmark, istream, istream + 20)
        if istart < 0:
            i = istream + 20
            continue
        iend = pdf.find("endstream", istart)
        if iend < 0:
            raise Exception("Didn't find end of stream!")
        iend = pdf.find(endmark, iend - 20)
        if iend < 0:
            raise Exception("Didn't find end of JPG!")

        istart += startfix
        iend += endfix
        print "JPG %d from %d to %d" % (njpg, istart, iend)
        jpg = pdf[istart:iend]
        NewFileName = Path + "/jpg%d.jpg" % njpg
        jpgfile = file(NewFileName, "wb")
        jpgfile.write(jpg)
        jpgfile.close()
        Images.append(NewFileName)

        njpg += 1
        i = iend
    ImagesObjects = []
    ordering = 0
    for item in Images:
        ordering = ordering + 1
        f = open(item)
        NewObject = ImagesSimple(order=ordering)
        print str(f)
        Name = "%i.jpg" % (ordering)
        NewObject.path.save(Name, File(f))
        NewObject.save()
        ImagesObjects.append(NewObject)

    return ImagesObjects
