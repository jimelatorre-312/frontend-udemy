const formulario = document.getElementById("formulario");
formulario.addEventListener("submit", (e) => {
  e.preventDefault();
  const email = document.getElementById("email");
  const name = document.getElementById("name");
  const password = document.getElementById("password");
  const passwordVerificar = document.getElementById("passwordVerificar");

  if (validator.isEmail(email.value) == false) {
    alert("Se ha ingresado incorrectamente el email");
    return;
  }
  if (validator.isAlpha(name.value) == false) {
    alert("Se ha ingresado incorrectamente el nombre");
    return;
  }
  if (validator.isStrongPassword(password.value) == false) {
    alert("Se ha ingresado incorrectamente la contraseña");
    return;
  }
  if (validator.equals(passwordVerificar.value, password.value) == false) {
    alert("Se ha ingresado incorrectamente la contraseña de verificación");
    return;
  }
});
