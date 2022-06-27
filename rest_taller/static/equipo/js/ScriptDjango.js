const btnEliminacion = document.querySelectorAll('.btnEliminar');

(function(){

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click',function(e){
            let confirmacion=confirm("¿Confirma la eliminación del Docente?");
            if (!confirmacion){
                e.preventDefault();
            }
        })
    });


})