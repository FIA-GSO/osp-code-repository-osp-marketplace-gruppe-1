document.querySelectorAll('.event-date').forEach(el => {
    const text = el.textContent.trim();

    if (text) {
        const parts = text.split(' ');
        const date = new Date(parts[0]);

        if (!isNaN(date)) {
            const formattedDate = date.toLocaleDateString('de-DE');
            el.textContent = `${formattedDate} ${parts.slice(1).join(' ')}`;
        }
    }
});
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