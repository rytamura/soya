var ic_doc24 = L.icon({
	iconUrl: '/static/wiki/image/doc24.png',
	iconSize: [24,24],
});

var ic_doc48 = L.icon({
	iconUrl: '/static/wiki/image/doc48.png',
	iconSize: [48,48],
});

var ic_doc24_unpub = L.icon({
	iconUrl: '/static/wiki/image/doc24_unpub.png',
	iconSize: [24,24],
});

var ic_doc48_unpub = L.icon({
	iconUrl: '/static/wiki/image/doc48_unpub.png',
	iconSize: [48,48],
});

var ic_loc24 = L.icon({
	iconUrl: '/static/wiki/image/loc24.png',
	iconSize: [24,24],
});

var ic_loc48 = L.icon({
	iconUrl: '/static/wiki/image/loc48.png',
	iconSize: [48,48],
});

var ic_photo24 = L.icon({
	iconUrl: '/static/wiki/image/photo24.png',
	iconSize: [24,24],
});

var ic_photo48 = L.icon({
	iconUrl: '/static/wiki/image/photo48.png',
	iconSize: [48,48],
});

var ic_photo24_unpub = L.icon({
	iconUrl: '/static/wiki/image/photo24_unpub.png',
	iconSize: [24,24],
});

var ic_photo48_unpub = L.icon({
	iconUrl: '/static/wiki/image/photo48_unpub.png',
	iconSize: [48,48],
});

function makeFeatureLayer(urlstring){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var label = feature.properties.name.toString();
			layer.bindPopup(label);
		},
		style: function(feature){
			return{'weight': 8, 'color': "red", 'opacity':0.3};
		}
	});
};

function makeSectionLayer(urlstring){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var label = feature.properties.rail_name.toString() + ' (' + feature.properties.company.toString() + ')';
			if (feature.properties.operated_to.toString() != "9999"){
				label = label + '<br />' + feature.properties.operated_from.toString() + ' - ' + feature.properties.operated_to.toString();
			} 
			layer.bindPopup(label);
		},
		style: function(feature){
			return {'weight':4, 'color': feature.properties.ctype == 2 ? 'blue' : 'darkgreen', 'opacity':0.3};
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

function makeStationLayer(urlstring){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var label = feature.properties.station_name.toString() + '駅 (' + feature.properties.rail_name.toString() + ')';
			if (feature.properties.operated_to.toString() != "9999"){
				label = label + '<br />' + feature.properties.operated_from.toString() + ' - ' + feature.properties.operated_to.toString();
			}
			layer.bindPopup(label);
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
    color: '#228852', 
    weight: 2,
    opacity: 0.7,
    fillOpacity: 0.0
};

function makeAdmLayer(urlstring, year, legend){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			layer.setStyle(defaultStyle);
			var label = feature.properties.city;
			if (feature.properties.district != ''){
				var label = label + ' (' + feature.properties.district + ')';
			}
			layer.bindPopup(label);
			layer.on('mouseover', function(e){
				layer.setStyle(highlightStyle);
			});
			layer.on('mouseout', function(e){
				layer.setStyle(defaultStyle);
			});		
		},
		
		attribution: legend,
	});
};



