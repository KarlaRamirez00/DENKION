var i = 0;
var imagenes = ["/static/administrador/img/fondo_tocadiscos.jpg", "/static/administrador/img/fondo_receiver.jpg", "/static/administrador/img/fondo_radio.jpg"]
var imagen = document.getElementById("imagenf");

function cambioimg (){
    imagen.style.opacity = 0.75;

    setTimeout(function(){
        imagen.src = imagenes[i];
        imagen.style.opacity = 1;
        i = (i+1) % imagenes.length;
    },120);
}

function nuevaimg(){
    cambioimg ()
    setInterval(cambioimg,3000);
}

window.onload = function(){
    nuevaimg();
};