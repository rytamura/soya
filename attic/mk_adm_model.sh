python manage.py ogrinspect --srid=4612              shp/N03-200101_01-g_AdministrativeBoundary.shp --mapping --multi Border1921 >  model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-501001_01-g_AdministrativeBoundary.shp --mapping --multi Border1950 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-551001_01-g_AdministrativeBoundary.shp --mapping --multi Border1955 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-601001_01-g_AdministrativeBoundary.shp --mapping --multi Border1960 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-801001_01-g_AdministrativeBoundary.shp --mapping --multi Border1980 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-851001_01-g_AdministrativeBoundary.shp --mapping --multi Border1985 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-951001_01-g_AdministrativeBoundary.shp --mapping --multi Border1995 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-05_01-g_AdministrativeBoundary.shp     --mapping --multi Border2005 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-15_01_150101.shp                       --mapping --multi Border2015 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N03-17_01_170101.shp                       --mapping --multi Border2017 >> model.py
echo >> model.py

python manage.py ogrinspect --srid=4612 --no-imports shp/N05-16_RailroadSection2.shp --mapping --multi RailroadSection2 >> model.py
echo >> model.py
python manage.py ogrinspect --srid=4612 --no-imports shp/N05-16_Station2.shp --mapping --multi Station2 >> model.py
echo >> model.py

# DO NOT FORGET ADDING # -*- coding: utf-8 -*- AT THE BEGENNING OF THE FILE!!!


