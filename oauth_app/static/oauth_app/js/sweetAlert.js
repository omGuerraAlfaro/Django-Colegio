/* (function () {
    btnEliminacion.forEach((btn) => {
        btn.addEventListener("click", function (e) {
            e.preventDefault();
            //console.log(e.target.href)
            Swal.fire({
            title:'¿Cerrar Sesión?',
            text: '¿Está seguro?',
            icon: 'warning',
            showConfirmButton: true,
            cancelButtonText: 'No',
            confirmButtonText: 'Si',
            showCancelButton:true,
            timer: 100000,
            timerProgressBar: true,
            preConfirm:()=>{
                console.log("confirmado!")
                location.href = e.target.href
            },
            allowOutSideClick:()=>false,
            allowEscapeKey:()=>false,
        });
    });
        
});
 */



/* 
Swal.fire({
	// title:
	// text:
	// html:
	// icon:
	// confirmButtonText:
	// footer:
	// width:
	// padding:
	// background:
	// grow:
	// backdrop:
	// timer:
	// timerProgressBar:
	// toast:
	// position:
	// allowOutsideClick:
	// allowEscapeKey:
	// allowEnterKey:
	// stopKeydownPropagation:

	// input:
	// inputPlaceholder:
	// inputValue:
	// inputOptions:
	
	//  customClass:
	// 	container:
	// 	popup:
	// 	header:
	// 	title:
	// 	closeButton:
	// 	icon:
	// 	image:
	// 	content:
	// 	input:
	// 	actions:
	// 	confirmButton:
	// 	cancelButton:
	// 	footer:	

	// showConfirmButton:
	// confirmButtonColor:
	// confirmButtonAriaLabel:

	// showCancelButton:
	// cancelButtonText:
	// cancelButtonColor:
	// cancelButtonAriaLabel:
	
	// buttonsStyling:
	// showCloseButton:
	// closeButtonAriaLabel:


	// imageUrl:
	// imageWidth:
	// imageHeight:
	// imageAlt:
});
 */