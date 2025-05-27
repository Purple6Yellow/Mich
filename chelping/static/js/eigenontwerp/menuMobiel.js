$(document).ready(function(){
    $('#menu').on('click', function(event){
       //alert('op menubalk geklikt')
        //#menu is het logo & #menuMobiel is div 
       event.stopPropagation();
        $('#menuMobiel').slideToggle();
    });
    $('body').on('click', function(event){
       //alert ('op body geklikt, menubalk verdwijnt')
        $('#menuMobiel').slideUp();
    });
    $('#menu').on('click', function(event){
        event.stopPropagation(); //Zorgt dat het niet sluit bij klikken op 
    });
});
