function refreshMapCoordinates(lat, lon) {
    var map = document.getElementById("1");

    var new_map_src_1 = "https://www.openstreetmap.org/";
    var new_map_src_2 = "?mlat=" + lat + "&amp;mlon=" + lon;
    var new_map_src_3 = "#map=13/" + lat + "/" + lon;

    var new_map_src = new_map_src_1 + new_map_src_2 + new_map_src_3;

    document.getElementById("1").setAttribute("src", new_map_src)
}

function refreshMapPlace(place) {
    var map = document.getElementById("1");
    var req = new XMLHttpRequest();

    req.onreadystatechange = function () {
        if (req.readyState == 4 && req.status == 200){
            var resp_json = req.responseText;
            // var substr = resp_json.substring(
            //     resp_json.indexOf('=') + 1,
            //     resp_json.indexOf('&')
            // );
            console.log(resp_json);

            // let features = resp_json.features[0];
            // let lat = features['geometry'].coordinates[0];
            // let lon = features['geometry'].coordinates[1];

            let lat = resp_json[0].lat;
            let lon = resp_json[0].lon;

            refreshMapCoordinates(lat, lon);

            // var new_map_src_1 = "https://www.openstreetmap.org/";
            // var new_map_src_2 = "?mlat=" + lat + "&amp;mlon=" + lon;
            // var new_map_src_3 = "#map=13/" + lat + "/" + lon;
            //
            // var new_map_src = new_map_src_1 + new_map_src_2 + new_map_src_3;
            //
            // document.getElementById("1").setAttribute("src", new_map_src)
            // document.getElementById("1").setAttribute("src", req.responseText);

        }
    };

    var find_map = "https://nominatim.openstreetmap.org/?addressdetails=1&q=" + place + "&format=geojson&limit=1";
    req.open("GET", find_map, true);
    req.send();
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
