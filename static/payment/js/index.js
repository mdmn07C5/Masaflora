var stripe = Stripe('pk_test_51ONer8G7zBYX1q0bSklHAsYsrqIHo4cou2qbl63eGl1hEOCoe1CjsW8t2HVs2wFCEBub7800onDWIuEK1GVEpByC000MEzgQO8')

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        lineHeight: '2.4',
        fontSize: '16px',
    }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");


card.on('change', function (e) {
    var displayError = document.getElementById('card-errors');
    if (e.error) {
        displayError.textContent = e.error.message;
        $('#card-errors').addClass('alert alert-info');
    } else {
        displayError.textContent = 'asdfsadf';
        $('#card-errors').removeClass('alert alert-info');
    }
});

var form = document.getElementById('payment-form')

form.addEventListener('submit', function(e) {
    e.preventDefault();

    var custName = document.getElementById("custName").value;
    var custAdd = document.getElementById("custAdd").value;
    var custAdd2 = document.getElementById("custAdd2").value;

    stripe.confirmCardPayment(clientsecret, {
        payment_method: {
            card: card,
            billing_details: {
                address: {
                    line1: custAdd,
                    line2: custAdd2
                },
                name: custName
            },
        }
    }).then(function(result) {
        if (result.error) {
            console.log('payment error');
            console.log(result.error.message);
        } else {
            // There's a risk of the customer closing the browser before callback execution.
            // Set up webhook or plugin to listen for the payment_intent.succeeded event 
            // that handles any business critical post-payment actions. 
            if (result.paymentIntent.status === 'succeeded') {
                console.log('payment processed');
                // for now, we do memes.
                window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
            }
        }
    });
});