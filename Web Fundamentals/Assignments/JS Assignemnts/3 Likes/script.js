var likeCounter1 = document.querySelector("#like-count-1")
var likeCount = [9,12,9]

var likeCounter2 = document.querySelector("#like-count-2")
var likeCount2 = 12

var likeCounter3 = document.querySelector("#like-count-3")
var likeCount3 = 9


function addLikes1(element){
    likeCount[0] = likeCount[0] + 1
    likeCounter1.innerText = likeCount[0] + " like(s)"
}

function addLikes2(element){
    likeCount[1] = likeCount[1] + 1
    likeCounter2.innerText = likeCount[1] + " like(s)"
}

function addLikes3(element){
    likeCount[2] = likeCount[2] + 1
    likeCounter3.innerText = likeCount[2] + " like(s)"
}