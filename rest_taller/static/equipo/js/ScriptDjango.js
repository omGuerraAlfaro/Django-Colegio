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

window.addEventListener('load', () => {
    //ubicacion por ciudad especifica
    const url = `http://127.0.0.1:8000/api/lista_taller`
    fetch(url)
        .then(response => { return response.json() })
        .then(data => {
            for(let i of data){
                console.log(i);
            } //datos primera API "openweathermap"
        })
        .catch(error => {
            console.log(error)
        })
})

//