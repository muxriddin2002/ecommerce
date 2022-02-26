let shipping_form = document.querySelector('#shipping-form')


shipping_form.addEventListener('submit', function (event) {
    event.preventDefault()

    if (user === 'AnonymousUser') {
        console.log('Foydalanuvchi topilmadi!!')
    } else {
        submitForm()
    }

})

function submitForm () {
    let url = '/check_process/'

    let shipping_info = {
        'adress': shipping_form.adress.value,
        'city': shipping_form.city.value,
        'state': shipping_form.state.value,
        'zip_code': shipping_form.zip_code.value,
        'phone_number': shipping_form.phone_number.value,
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'shipping':shipping_info})
    })

    .then(response => response.json())

    .then(data => {
        console.log('Bajarilgan holati:',data)
        if (data === 'true') {
            alert('Buyurtma muvaffaqiyatli amalga oshrildi!')
            window.location.href = home_location
        }


    })

}