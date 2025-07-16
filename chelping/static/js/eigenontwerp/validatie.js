document.getElementById('verzendknop').addEventListener('click', function() {
    // Hier komt de code die moet worden uitgevoerd wanneer op de knop wordt geklikt
    console.log('De verzendknop is geklikt!');
    //alert('validatie_WW.js is geactiveerd')
    console.log('tot hier: 1')
// GEGEVENS 
    const A = document.getElementById('naam');
    const B = document.getElementById('email').value;
    const C = document.getElementById('telefoon');
    const D = document.getElementById('leeftijd').value;
    const E = document.getElementById('niveau').value;
    const F = document.getElementById('training').value;
    const A1 = A.value
    const C1 = C.value
    //alert(A1)
    //aantaltekens = A1.length
    //alert(aantaltekens)
    //alert(B)
// DATUM
    const vandaag = new Date();
    const jaar = vandaag.getFullYear();
    const maand = String(vandaag.getMonth()+1).padStart(2,'0'); // Maand is 0-gebaseerd, dus +1
    const dag = String(vandaag.getDate()).padStart(2,'0'); // Zorgt voor 2 cijfers, bijvoorbeeld '01'
    const vandaag1 =  (dag + "-" + maand + "-" + jaar ) 
    //alert (dag + "-" + maand + "-" + jaar )
    //  alert(vandaag1)
    console.log('tot hier: 2')
// VOORWAARDEN
    if (A1.length <= 1){
            alert('Uw naam is niet volledig geschreven')}
        else if (!B.includes("@")){
            alert ('Uw emailadres is niet correct')}
        else if (!C.length ==10){
            alert ('Uw telefoonnummer klopt niet, het nummer bevat maar ' + C.length + 'cijfers')}
}); 

