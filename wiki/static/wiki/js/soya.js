function makeFeatureLayer(urlstring){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var label = feature.properties.name.toString();
			layer.bindPopup(label);
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
			return {'color': feature.properties.ctype == 2 ? 'blue' : 'darkgreen', opacity:0.3};
		}
	});
};

var geojsonMarkerOptions = {
    radius: 6,
    fillColor: "#ff7800",
    color: "#000",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
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

function makeAdmLayer(urlstring, year, legend){
	return new L.GeoJSON.AJAX(urlstring, {
		onEachFeature: function(feature, layer){
			var label = feature.properties.city + ' (' + feature.properties.district + ')';
			layer.bindPopup(label);
		},
		attribution: legend,
		color: '#776655',
		fillOpacity: 0.0,
		weight:1
	});
};
