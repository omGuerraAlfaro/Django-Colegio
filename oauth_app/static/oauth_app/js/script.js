/* validacion form */
(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

function confirmarSesion(){
    var respuesta2 = confirm("¿Cerrar Sesion?");

    if(respuesta2 == true){
        alert("Sesion Cerrada!")
        return true;
    }else{
        alert("No se ha cerrado sesion")
        return false;
    }
}

function saltarA(id, tiempo) { //Funcion para ir a cualquier parte del sitio
    var tiempo = tiempo || 10; //Tiempo que tarda en reflejar la accion en ms; por defecto son 10ms
    console.log(tiempo)
    $("html, body").animate({ scrollTop: $(id).offset().top }, tiempo); //Se mueve hasta el inicio del id

  }





