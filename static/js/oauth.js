var elm = document.getElementById('Token');
var sender = document.getElementById('token-field');
var urlHash = document.location.hash;
var token = urlHash.split('&')[0].split('=')[1];

elm.innerHTML = token;
sender.value = token;