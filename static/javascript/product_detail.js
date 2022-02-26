let detailBtns = document.querySelectorAll('.product-detail')
let name = document.querySelector('#product-detail-name')
let price = document.querySelector('#product-detail-price')
let img = document.querySelector('#product-detail-img')
let description = document.querySelector('#product-detail-description')
for (let i of detailBtns) {
    i.addEventListener('click', function () {
        let product = JSON.parse(this.dataset.product)

        name.textContent = product['name']
        price.textContent ='$'+product['price']
        description.textContent = product['description']
        img.src = product['image']
        countForm.dataset.product = product['product_id']

    })
}

// Product Control

let product_prices = document.querySelectorAll('.product-price')


for (let i of product_prices) {
    let discount = i.dataset.discount
    let price = i.dataset.price

    if (discount !== '') {
        let newPrice = parseFloat(i.dataset.discountprice).toFixed(2)
        i.innerHTML = `<span class="new-price new-price-2">$${newPrice}</span>
                        <span class="old-price">$${price}</span>
                         <span class="discount-percentage">-${discount}%</span>`

    }

}

// Action Buttons

let addCartBnts = document.querySelectorAll('.add-cart')

for (let i of addCartBnts ) {
    let quantity = parseInt(i.dataset.quantity)
    if (quantity <= 0) {
        i.classList.add('not-available')
        i.classList.remove('update-cart')
    }


}

// product mavjudligi
let product_available = document.querySelectorAll('.available')

for (let i of product_available) {
    let quantity = parseInt(i.dataset.quantity)
    // console.log('son>>>>>>>',quantity)

    if (quantity > 0) {
        i.classList.add('text-success')
        i.textContent = 'Now available'
    }
    else if (quantity === 0) {
        i.classList.add('text-danger')
        i.textContent = 'Not available'
    }
}


// Add-to-cart

let countForm = document.querySelector('.cart-quantity')
countForm.addEventListener('submit', function (event) {
    event.preventDefault()
    let product_id = this.dataset.product
    let count = this.querySelector('input').value

    if (user === 'AnonymousUser') {
        console.log('Saytga login qilinmagan')
    }
    else {
        add_cart(product_id, count)
    }


})

function add_cart(product_id, count) {
    let url = '/add-to-cart/'

    fetch(url, {

            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },

            body: JSON.stringify({'product_id': product_id, 'count': count})
        })

            .then(response => {
                return response.json()
            })

            .then(data => {
                console.log('Data:',data)
                location.reload()
            })

}



