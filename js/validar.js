function login(){ 
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

function registrar(){
    event.preventDefault(); //Sirve para prevenir el comportamiento por defecto 
    //Tomar cada variable del registro 
    var nombre = document.getElementById("inputName1").value;
    var apellido = document.getElementById("inputLastName1").value;
    var rut = document.getElementById("inputRut1").value;
    var dv = document.getElementById("inputDv1").value;
    var dire = document.getElementById("inputDireccion1").value;
    var ciudad = document.getElementById("inputCiudad1").value;
    var region = document.getElementById("inputRegion1").value;
    var correo = document.getElementById("inputEmail2").value;
    var tele = document.getElementById("inputTelefono1").value;
    var pass1 = document.getElementById("inputPassword1").value;
    var pass2 = document.getElementById("inputPassword2").value;

    //Crear mensaje visible en la consola, para ver si registra todo ok. (Esto es al inspeccionar)
    console.log("Mensaje desde la consola: ");
    console.log("Nombre: "+nombre+", Apellido: "+apellido+", Rut: "+rut+", Dv: "+dv+", Dirección: "+dire+", Ciudad: "+ciudad+",Región: "+region+"Correo: "+correo+"Teléfono: "+tele+"Contraseña 1: "+pass1+"Contraseña 2: "+pass2);

    //Validar con los if, que exista algún caracter dentro de las variables
    if(nombre == ''){
        alert("El nombre no puede estar vacío.");
    }else if(apellido == ''){
        alert("El apellido no puede estar vacío.");
    }else if(rut == ''){
        alert("El rut no puede estar vacío.");
    }else if(dv == ''){
        alert("El dígito verificador no puede estar vacío.");
    }else if(dire == ''){
        alert("La dirección no puede estar vacía.");
    }else if(ciudad == ''){
        alert("La ciudad no puedes estar vacía.");
    }else if(region == 'Seleccione...'){
        alert("Debe seleccionar una región.")
    }else if(correo == ''){
        alert("El correo no puede estar vacío.");
    }else if(tele == ''){
        alert("El teléfono no puede estar vacío.");
    }else if(pass1 == ''){
        alert("La contraseña no puede estar vacía.");
    }else if(pass2 == ''){
        alert("La contraseña no puede estar vacía");
    }else{
        document.getElementById("validado").submit();
    }
}

function contacto(){
    event.preventDefault(); //Sirve para prevenir el comportamiento por defecto 
    //Tomar cada variable del formulario de contacto 
    var Nombre = document.getElementById("inputNombre1").value;
    var Correo = document.getElementById("inputCorreo1").value;
    var Telefono = document.getElementById("inputTel1").value;
    var TipoCons = document.getElementById("inputCon").value;
    var Consulta = document.getElementById("inputArea1").value;

    //Crear mensaje visible en la consola, para ver si está todo ok. (Esto es al inspeccionar)
    console.log("Mensaje desde la consola: ");
    console.log("Nombre: "+Nombre+", Correo: "+Correo+", Telefono: "+Telefono+", Tipo Consulta: "+Consulta);


//Validar con los if, que exista algún caracter dentro de las variables
if(Nombre == ''){
    alert("El nombre no puede estar vacío.");
}else if(Correo == ''){
    alert("El correo no puede estar vacío.");
}else if(Telefono == ''){
    alert("El teléfono no puede estar vacío");
}else if(TipoCons =='Seleccione...'){
    alert("Debe seleccionar un tipo de consulta");
}else if(Consulta == ''){
    alert("La consulta no puede estar vacía");
}else{
    document.getElementById("ContactoForm").submit();
}
}