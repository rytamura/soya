import os
from django.contrib.gis.utils import LayerMapping
from .models import *

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

Adm2015_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

Adm2017_mapping = {
    'pref': 'N03_001',
    'sub_pref': 'N03_002',
    'district': 'N03_003',
    'city': 'N03_004',
    'adm_code': 'N03_007',
    'geom': 'MULTIPOLYGON',
}

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

def main(klass, mapping, name, verbose=True):
    shp = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../shp', name)
    )
    lm = LayerMapping(
        klass, shp, mapping, 
        transform=True, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)


#main(Adm2017, Adm2017_mapping, "adm2017.shp")
#main(Adm2015, Adm2015_mapping, "adm2015.shp")
#main(Adm2005, Adm2005_mapping, "adm2005.shp")
main(Adm1995, Adm1995_mapping, "adm1995.shp")
main(Adm1985, Adm1985_mapping, "adm1985.shp")
main(Adm1980, Adm1980_mapping, "adm1980.shp")
main(Adm1960, Adm1960_mapping, "adm1960.shp")
main(Adm1955, Adm1955_mapping, "adm1955.shp")
main(Adm1950, Adm1950_mapping, "adm1950.shp")
main(Adm1920, Adm1920_mapping, "adm1920.shp")
main(RailroadSection2, railroadsection2_mapping, "railroad_section2.shp")
main(RailroadStation2, railroadstation2_mapping, "railroad_station2.shp")


