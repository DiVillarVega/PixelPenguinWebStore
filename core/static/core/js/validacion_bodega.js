$(document).ready(function() {
  
  // Agregar método de validación para que un campo sólo acepte 
  // letras y espacios en blanco, pero no números ni símbolos,
  // ideal para campos como nombres y apellidos
  $.validator.addMethod("soloLetras", function(value, element) {

    return this.optional(element) || /^[a-zA-Z\s]*$/.test(value);

  }, "Sólo se permiten letras y espacios en blanco.");


  // Validar Números con % como descuentos pa
  $.validator.addMethod("soloNumeros", function(value, element) {

    return this.optional(element) || /^[0-9]+%*$/.test(value);

  }, "Sólo se permiten números.");

  // Validar formulario de bodega
  $('#formulario_bodega').validate(
    {
      rules: {
        categoria:{
          required: true
        },
        cantidad: {
          required: true,
          min: 1
        },
        titulo: {
          required: true,
          minlength: 1,
          maxlength: 60
        }
      },
      messages: {
        categoria: {
          required: "La categoría es un campo requerido."
        },
        cantidad: {
          required: "La cantidad es un campo requerido.",
          min: "La cantidad debe ser mayor a 0."
        },
        titulo: {
          required: "El título es un campo requerido.",
          minlength: "El título debe tener un mínimo de 1 caracter.",
          maxlength: "El título debe tener un máximo de 60 caracteres."
        }
      }
    }
  );
});