(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation')

    const emailInput = document.getElementById('email')
    const emailFeedback = emailInput.parentElement.querySelector('.invalid-feedback')

    const repeatedEmailInput = document.getElementById('repeatedemail')
    const repeatedEmailFeedback = repeatedEmailInput.parentElement.querySelector('.invalid-feedback')

    const passwordInput = document.getElementById('password')
    const passwordFeedback = passwordInput.parentElement.querySelector('.invalid-feedback')

    const repeatedPasswordInput = document.getElementById('repeatedpasssword')
    const repeatedPasswordFeedback = repeatedPasswordInput.parentElement.querySelector('.invalid-feedback')

    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z\d]).{8,}$/

    Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {

      repeatedEmailInput.setCustomValidity('')
      passwordInput.setCustomValidity('')
      repeatedPasswordInput.setCustomValidity('')

      if(!emailInput.checkValidity()) {
        emailFeedback.textContent = 'Bitte geben Sie eine gültige E-Mail-Adresse an.'
      }
      if(!repeatedEmailInput.checkValidity()) {
        repeatedEmailFeedback.textContent = 'Bitte geben Sie eine gültige E-Mail-Adresse an.'
      }
      if (emailInput.checkValidity() && repeatedEmailInput.checkValidity() && emailInput.value !== repeatedEmailInput.value) {
        repeatedEmailInput.setCustomValidity('Die eingegebenen E-Mail-Adressen stimmen nicht überein.')
        repeatedEmailFeedback.textContent = 'Die eingegebenen E-Mail-Adressen stimmen nicht überein.'
      }
      if (!passwordRegex.test(passwordInput.value)) {
        passwordInput.setCustomValidity('Mind. 8 Zeichen inkl. Groß-, Kleinbuchstaben, Zahl und Sonderzeichen.')
        passwordFeedback.textContent = 'Mind. 8 Zeichen inkl. Groß-, Kleinbuchstaben, Zahl und Sonderzeichen.'
      }
      if (passwordRegex.test(passwordInput.value) && passwordInput.value !== repeatedPasswordInput.value) {
        repeatedPasswordInput.setCustomValidity('Die eingegebenen Passwörter stimmen nicht überein.')
        repeatedPasswordFeedback.textContent = 'Die eingegebenen Passwörter stimmen nicht überein.'
      }

      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
    })
})()
