let p = document.getElementById('amount_at_end');
let button = document.getElementById('submit');

button.addEventListener('click', async (e) => {
    e.preventDefault();

    const res = await request({url: 'credit', body: {
        amount_at_start: document.getElementById('amount_at_start').value,
        deposit_percent: document.getElementById('deposit_percent').value,
        ages: document.getElementById('ages').value,
        inflation_rate: document.getElementById('inflation_rate').value,
    }, headers:{
        'X-CSRFToken': csrf_token,
    }});

    console.log(res);
    console.log(JSON.parse(res));

    p.innerHTML = JSON.parse(res).amount_at_end;
})