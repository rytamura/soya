from django.db import models
from django.contrib.gis.db import models
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import Point
from django.forms import ModelForm, HiddenInput

# Base admin border, rail, station Geo shapes

class Adm1920(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=14)
    begin    = models.CharField(max_length=10)
    end      = models.CharField(max_length=10)
    year     = 1920
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)

    def __str__(self):
        return self.pref + self.district + self.city

    @property
    def year(self):
        return 1920

# Auto-generated `LayerMapping` dictionary for Adm1920 model
Adm1920_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm1950(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=14)
    begin    = models.CharField(max_length=10)
    end      = models.CharField(max_length=10)
    year     = 1950
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm1950 model
Adm1950_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm1955(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=14)
    begin    = models.CharField(max_length=10)
    end      = models.CharField(max_length=10)
    year     = 1955
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm1955 model
Adm1955_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm1960(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=14)
    begin    = models.CharField(max_length=10)
    end      = models.CharField(max_length=10)
    year     = 1960
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm1960 model
Adm1960_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm1980(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=14)
    begin    = models.CharField(max_length=10)
    end      = models.CharField(max_length=10)
    year     = 1980
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm1980 model
Adm1980_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm1985(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=14)
    begin    = models.CharField(max_length=10)
    end      = models.CharField(max_length=10)
    year     = 1985
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm1985 model
Adm1985_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm1995(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=14)
    begin    = models.CharField(max_length=10)
    end      = models.CharField(max_length=10)
    year     = 1995
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm1995 model
Adm1995_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm2005(models.Model):
    pref     = models.CharField(max_length=8)
    sub_pref = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    city     = models.CharField(max_length=12)
    begin    = models.CharField(max_length=1)
    end      = models.CharField(max_length=1)
    year     = 2005
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm2005 model
Adm2005_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'begin': 'N03_005',
    'end': 'N03_006',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm2015(models.Model):
    pref     = models.CharField(max_length=10)
    sub_pref = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    city     = models.CharField(max_length=20)
    year     = 2015
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm2015 model
Adm2015_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class Adm2017(models.Model):
    pref     = models.CharField(max_length=10)
    sub_pref = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    city     = models.CharField(max_length=20)
    year     = 2017
    adm_code = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)


# Auto-generated `LayerMapping` dictionary for Adm2017 model
Adm2017_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

class RailroadSection2(models.Model):
    ctype           = models.CharField(max_length=1)
    rail_name       = models.CharField(max_length=28)
    company         = models.CharField(max_length=30)
    supplied_in     = models.CharField(max_length=4)
    operated_from   = models.CharField(max_length=4)
    operated_to     = models.CharField(max_length=4)
    relation_id     = models.CharField(max_length=10)
    transition_id   = models.CharField(max_length=1)
    transition_note = models.CharField(max_length=1)
    note            = models.CharField(max_length=40)
    relation_note   = models.CharField(max_length=21)

    geom = models.MultiLineStringField(srid=4612)


# Auto-generated `LayerMapping` dictionary for RailroadSection2 model
railroadsection2_mapping = {
    'ctype': 'N05_001', 
    'rail_name': 'N05_002',
    'company': 'N05_003',
    'supplied_in': 'N05_004',
    'operated_from': 'N05_005b',
    'operated_to': 'N05_005e',
    'relation_id': 'N05_006',
    'transition_id': 'N05_007',
    'transition_note': 'N05_008',
    'note': 'N05_009',
    'relation_note': 'N05_010',
    'geom': 'MULTILINESTRING',
}

class RailroadStation2(models.Model):
    ctype           = models.CharField(max_length=1)
    rail_name       = models.CharField(max_length=28)
    company         = models.CharField(max_length=30)
    supplied_in     = models.CharField(max_length=4)
    operated_from   = models.CharField(max_length=4)
    operated_to     = models.CharField(max_length=4)
    relation_id     = models.CharField(max_length=13)
    transition_id   = models.CharField(max_length=1)
    transition_note = models.CharField(max_length=10)
    note            = models.CharField(max_length=40)
    station_name    = models.CharField(max_length=35)

    geom = models.MultiPointField(srid=4612)

    def __str__(self):
        return self.station_name + "(" + self.rail_name +")"

# Auto-generated `LayerMapping` dictionary for Station2 model
railroadstation2_mapping = {
    'ctype': 'N05_001',
    'rail_name': 'N05_002',
    'company': 'N05_003',
    'supplied_in': 'N05_004',
    'operated_from': 'N05_005b',
    'operated_to': 'N05_005e',
    'relation_id': 'N05_006',
    'transition_id': 'N05_007',
    'transition_note': 'N05_008',
    'note': 'N05_009',
    'station_name': 'N05_011',
    'geom': 'MULTIPOINT',
}

## Geographical Features
class Feature(models.Model):
    name = models.CharField(max_length=128, verbose_name="場所の名前")
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    note = models.CharField(max_length=256, verbose_name="市町村名")

    geom = models.PointField(srid=4612)

    def __str__(self):
        return self.name

    def geocode(self):
        geolocator = Nominatim()
        loc = geolocator.geocode(address)

    @classmethod
    def create(cls, name, note, latitude, longitude):
        pt = Point(longitude, latitude)
        feat = cls(name=name, note=note, latitude=latitude, longitude=longitude, geom=pt)
        return feat

class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = ['name', 'note', 'latitude', 'longitude']
        widgets = {'longitude': HiddenInput(), 'latitude': HiddenInput(), 'note': HiddenInput()}

        

