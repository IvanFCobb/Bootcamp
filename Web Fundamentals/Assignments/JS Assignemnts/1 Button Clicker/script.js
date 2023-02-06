function logStatus(element){
    if (element.innerText=="Login"){
    element.innerText = "Logout"
    } else{
        element.innerText = "Login"
    }
}

function removeElement(element){
    element.remove()
}