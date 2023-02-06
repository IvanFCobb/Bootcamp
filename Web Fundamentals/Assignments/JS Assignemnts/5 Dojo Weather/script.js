var unit = document.querySelector("#unit").value
console.log(unit)

function removeElement(id){
    var element=document.querySelector(id)
    element.remove()
}

var highTemps = [
    document.querySelector("#day1-high").innerText,
    document.querySelector("#day2-high").innerText,
    document.querySelector("#day3-high").innerText,
    document.querySelector("#day4-high").innerText,
]
var elementHighTemps = [
    document.querySelector("#day1-high"),
    document.querySelector("#day2-high"),
    document.querySelector("#day3-high"),
    document.querySelector("#day4-high"),
]

var lowTemps = [
    document.querySelector("#day1-low").innerText,
    document.querySelector("#day2-low").innerText,
    document.querySelector("#day3-low").innerText,
    document.querySelector("#day4-low").innerText,
]

var elementLowTemps = [
    document.querySelector("#day1-low"),
    document.querySelector("#day2-low"),
    document.querySelector("#day3-low"),
    document.querySelector("#day4-low"),
]

console.log(lowTemps)
console.log(highTemps)

function convertUnits(){
if(unit=="celcius"){
    for(i=0;i<highTemps.length;i++) {
        highTemps[i] = ((highTemps[i]*9/5)+32)|0
        elementHighTemps[i].innerText=highTemps[i]
    }

    for(i=0;i<lowTemps.length;i++) {
        lowTemps[i] = ((lowTemps[i]*9/5)+32)|0
        elementLowTemps[i].innerText=lowTemps[i]
    }
}else{
    for(i=0;i<highTemps.length;i++) {
        highTemps[i] = ((highTemps[i]-31)*(5/9))|0
        elementHighTemps[i].innerText=highTemps[i]
    }

    for(i=0;i<lowTemps.length;i++) {
        lowTemps[i] = ((lowTemps[i]-31)*(5/9))|0
        elementLowTemps[i].innerText=lowTemps[i]
    }
}
unit = document.querySelector("#unit").value
console.log(unit)
}