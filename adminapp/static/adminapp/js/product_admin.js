let items = document.querySelectorAll('.delete-btn')
let modalText = document.querySelector('.modal-text')
let deleteConfirm = document.querySelector('#del-confirm')

items.forEach(item => {
    item.addEventListener('click', () => {
        let product = JSON.parse(item.dataset.product)
        modalText.innerHTML = `Delete item: <span class="text-danger ml-2">${product['name']}</span>`
        deleteConfirm.addEventListener('click', () => {
            product_delete(product['product_id'])
        })
    })
})

function product_delete(product_id) {
    let url = '/adminapp/product-delete/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'product_id': product_id})
        })
            .then(response => {
                return response.json()
            })

            .then(data => {
                console.log('Data',data)
                location.reload()

            })
}

// All check

let checkAll = document.querySelector('#all-check')
let product_check = document.querySelectorAll('.check__box')
checkAll.addEventListener('click', () => {
   product_check.forEach(item => {
       if (checkAll.checked) {
           item.checked = true
   }
       else if (!checkAll.checked) {
           item.checked = false
    }
   })
})



product_check.forEach(item => {

    item.addEventListener('click', () =>{
        if(count(product_check)) {
            checkAll.checked = true
        }
        else {
            checkAll.checked = false
        }
    })

})

function count(array) {
    let s = 0
    const len = array.length
    array.forEach(item => {
        s += item.checked
    })

    if(s === len) {
        return true
    }
    else {
        return false
    }
}

