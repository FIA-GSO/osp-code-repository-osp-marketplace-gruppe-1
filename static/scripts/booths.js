(function(){
    const eventSelect = document.getElementById('eventSelect');
    const boothStatusSelect = document.getElementById('boothStatusSelect');
    const donationSelect = document.getElementById('donationSelect');
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

    function showDonationUid(uid) {
        blocks.forEach(b => {
            if (!uid) {
                b.classList.remove('active');
            } else {
                b.classList.toggle('active', b.dataset.donationUid === uid);
            }
        });
    }

    eventSelect.addEventListener('change', e => {
        showUid(e.target.value);
    });
    boothStatusSelect.addEventListener('change', e => {
        showStatusUid(e.target.value);
    });
    donationSelect.addEventListener('change', e => {
        showDonationUid(e.target.value);
    });
    showUid(eventSelect.value);
})();
document.addEventListener('DOMContentLoaded', function() {
    const actionButtons = document.querySelectorAll('.js-button');

    actionButtons.forEach(btn =>
        btn.addEventListener('click', event => {
            event.preventDefault();
            boothId = btn.getAttribute('data-booth-id');
            action = btn.getAttribute('data-action');

            const accordionBody = btn.closest('.accordion-body');
            const statusContainer = accordionBody.querySelector('.js-status');

            fetch('/api/booths', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 'uid': parseInt(boothId), 'action': action }),
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Backend Error: ' + response.status);
                }
                return response.json(); 
            }).then(data => {
                if( data.status === 2 ) {
                    statusContainer.innerHTML = 'Abgelehnt';
                    statusContainer.classList.remove('text-success');
                    statusContainer.classList.add('text-danger');
                }
                else if( data.status === 3 ) {
                    statusContainer.innerHTML = 'Angenommen';
                    statusContainer.classList.remove('text-danger');
                    statusContainer.classList.add('text-success');
                }
            });
        })
    );
});