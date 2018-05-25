var ic_doc24 = L.icon({
	iconUrl: '/wiki/image/doc24.png',
	iconSize: [24,24],
});

var ic_doc48 = L.icon({
	iconUrl: '/wiki/image/doc48.png',
	iconSize: [48,48],
});

var ic_doc24_unpub = L.icon({
	iconUrl: '/wiki/image/doc24_unpub.png',
	iconSize: [24,24],
});

var ic_doc48_unpub = L.icon({
	iconUrl: '/wiki/image/doc48_unpub.png',
	iconSize: [48,48],
});

var ic_loc24 = L.icon({
	iconUrl: '/wiki/image/loc24.png',
	iconSize: [24,24],
});

var ic_loc48 = L.icon({
	iconUrl: '/wiki/image/loc48.png',
	iconSize: [48,48],
});

var ic_photo24 = L.icon({
	iconUrl: '/wiki/image/photo24.png',
	iconSize: [24,24],
});

var ic_photo48 = L.icon({
	iconUrl: '/wiki/image/photo48.png',
	iconSize: [48,48],
});

var ic_photo24_unpub = L.icon({
	iconUrl: '/wiki/image/photo24_unpub.png',
	iconSize: [24,24],
});

var ic_photo48_unpub = L.icon({
	iconUrl: '/wiki/image/photo48_unpub.png',
	iconSize: [48,48],
});

function makeFeatureLayerWithLink(urlstring){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var coords = feature.geometry.coordinates.toString().split(",");
			var lat = coords[1];
			var lng = coords[0];
			var coords_str = '&lat='+lat+'&lng='+lng;
			// var period = Cookies.get('period');
			var label = feature.properties.name.toString();
			var linkstr = label+'<br /><a href="/wiki/create/article?feature='+label+coords_str+'" target="_new">この場所に関する記事を作成</a>';
			layer.bindPopup(linkstr);
		}
	});
};

function makeSectionLayerWithLink(urlstring){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var label1 = feature.properties.rail_name.toString() + ' (' + feature.properties.company.toString() + ')';
			if (feature.properties.operated_to.toString() != "9999"){
				var label2 = label1 + '<br />' + feature.properties.operated_from.toString() + ' - ' + feature.properties.operated_to.toString();
			}
			else {
				label2 = label1;
			}
			var linkstr = label2 + '<br /><a href="/wiki/create/article?section=' + feature.properties.rail_name.toString() + '" target="_new">この路線に関する記事を作成</a>';
			layer.bindPopup(linkstr);
		},
		style: function(feature){
			return {'weight':4, 'color': feature.properties.ctype == 2 ? 'blue' : 'darkgreen', opacity:0.3};
		}
	});
};

var geojsonMarkerOptions = {
    radius: 4,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.32
};

function mklink_station(coords_str, station_name){
	var period = $('#period').val();
	var linkstr = label2 + '<br /><a href="/wiki/create/article?period='+period+'?station='+station_name+coords_str+'" target="_new">この駅に関する記事を作成</a>';
	return linkstr;
};

function makeStationLayerWithLink(urlstring){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var label1 = feature.properties.station_name.toString() + '駅';
			if (feature.properties.operated_to.toString() != "9999"){
				var label2 = label1 + '<br />' + feature.properties.operated_from.toString() + ' - ' + feature.properties.operated_to.toString();
			}
			else {
				label2 = label1;
			}
			// console.log(coords);
			var coords = feature.geometry.coordinates.toString().split(",");
			var lat = coords[1];
			var lng = coords[0];
			var coords_str = '&lat='+lat+'&lng='+lng;
			var station_name = feature.properties.station_name.toString();
			var linkstr = label2 + '<br /><a href="/wiki/create/article?station='+feature.properties.station_name.toString()+coords_str+'" target="_new">この駅に関する記事を作成</a>';
			layer.bindPopup(linkstr);
		},
		pointToLayer: function (feature, latlng) {
        	return L.circleMarker(latlng, geojsonMarkerOptions);
	    }
	});
};

var defaultStyle = {
    color: '#888888', 
    weight: 0.5,
    opacity: 0.6,
    fillOpacity: 0.0
};

var highlightStyle = {
    color: '#2262CC', 
    weight: 2,
    opacity: 0.7,
    fillOpacity: 0.0
};
function makeAdmLayerWithLink(urlstring, year, legend){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			layer.setStyle(defaultStyle);
			layer.on('click', function(e){
				var latlng = e.latlng;
				var label1 = feature.properties.city;
				if (feature.properties.district != ''){
					var label2 = label1 + ' (' + feature.properties.district + ')';
				}
				else {
					label2 = label1;
				}
				var coords_str = '&lat='+latlng.lat+'&lng='+latlng.lng
				var linkstr = label2 + '<br /><a href="/wiki/create/article?adm='+label1 + '" target="_new">'+label1+'に関する記事を作成</a>';
				// linkstr = linkstr + '<br /><a href="/wiki/create/article?adm='+label1+ coords_str + '" target="_new">この場所に関する記事を作成</a>';
				linkstr = linkstr + '<br /><a data-fancybox data-type="iframe" data-src="/wiki/create/feature?adm='+label1+ coords_str + '">この場所を地図に新規登録</a>';
				layer.bindPopup(linkstr).openPopup();
			});
			layer.on('mouseover', function(e){
				layer.setStyle(highlightStyle);
			});
			layer.on('mouseout', function(e){
				layer.setStyle(defaultStyle);
			});
		},
		attribution: legend
	});
};
