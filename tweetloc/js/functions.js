var map;
var marker;

var nominatimUrl = 'https://nominatim.openstreetmap.org/?addressdetails=1&q=PLACE&format=json&limit=1'

function initMap() {
    map = L.map('map');
    map.setView([51.505, -0.09], 13);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
		maxZoom: 18,
		attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
			'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
			'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: -1
	}).addTo(map);
}

function refreshMapCoordinates(lat, lon) {
	if (marker) { map.removeLayer(marker) }
	map.setView([lat, lon], 13);
    map.flyTo(new L.latLng(lat, lon));
    marker = L.marker([lat, lon]).addTo(map);
}

function refreshMapPlace(place) {
	console.log(place);
    place = place.replace(',', '');
    place = place.replace(' ', '+');
    var url = nominatimUrl.replace('PLACE', place);
    console.log(url);

    fetch(url, {
        method: 'GET',
    }).then((response) => {
        return response.json();
    }).then((data) => {
        data = data[0];
        var lat = data.lat;
        var lon = data.lon;
        if (marker) { map.removeLayer(marker) }
        map.setView([lat, lon], 13);
        map.flyTo(new L.latLng(lat, lon));
        marker = L.marker([lat, lon]).addTo(map);
    });
}

function comprobarFormulario(form) {
    query = form.query.value; 
    if (query.lenght === 0 || !query.trim()) {
        $('.toast').toast('show');
        window.alert("La búsqueda no puede estar vacía.");
    }
    else {
       form.submit();
    }
}

initMap();
