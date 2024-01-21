/*function login(){ 
    event.preventDefault();var usuario  = document.getElementById("inputEmail1").value;var password = document.getElementById("inputContra1").value;
    
// alert("Usuario: "+usuario+", Password: "+password);

    console.log("Mensaje desde la consola: ");console.log("Usuario: "+usuario+", Password: "+password);

    if(usuario == ''){
        alert("El email no puede ir vacío");
    } else if (password == ''){
        alert("La contraseña no puede ir vacía");
    }
    else {
        document.getElementById("valido").submit();
    }
      
}
*/


function caracterLogin() {
    event.preventDefault();
    var id_correo = document.getElementById("inputEmail1").value;
    var id_pass = document.getElementById("inputContra1").value;

    var result1 = id_correo.includes("@");
    var result2 = id_correo.includes(".com"); 
    var result3 = id_correo.includes(".cl");

    var resultado_final_correo = false;
    var resultado_final_pass = false;

    var pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    
    if (result1 && (result2 || result3)) {
        resultado_final_correo = true;
    }

    if (id_pass.match(pass)) {
        resultado_final_pass = true;
    }

    if (resultado_final_correo && resultado_final_pass) {
        alert('Login exitoso.');
        document.getElementById("valido").innerHTML = "Válido";
        return true;
    } else {
        alert('Login incorrecto.');
        document.getElementById("valido").innerHTML = "Inválido";
        return false;
    }
}

function caracter_registrar (){
    event.preventDefault();
    //variables de los input
    var inputNombre = document.getElementById("inputName1").value;
    var inputApellido = document.getElementById("inputLastName1").value;
    var inputRut = document.getElementById("inputRut1").value;
    var inputDv = document.getElementById("inputDv1").value;
    var inputDire = document.getElementById("inputDireccion1").value;
    var inputCiudad = document.getElementById("inputCiudad1").value;
    var inputRegion = document.getElementById("inputRegion1").value;
    var inputEmail = document.getElementById("inputEmail2").value;
    var inputTel = document.getElementById("inputTelefono1").value;
    var inputCon = document.getElementById("inputPassword1").value;
    var inpuCond = document.getElementById("inputPassword2").value;

    //variables validación
    var resultado_rut = false;
    var resultado_dv1 = /^(?=.*\d|[kK]).{1}$/;
    var resultado_final_dv = false;
    var resultado_correo1 = inputEmail.includes("@");
    var resultado_correo2 = inputEmail.includes(".com"); 
    var resultado_correo3 = inputEmail.includes(".cl");
    var resultado_final_correo = false;
    var resultado_tel = /^.{8}$/;
    var resultado_final_tel = false;

    //Desarrollo de los If
    if(inputNombre == ''){
        alert("El nombre no puede estar vacío")
    }else if(inputApellido == ''){
        alert("El apellido no puede estar vacío")
        }

    if(isNaN(inputRut)){
        alert("Solo deben ingresarse números")
        resultado_rut = false;
    }else{
        resultado_rut = true;
    } 

    if(!inputDv.match(resultado_dv1)){
        alert("Ingrese sólo un número o una letra 'k' ")    
        resultado_final_dv = false;
    }else{
        resultado_final_dv = true;
    }

    if(inputDire == ''){
        alert("La dirección no puede estar vacía")
    }else if(inputCiudad == ''){
        alert("La ciudad no puede estar vacía")
    }else if(inputRegion == 'Seleccione...'){
        alert("Debe seleccionar una de las opciones")
    }

    if(resultado_correo1 && (resultado_correo2 || resultado_correo3)) {
        resultado_final_correo = true;
    }

    if(!inputTel.match(resultado_tel)){
        alert("Ingrese el número sin el +569")
        resultado_final_tel = false;
    }else{
        resultado_final_tel = true;
    }

    if(inputCon == '' && inpuCond == ''){
        alert("La contraseña no puede estar vacía")
    }else if(inputCon != inpuCond){
        alert("Las contraseñas no coinciden")
    }
    
    else{
        document.getElementById("validado").submit();
    }
}

function caracter_contacto(){
    event.preventDefault();
    //variables de los input
    var inputNombre = document.getElementById("inputNombre1").value;
    var inputEmail = document.getElementById("inputCorreo1").value;
    var inputTel = document.getElementById("inputTel1").value;
    var inputTipoCon = document.getElementById("inputCon").value;
    var inputConsu  = document.getElementById("inputArea1").value;

    //variables Validación
    var resultado_correo = /^(?=.*[@]).*\.(com|cl)$/i;
    var resultado_final_correo = false;
    var resultado_tel = /^.{8}$/;
    var resultado_final_tel = false;

    //Desarrollo de los If
    if(inputNombre == ''){
        alert("El nombre no puede estar vacío")
    }

    if(!inputEmail.match(resultado_correo)) {
        alert("No ha ingresado correctamente su correo")
        resultado_final_correo = false;
    }else{
        resultado_final_correo = true;
    }

    if(!inputTel.match(resultado_tel)){
        alert("Ingrese el número sin el +569")
        resultado_final_tel = false;
    }else{
        resultado_final_tel = true;
    }

    if(inputTipoCon == 'Seleccione...'){
        alert("Debe seleccionar una de las opciones")
    }else if (inputConsu == ''){
        alert("La consulta no puee estar vacía")
    }else{
        document.getElementById("ContactoForm").submit();
    }
}




