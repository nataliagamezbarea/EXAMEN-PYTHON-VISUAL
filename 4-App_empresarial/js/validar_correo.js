$(document).ready(function(){
  $('#formulario-pago').submit(function(event){
    event.preventDefault();
    SendFormGoogleSheets();
  });
});

function validarCorreoElectronico(correo) {
  var regex = /^[a-zA-Z0-9._-]+@santjosepobrer\.es$/;
  return regex.test(correo);
}

function SendFormGoogleAppsScript() {
  $.ajax({
    url: 'https://script.google.com/macros/s/AKfycbzzNkxO2FENHO_g5WAMlgFLrq6JfUsM8b2fX6ReUruvilyni3IkxWCQCdsz3bU4p1weBg/exec',
    type: 'post',
    data: $('#formulario-pago').serialize(),
    success: function(){
      alert("Registro exitoso");
    },
    error: function(){
      alert("Error en el Registro :(");
    }
  });
}

function SendFormGoogleSheets() {
  var correo = $('#email').val();
  
  if (!validarCorreoElectronico(correo)) {
    alert("Por favor, ingresa un correo de dominio @santjosepobrer.es válido.");
    return;
  }

  SendFormGoogleAppsScript(); // Envía el formulario si el correo es válido
  "window.location.href = "nataliagamezbarea.github.io/EXAMEN-PYTHON-VISUAL/4-App_empresarial/3-Formulario_general.html";
}
