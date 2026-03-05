(function(){
    const eventSelect = document.getElementById('eventSelect');
    const lectureStatusSelect = document.getElementById('lectureStatusSelect');
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
    lectureStatusSelect.addEventListener('change', e => {
        showStatusUid(e.target.value);
    });
    showUid(eventSelect.value);
})();

document.querySelectorAll('.js-button').forEach(btn =>
  btn.addEventListener('click', async event => {
    event.preventDefault();
    lectureId = btn.getAttribute('data-lecture-id');
    action = btn.getAttribute('data-action');

    response = '';

    if (action === 'accept') {
      response = await fetch('/api/lectures', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'action': action, 'uid': lectureId }),
      });
    }
    else if (action === 'reject') {
      response = await fetch('/api/lectures', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 'action': action, 'uid': lectureId }),
      });
    }
  })
);

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