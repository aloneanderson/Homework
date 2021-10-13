let submit = document.getElementById('submit_id');
let content = document.getElementById('content');

function search(items) {
    content.innerHTML = '';
    for (let i = 0; i < items.length; i++) {
        let div = document.createElement('div');
        div.classList.add('block');
        let p = document.createElement('p');
        p.innerHTML = `Name: ${items[i]['show']['name']}`;
        let img = document.createElement('img');
        img.setAttribute('src', `${items[i]['show']['image']['medium']}`);
        div.appendChild(p);
        div.appendChild(img);
        content.appendChild(div);
    }
}


submit.addEventListener('click', (event) => {
    let inputValue = document.getElementById('input_movie').value;
    let response = fetch(`http://api.tvmaze.com/search/shows?q=${inputValue}`);
    response
        .then((data) => {
            return data.json()
        })
        .then(items => {
            console.log('Movies: ', items)
            search(items)
        })
});
