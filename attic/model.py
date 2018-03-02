# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Border1921(models.Model):
    n03_001 = models.CharField(max_length=8)
    n03_002 = models.CharField(max_length=10)
    n03_003 = models.CharField(max_length=10)
    n03_004 = models.CharField(max_length=14)
    n03_005 = models.CharField(max_length=10)
    n03_006 = models.CharField(max_length=10)
    n03_007 = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4612)

    def __str__(self): return self.a


# Auto-generated `LayerMapping` dictionary for Border1921 model
border1921_mapping = {
    'n03_001': 'N03_001',
    'n03_002': 'N03_002',
    'n03_003': 'N03_003',
    'n03_004': 'N03_004',
    'n03_005': 'N03_005',
    'n03_006': 'N03_006',
    'n03_007': 'N03_007',
    'geom': 'MULTIPOLYGON',
}
