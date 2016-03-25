$(document).ready(function(){
    $("#contenido").load("{% url "homepage" %}");
    $("#tipuser").click(function(){
        $("#contenido").load("{% url 'perfil_app:tipo' %}");
    });
    $("#saludo2").click(function(){
     $("#contenido").load("/perfil/saludo2/");
    });
});
