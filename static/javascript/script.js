window.addEventListener('DOMContentLoaded', function () {

    let update_CartBnts = document.querySelectorAll('.update-cart')
    let removeBnts = document.querySelectorAll('.remove-cart')


     for (let i of update_CartBnts) {
            i.addEventListener('click', function () {

                let product_id = this.dataset.product
                let action = this.dataset.action
                let cart = this.dataset.cart
                let url = null

                if (user === 'AnonymousUser') {
                    console.log('User topilmadi')

                } else {
                    if (cart === 'order') {
                        url = '/update_cart/'


                    } else if (cart === 'wishlist') {
                        url = '/update_wishlist/'


                    }
                    update_cart(product_id,action,url)

                }

            })
        }


    function update_cart(product_id,action,url) {
        console.log('Product id:',product_id,'action:',action,'url:',url)

         fetch(url, {

            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },

            body: JSON.stringify({'product_id': product_id, 'action': action})
        })

            .then(response => {
                return response.json()
            })

            .then(data => {
                console.log('Data:',data)
                location.reload()
            })



    }




    for (let i of removeBnts) {
        i.addEventListener('click',function () {
            let item_id = this.dataset.item

            remove_from_cart(item_id)
        })
    }

    function remove_from_cart (item_id) {

        let url = '/remove_from_cart/'

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body:JSON.stringify({'item_id': item_id})
        })
            .then(response => {
                return response.json()
            })

            .then(data => {
                console.log('Data',data)
                location.reload()

            })
    }



})

