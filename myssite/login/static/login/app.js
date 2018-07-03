var mymap = L.map('mapid').setView([51.505, -0.09], 6);
L.tileLayer('https://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution : '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);
