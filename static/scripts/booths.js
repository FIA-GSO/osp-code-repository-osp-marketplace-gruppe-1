(function(){
    const eventSelect = document.getElementById('eventSelect');
    const boothStatusSelect = document.getElementById('boothStatusSelect');
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

    function showStatusUid(uid) {
        blocks.forEach(b => {
            if (!uid) {
                b.classList.remove('active');
            } else {
                b.classList.toggle('active', b.dataset.statusUid === uid);
            }
        });
    }

    eventSelect.addEventListener('change', e => {
        showUid(e.target.value);
    });
    boothStatusSelect.addEventListener('change', e => {
        showStatusUid(e.target.value);
    });
    showUid(eventSelect.value);
})();

document.querySelectorAll('.js-button').forEach(btn =>
    btn.addEventListener('click', async event => {
        event.preventDefault();
        boothId = btn.getAttribute('data-booth-id');
        action = btn.getAttribute('data-action');

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
