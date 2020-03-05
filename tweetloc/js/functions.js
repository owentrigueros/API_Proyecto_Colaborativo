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

    var new_map_src = "https://nominatim.openstreetmap.org/search?q=" + place;

    document.getElementById("1").setAttribute("src", new_map_src)
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
