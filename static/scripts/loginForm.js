(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation')

    const emailInput = document.getElementById('email')
    const emailFeedback = emailInput.parentElement.querySelector('.invalid-feedback')

    Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {

        if(!emailInput.checkValidity()) {
            emailFeedback.textContent = 'Bitte geben Sie eine gültige E-Mail-Adresse an.'
        }

        if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
        }

        form.classList.add('was-validated')
        }, false)
    })
})()
