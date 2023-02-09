from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D


def gen_ad(request):
    ad_1 = Post(title='Bhadaj', description='This is an example ad 1.', price=100.0, location='POINT(72.4816186 23.0868134)')
    ad_2 = Post(title='Shela', description='This is an example ad 1.', price=100.0, location='POINT(72.4360767 23.0016994)')
    ad_3 = Post(title='Naroda', description='This is an example ad 1.', price=100.0, location='POINT(72.6356151 23.069078)')
    ad_4 = Post(title='Kathwada', description='This is an example ad 1.', price=100.0, location='POINT(72.6743584 23.0455028)')
    ad_5 = Post(title='Aslali', description='This is an example ad 1.', price=100.0, location='POINT(72.5833572 22.9488857)')
    ad_6 = Post(title='Maninagar', description='This is an example ad 1.', price=100.0, location='POINT(72.5956249 22.9927378)')
    ad_7 = Post(title='Bapunagar', description='This is an example ad 1.', price=100.0, location='POINT(72.6110299 23.033986)')
    ad_8 = Post(title='Sanand', description='This is an example ad 1.', price=100.0, location='POINT(72.369606 22.991901)')
    ad_9 = Post(title='Adalaj', description='This is an example ad 1.', price=100.0, location='POINT(72.5701652 23.1713412)')
    ad_10 = Post(title='Changodar', description='This is an example ad 1.', price=100.0, location='POINT(72.4215529 22.9200145)')
    
    ad_1.save()
    ad_2.save()
    ad_3.save()
    ad_4.save()
    ad_5.save()
    ad_6.save()
    ad_7.save()
    ad_8.save()
    ad_9.save()
    ad_10.save()

    return HttpResponse("<h1>Data added to database</h1>")

def index(request):
    user_location = Point(72.517031, 23.070391)
    nearby_ads = Post.objects.filter(location__distance_lte=(user_location, D(km=15)))
    print(nearby_ads)
    if len(nearby_ads) == 0:
        return HttpResponse("No ads near you")
    return HttpResponse(nearby_ads)