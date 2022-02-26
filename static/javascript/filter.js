let inputs = document.querySelector('.filter').querySelectorAll('input')
let form = document.querySelector('#filter-form')
inputs.forEach(checkbox => {
    checkbox.addEventListener('click', (e) => {
        filter(checkbox.value)

    })
})

function filter(value) {
    let url = '/filter-result/'
    fetch(url, {

    })
}
