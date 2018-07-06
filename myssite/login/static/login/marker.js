var planes = "";
planes = {
  "places": [{
    "name": "Ciheul Technologies",
    "lat": "-6.894495",
    "lng": "107.629039",
    "address": "Jl. Sidomukti No.27, Sukaluyu,<br> Cibeunying Kaler, Kota Bandung,<br> Jawa Barat 40123"
  }, {
    "name": "Gedung Sate",
    "lat": "-6.902239",
    "lng": "107.61886",
    "address": "Jl. Diponegoro No.22, Citarum,<br> Bandung Wetan, Kota Bandung,<br> Jawa Barat 40115"
  }, {
    "name": "Institut Teknologi Bandung",
    "lat": "-6.890357",
    "lng": "107.610427",
    "address": "Jl. Ganesha No.10, Lb. Siliwangi,<br> Coblong, Kota Bandung,<br> Jawa Barat 40132"
  }, {
    "name": "Lapangan Gasibu",
    "lat": "-6.899950",
    "lng": "107.618688",
    "address": "Jalan Diponegoro, Citarum,<br> Bandung Wetan, Kota Bandung,<br> Jawa Barat 40115"
  }, {
    "name": "Lapangan Siliwangi",
    "lat": "-6.910108",
    "lng": "107.620099",
    "address": "Jl. Lombok No.10, Merdeka,<br> Sumur Bandung, Kota Bandung,<br> Jawa Barat 40113"
  }, {
    "name": "Cihampelas Walk Bandung",
    "lat": "-6.893416",
    "lng": "107.605305",
    "address": "Jalan Cihampelas No.160,<br> Cipaganti, Coblong, Kota Bandung,<br> Jawa Barat 40131"
  }, {
    "name": "Universitas Padjadjaran",
    "lat": "-6.926043",
    "lng": "107.774507",
    "address": "Jl. Raya Bandung Sumedang KM.21,<br> Hegarmanah, Jatinangor, Kabupaten Sumedang,<br> Jawa Barat 45363"
  }, {
    "name": "Alun Alun Kota Bandung",
    "lat": "-6.921751",
    "lng": "107.607094",
    "address": "Jl. Asia Afrika, Balonggede,<br> Regol, Kota Bandung,<br> Jawa Barat 40251"
  }, {
    "name": "Taman Makam Pahlawan Cikutra",
    "lat": "-6.892268",
    "lng": "107.635601",
    "address": "Jl. Cikutra, Neglasari,<br> Cibeunying Kaler, Kota Bandung,<br> Jawa Barat 40191"
  }, {
    "name": "Bandara Husein Sastranegara",
    "lat": "-6.903560",
    "lng": "107.580196",
    "address": "Jl. Pajajaran No.156,<br> Husen Sastranegara, Cicendo, Kota Bandung,<br> Jawa Barat 40174"
  }]
};
var map = L.map('mapid').setView([-6.894495, 107.629039], 11);
mapLink =
  '<a href="http://openstreetmap.org">OpenStreetMap</a>';
L.tileLayer(
  'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; ' + mapLink + ' Contributors',
    maxZoom: 20,
  }).addTo(map);

var i = "";
for (i in planes.places) {
  // (function(planes) {
    marker = new L.marker([planes.places[i].lat,planes.places[i].lng])
        .bindPopup("<b>"+planes.places[i].name+"</b>"+planes.places[i].address)
        .addTo(map);

    var myPopup = L.DomUtil.create('div','info');
    myPopup.innerHTML = "<div id='info'><p id='title'><b>" +planes.places[i].name+"</b></p>"+planes.places[i].address+ "</div>";
    marker.bindPopup(myPopup);
    var n,a = "";
    n = planes.places[i].name;
    a = planes.places[i].address;
    $('#info', myPopup).on('click', function() {
          $("#userTitle").html(n).html();
          $("#userAddr").html(a).html();
          // $("#userDetails").modal({
          //   inverted: true
          // });
          // $("#userDetails").modal("show");
        });
  // })
    (planes.places[i]);
}
