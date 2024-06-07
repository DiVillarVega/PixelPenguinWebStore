$(document).ready(function() {

   // Agregar método de validación para correo
   $.validator.addMethod("emailCompleto", function(value, element) {

    // Expresión regular para validar correo electrónico
    var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z\-0-9]{2,}))$/;

    // Validar correo electrónico con la expresión regular
    return regex.test(value);

  }, 'El formato del correo no es válido');

   // Validar formulario de login
   $('#formulario_login').validate(
    {
      rules: {
        correo: {
          required: true,
          emailCompleto: true,
          email: true
        },
        password: {
          required: true,
          minlength: 8,
          maxlength: 15,
        }
      },
      messages: {
        correo: {
          required: 'El correo es un campo obligatorio',
          emailCompleto: 'Ingrese un correo válido',
          email: 'Ingrese un correo válido'
        },
        password: {
          required: 'La contraseña es un campo requerido',
          minlength: 'La contraseña debe tener un mínimo de 8 caracteres',
          maxlength: 'La contraseña debe tener un máximo de 15 caracteres', 
        }
      }
    }
  );
});