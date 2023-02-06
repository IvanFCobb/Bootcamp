var imgage;

function removeElement(id){
    var element=document.querySelector(id)
    element.remove()
}

function altImageOn(id){
    image=document.querySelector(id)
    image.src = "assets/succulents-2.jpg"
}

function altImageOff(id){
    image=document.querySelector(id)
    image.src = "assets/succulents-1.jpg"
    
}