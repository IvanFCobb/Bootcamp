var user = [
    document.querySelector("#user1"), 
    document.querySelector("#user2"),
    ]

var connections = document.querySelector("#connect-number")
var connectCount = 500

console.log(connections)

var requests = document.querySelector("#request-number2")
var requestCount = 2

console.log(requests)


var userName = document.querySelector("#user-name")

function removeUser(x){
    user[x].remove()
}

function addConnection(){
    connectCount = connectCount + 1
    connections.innerText = connectCount+"+"
}

function removeRequest(){
    requestCount = requestCount - 1
    requests.innerText = requestCount
}

function changeName(){
    userName.innerText = "Ivan Cobb"
}