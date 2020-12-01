const text = 'testId';
const testID = document.getElementById('some_text');
console.log(testID.innerText);

const divTest = document.getElementById('Monday');
const pElem = document.createElement('p');
divTest.appendChild(pElem);

let name = 'Alex';
let username = prompt('type ur name');
if (name === username) {
    document.write('Privet ', name);
} else {
    document.write('Goodbye ', username);
}
document.onclick = function () {
    console.log('ТЫ НАЖАЛ НА МЫШКУ')
}

const idClass = document.getElementById('idClass');

idClass.style.width = '100px';
idClass.style.height = '100px';
idClass.style.backgroundColor = 'Yellow';
idClass.addEventListener('click', function (event) {
    console.log('ДОБАВИЛ СОБЫТИЕ')
})

const divElement = document.getElementById('main');
divElement.style.width = '500px';
divElement.style.height = '500px';
divElement.style.backgroundColor = 'black';
divElement.addEventListener('click', (event) => {
    console.log('event: ', event.target);
    if (!event.target.id) {
        event.target.style.backgroundColor = 'red';
    }
})

const login = document.getElementById('id1');
const password = document.getElementById('id2');
const submit = document.getElementById('id3');

submit.addEventListener('click', (event) => {
    console.log(login.value);
    console.log(password.value);
})

const names = document.getElementsByClassName('user');
for (let i = 0; i < names.length; i++) {
    names[i].addEventListener('click', () => {
        console.log(names[i].innerText)
    });

    setTimeout(() => {
            console.log('Hellow');
        }, 2000
    );

    let response = fetch('http')
