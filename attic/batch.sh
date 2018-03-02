cd data
for f in `ls *.shp`; do
	shp2pgsql -W cp932 -s 4612 ${f} geo_${f%.*} > ${f%.*}.sql
done
cd ..

