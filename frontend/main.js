let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = 'file:///C:/Users/User/Desktop/frontend/login.html'
})

let productsURL = 'http://127.0.0.1:8000/api/products/'

let getProducts = () => {
    fetch(productsURL)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildProducts(data)
    })
}

let buildProducts = (products) => {
    let productsWrapper = document.getElementById('products--wrapper')
    productsWrapper.innerHTML = ''
    for(let i = 0; products.length > i; i++){
        let product = products[i]
        
        let productCard = `
           <div class=product--card>
            <img src="http://127.0.0.1:8000${product.featured_image}">

            <div>
                <div class="card--header">
                    <h3>${product.title}</h3>
                    <strong class="vote--option" data-vote="Like" data-product=${product.id}>&#43</strong>
                    <strong class="vote--option" data-vote="Unlike" data-product=${product.id}>&#8722</strong>
                </div>
                <i>${product.vote_ratio}% Positive Feedback</i>
                <p> ${product.description.substring(0,150)}</p>
            </div>

           </div>`
        productsWrapper.innerHTML += productCard
    }
    addVoteEvents()
}


let addVoteEvents = () => {
    let voteButtons = document.getElementsByClassName('vote--option')

    for(let i = 0; voteButtons.length > i; i++){
        voteButtons[i].addEventListener('click', (e)=> {
            let token = localStorage.getItem('token')
            console.log('TOKEN:', token)
            let vote = e.target.dataset.vote
            let product = e.target.dataset.product
            
            fetch(`http://127.0.0.1:8000/api/products/${product}/vote/`, {
                method:'POST',
                headers: {
                    'Content-Type':'application/json',
                    Authorization:`Bearer ${token}`
                },
                body: JSON.stringify({'value':vote})

            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data)
                getProducts()
            })
        })
    }
}


getProducts()