(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation')

    Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {

        if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
        }

        form.classList.add('was-validated')
        }, false)
    })

    document.querySelectorAll('.event-date').forEach(el => {
        const dateString = el.textContent.trim();
        if (dateString) {
            const date = new Date(dateString);
            el.textContent = date.toLocaleDateString('de-DE');
        }
    });
})()
