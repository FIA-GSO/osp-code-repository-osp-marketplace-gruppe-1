(function(){
    const select = document.getElementById('eventSelect');
    const blocks = document.querySelectorAll('.event-block');

    function showUid(uid) {
        blocks.forEach(b => {
            if (!uid) {
                b.classList.remove('active');
            } else {
                b.classList.toggle('active', b.dataset.uid === uid);
            }
        });
    }

    select.addEventListener('change', e => {
        showUid(e.target.value);
    });
    showUid(select.value);
})();

document.querySelectorAll('.js-button').forEach(btn =>
    btn.addEventListener('click', async event => {
        event.preventDefault();
        boothId = btn.getAttribute('data-booth-id');
        action = btn.getAttribute('action');

        response = '';

        if (action === 'accept') {
            response = await fetch('/api/booths', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 'action': action, 'uid': boothId }),
            });
        }
        else if (action === 'reject') {
            response = await fetch('/api/booths', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 'action': action, 'uid': boothId }),
            });
        }
    })
);

document.querySelectorAll('.event-date').forEach(el => {
    const dateString = el.textContent.trim();
    if (dateString) {
        const date = new Date(dateString);
        el.textContent = date.toLocaleDateString('de-DE');
    }
});
