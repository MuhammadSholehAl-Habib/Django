var planes = "";
planes = {
  "places" : [{
    "name" : "Ciheul Technologies",
    "lat" : "-6.894495",
    "lng" : "107.629039",
    "address" : "<br>Jl. Sidomukti No.27, Sukaluyu,<br> Cibeunying Kaler, Kota Bandung,<br> Jawa Barat 40123"
  },{
    "name" : "Gedung Sate",
    "lat" : "-6.902239",
    "lng" : "107.61886",
    "address" : "<br>Jl. Diponegoro No.22, Citarum,<br> Bandung Wetan, Kota Bandung,<br> Jawa Barat 40115"
  },{
    "name" : "Institut Teknologi Bandung",
    "lat" : "-6.890357",
    "lng" : "107.610427",
    "address" : "<br>Jl. Ganesha No.10, Lb. Siliwangi,<br> Coblong, Kota Bandung,<br> Jawa Barat 40132"
  }]
};
var map = L.map('mapid').setView([-6.894495, 107.629039], 10);
mapLink =
  '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
  'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; ' + mapLink + ' Contributors',
    maxZoom: 20,
  }).addTo(map);

var i = "";
for (i in planes.places) {
  marker = new L.marker([planes.places[i].lat,planes.places[i].lng])
      .bindPopup("<b>"+planes.places[i].name+"</b>"+planes.places[i].address)
      .addTo(map);
}
