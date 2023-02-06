// // // 1 Always Hungry **************************************************

function alwaysHungry(arr) {
    for (i = 0; i < arr.length; i++) {
        if (arr[i] == "food") {
            return console.log("yummy")
        }
    }
    console.log("I'm hungry")
}

alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]);


// // 2 High Pass Filter **************************************************

function highPass(arr, cutoff) {
    var filteredArr = [];
    for (i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff)
            filteredArr.push(arr[i])
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);


// // 3 Better than average **************************************************

function betterThanAverage(arr) {
    var sum = 0;
    for (i = 0; i < arr.length; i++) {
        sum = sum + arr[i]
        var avg = sum / (arr.length - 1)
    }
    var avg = sum / (arr.length - 1)
    var count = 0
    for (i = 0; i < arr.length; i++) {
        if (avg > arr[i]) {
            count = count + 1
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);


// // 4 Array Reverse **************************************************

function reverse(arr) {
    var arrTemp = []
    for (i = arr.length - 1; i >= 0; i--) {
        arrTemp.push(arr[i])
    }
    arr = arrTemp
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]copy

// // 5 Array Reverse **************************************************

function fibonacciArray(n) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    var fibArr = [0, 1];
    for (var i = 0; i < n - 2; i++) {
        fibArr.push(fibArr[i] + fibArr[i + 1])
    }
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]