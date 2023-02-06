
var crustType = ["deep dish", "hand tossed", "thin crust"]
var sauceType = ["traditional", "marinara", "meat sauce"]
var cheeses = ["mozzerella", "fetta", "mozz and feta"]
var toppings = [" pepperoni", " sausage", " mushrooms", " olives", " onions"]




function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {};
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings
    return pizza;
}

var p1 = pizzaOven(crustType[0], sauceType[0], cheeses[0], toppings[0] + toppings[1]);
var p2 = pizzaOven(crustType[1], sauceType[1], cheeses[2], toppings[2] + toppings[3] + toppings[4]);
var p3 = pizzaOven(crustType[Math.round(Math.random() * 2)], sauceType[Math.round(Math.random() * 2)], cheeses[Math.round(Math.random() * 2)], toppings[Math.round(Math.random() * 4)] + toppings[Math.round(Math.random() * 4)]);
var p4 = pizzaOven(crustType[Math.round(Math.random() * 2)], sauceType[Math.round(Math.random() * 2)], cheeses[Math.round(Math.random() * 2)], toppings[Math.round(Math.random() * 4)] + toppings[Math.round(Math.random() * 4)]);

console.log("Pizza 1");
console.log(p1);
console.log("Pizza 2");
console.log(p2);
console.log("Pizza 2 topping random 1");
console.log(p3);
console.log("Pizza 2 topping random 2");
console.log(p4);


