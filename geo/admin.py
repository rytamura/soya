from django.contrib import admin
from django.contrib.gis import admin

from geo.models import Adm1920, Adm1950, Adm1955, Adm1960, Adm1980, Adm1995, Adm2005, Adm2015, Adm2017, RailroadSection2, RailroadStation2, Feature
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
#admin.site.register(Adm1920, LeafletGeoAdmin)
#admin.site.register(Adm1950, LeafletGeoAdmin)
#admin.site.register(Adm1955, LeafletGeoAdmin)
#admin.site.register(Adm1960, LeafletGeoAdmin)
#admin.site.register(Adm1980, LeafletGeoAdmin)
#admin.site.register(Adm1995, LeafletGeoAdmin)
#admin.site.register(Adm2005, LeafletGeoAdmin)
#admin.site.register(Adm2015, LeafletGeoAdmin)
#admin.site.register(Adm2017, LeafletGeoAdmin)
#admin.site.register(RailroadStation2, LeafletGeoAdmin)
#admin.site.register(RailroadSection2, LeafletGeoAdmin)

class Adm1920Admin(LeafletGeoAdmin):
	search_fields = ['city']
	list_filter = ('city', )

class RailroadStation2Admin(LeafletGeoAdmin):
	search_fields = ['rail_name', 'station_name',]
	list_filter = ('rail_name', 'station_name')

#admin.site.register(Adm1920, Adm1920Admin)
#admin.site.register(RailroadStation2, RailroadStation2Admin)

class FeatureAdmin(LeafletGeoAdmin):
	search_fields = ['name', 'address',]
	list_filter = ('name',)

admin.site.register(Feature, FeatureAdmin)

#https://www.google.co.jp/maps/place/学校法人稚内北星学園/@45.3828072,141.7157338,17z/data=!3m1!4b1!4m5!3m4!1s0x5f103b2edc29ef1d:0x6215a5a47cb6f338!8m2!3d45.3828035!4d141.7179225