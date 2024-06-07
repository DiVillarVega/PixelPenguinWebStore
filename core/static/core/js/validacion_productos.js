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

  // Validar formulario de productos
  $('#formulario_productos').validate(
    {
      rules: {
        id: {
          required: true,
          minlength: 1,
          maxlength: 5,
          soloNumeros: true
        },
        nombrep: {
          required: true,
          minlength: 1,
          maxlength: 60
        },
        descripcion: {
          required: true,
          minlength: 10,
          maxlength: 100
        },
        precio: {
          required: true,
          number: true,
          min: 0
        },
        descuentosub: {
          required: true,
          number: true,
          min: 0,
          max: 100
        },
        descuentoof: {
          required: true,
          number: true,
          min: 0,
          max: 100
        },
        categoria:{
          required: true
        }
      },
      messages: {  
        id: {
          required: "El ID es un campo requerido",
          minlength: 'El ID debe tener un mínimo de 1 caracteres',
          maxlength: 'El ID debe tener un máximo de 7 caracteres',
          soloNumeros: 'Ingrese solo números'
        },   
        nombrep: {
          required: 'El nombre es un campo requerido',
          minlength: 'El nombre debe tener un minimo de 1 caracter',
          maxlength: 'El nombre debe tener un máximo de 60 caracteres'
        },
        descripcion: {
          required: 'La descripción es un campo requerido',
          minlength: 'La descripción debe tener un mínimo de 10 caracteres',
          maxlength: 'La descripción debe tener un máximo de 50 caracteres'
        },
        precio: {
          required: 'El precio es un campo requerido',
          minlength: 'El precio debe tener un mínimo de 1 caracteres',
          maxlength: 'El precio debe tener un máximo de 7 caracteres',
          soloNumeros: 'Ingrese solo números',
          min: 'El precio debe ser mayor a 0'
        },
        descuentosub: {
          required: 'El descuento es un campo requerido',
          minlength: 'El descuento debe tener un mínimo de 1 caracteres',
          maxlength: 'El descuento debe tener un máximo de 5 caracteres',
          soloNumeros: 'Ingrese solo numeros y %',
          min: 'El descuento debe ser mayor a 0',
          max: 'El descuento debe ser menor a 100'
        },
        descuentoof: {
          required: 'El descuento es un campo requerido',
          minlength: 'El descuento debe tener un mínimo de 1 caracteres',
          maxlength: 'El descuento debe tener un máximo de 5 caracteres',
          soloNumeros: 'Ingrese solo numeros y %',
          min: 'El descuento debe ser mayor a 0',
          max: 'El descuento debe ser menor a 100'
        },
        categoria: {
          required: "La categoría es un campo requerido"
        },
      }
    }
  );
});