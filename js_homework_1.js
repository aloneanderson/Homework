// 1. While confirm
let res = confirm("Type OK to close this window");
while (res === false) {
    let res = confirm("Type OK to close this window");
    if (res === true) {
        break;
    }
}

// 2. Cubes
let cubes = [];
for (let i = 0; i < 30; i++) {
    cubes.push(i * i * i);
}
console.log(cubes);

// 3. Cумма арифметической прогрессии с шагом 3
let type = prompt('Type ur number');
let sum = 0;
for (let i = 1; i <= type; i = i + 3) {
    console.log(i);
    sum += i;
}
document.write(sum)


// 4. Строка с шахматной доской
let m = 6;
let n = 4;
let text = '.#'
let result = '';
for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        if (i % 2 === 0) {
            result += text;
        } else {
            result += text.split('').reverse().join('');
        }
    }
    result += '\n'
}
console.log(result);
