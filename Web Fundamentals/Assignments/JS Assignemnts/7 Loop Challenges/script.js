// **************************************************************
// 1 Print odds 1-20

console.log("1 Print odds 1-20")

function odds() {
    var odds = 0;
    for (i = 1; i < 20; i += 2) {
        odds = odds + i;
    }
    console.log(odds)
}

odds()


// **************************************************************
// 2 Decreasing Multiples of 3

console.log("2 Decreasing Multiples of 3")

function multiples3() {
    for (i = 100; i > 0; i -= 1)
        if (i % 3 == 0) {
            console.log(i)
        }
}
multiples3()


// **************************************************************
// 3 Print the sequence

console.log("3 Print the sequence")

function sequence() {
    for (i = 4; i >= -3.5; i -= 1.5) {
        console.log(i)
    }
}
sequence()


// **************************************************************
// 4 Sigma

console.log("4 Sigma")

function sigma() {
    var sum = 0;
    for (i = 1; i <= 100; i++) {
        sum = sum + i;
    }
    console.log(sum)
}
sigma()


// **************************************************************
// 5 Factorial

console.log("5 Factorial")

function factorial() {
    var product = 1;
    for (i = 1; i <= 12; i++) {
        product = product * i;
    }
    console.log(product)
}

factorial()
