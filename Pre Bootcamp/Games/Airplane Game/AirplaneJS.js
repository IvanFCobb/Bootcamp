document.addEventListener('DOMContentLoaded',() => {
    document.addEventListener('keydown', control)
    let content
var player = {
    left: 450,
    top: 620
}

var enemies = [
    {left: 450, top: 250},
    {left: 550, top: 200},
    {left: 650, top: 150},
    {left: 350, top: 200},
    {left: 250, top: 150}
]

var missiles = []

function drawPlayer(){
    content = "<div class='player' style='left:"+player.left+"px; top:"+player.top+"px'></div>";
    document.getElementById("players").innerHTML = content;
}
document.getElementById("players").innerHTML = content;


function drawEnemies(){
    content = "";
    for(var idx=0;idx<enemies.length;idx++) {
        content += "<div class='enemies' style='left:"+enemies[idx].left+"px; top:"+enemies[idx].top+"px'></div>";
    }
    document.getElementById("enemies").innerHTML = content;
}

function moveEnemies(){
    for(var idx=0;idx<enemies.length;idx++){
        enemies[idx].top = enemies[idx].top + .25;
    }
}

function drawMissiles(){
    content="";
    for (var idx=0;idx<missiles.length;idx++){
        content += "<div class='missiles' style='left:"+missiles[idx].left+"px; top:"+missiles[idx].top+"px'></div>";
    }
    document.getElementById("missiles").innerHTML = content;
}

function moveMissiles(){
    for(var idx=0;idx<missiles.length;idx++){
        missiles[idx].top = missiles[idx].top - 1;
    }
}

function control(e) {
    if(e.keyCode == 37 && player.left>10){//left
        player.left = player.left - 20
    }
    if(e.keyCode == 39 && player.left<830){//right
        player.left = player.left + 20
        console.log(player.left)
    }
    if(e.keyCode == 38 && player.top>400){//Up
        player.top = player.top - 20
        console.log(player.top)
    }
    if(e.keyCode == 40 && player.top<620){//down
        player.top = player.top + 20
        console.log(player.top)
    }
    if(e.keyCode ==32){
        missiles.push({left: (player.left+34), top: (player.top-8)})
        drawMissiles()
    }
    drawPlayer();
}

function gameloop(){
    setTimeout(gameloop, 10)

    drawEnemies()
    moveEnemies()

    drawMissiles()
    moveMissiles()

    drawPlayer()
}
gameloop()


})