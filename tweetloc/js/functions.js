function refreshMapCoordinates(lat, lon) {
    var map = document.getElementById("1");

    var new_map_src_1 = "https://maps.google.com/maps?width=100%&height=600&hl=en";
    var new_map_src_2 = "&q=" + lat + ',' + lon;
    var new_map_src_3 = "&ie=UTF8&t=&z=14&iwloc=B&output=embed";

    var new_map_src = new_map_src_1 + new_map_src_2 + new_map_src_3;

    document.getElementById("1").setAttribute("src", new_map_src)
}

function refreshMapPlace(place) {
    var map = document.getElementById("1");

    var new_map_src_1 = "https://maps.google.com/maps?width=100%&height=600&hl=en";
    var new_map_src_2 = "&q=" + place;
    var new_map_src_3 = "&ie=UTF8&t=&z=14&iwloc=B&output=embed";

    var new_map_src = new_map_src_1 + new_map_src_2 + new_map_src_3;

    document.getElementById("1").setAttribute("src", new_map_src)
}

function comprobarFormulario(form) {
    query = form.query.value; 
    if (query.lenght === 0 || !query.trim()) {
        window.alert("La búsqueda no puede estar vacía.");
    }
    else {
       form.submit();
    }
}
