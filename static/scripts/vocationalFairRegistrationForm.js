document.querySelectorAll('.event-date-checkbox').forEach(el => {
    const dateString = el.textContent.trim();
    if (dateString) {
        const date = new Date(dateString);
        el.innerHTML = date.toLocaleDateString('de-DE');
    }
});

function selectEvent (eventCheckboxId){
    const checkbox = document.getElementById(eventCheckboxId);
    checkbox.checked = !checkbox.checked;
}