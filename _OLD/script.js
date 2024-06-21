// Copia los productos de index.html 20 veces

if (document.getElementById('mini_producto')) {

  var tarjeta = document.getElementById('mini_producto').outerHTML;

  var tarjetas = '';

  for (i = 0; i < 20; i++) {

      tarjetas = tarjetas + tarjeta;

  }

  document.getElementById('mini_producto').outerHTML = tarjetas;

}

// MENU PUBLICO

if (document.getElementById('menuP')) {

  fetch('menuPublico.html').then(response => {

      return response.text();

  }).then(htmlContent => {

  document.getElementById('menuP').innerHTML = htmlContent;

  window.scrollTo(0, 0);

  });

};

// MENU CLIENTES

if (document.getElementById('menuC')) {

  fetch('menuClientes.html').then(response => {

      return response.text();

  }).then(htmlContent => {

  document.getElementById('menuC').innerHTML = htmlContent;

  window.scrollTo(0, 0);

  });

};

// MENU ADMIN

if (document.getElementById('menuA')) {

  fetch('menuAdmin.html').then(response => {

      return response.text();

  }).then(htmlContent => {

  document.getElementById('menuA').innerHTML = htmlContent;

  window.scrollTo(0, 0);

  });

};

//BOTÓN COMPRAR (Lleva a ficha.html)
const btnComprar = document.getElementById('btnComprar');

if (btnComprar) {
  btnComprar.addEventListener('click', () => {
    window.location.href = 'ficha.html';
  });
}

// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()
