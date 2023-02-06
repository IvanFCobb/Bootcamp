document.addEventListener('DOMContentLoaded',() => {
//Creating Divs for game board
document.addEventListener('keyup', control)
drawWorld();
drawMiniGrid();
function drawWorld() {
    output = "";
    for (var i=0; i<220; i++) {
      output += "<div>";
      output += "</div>";
    }
    document.getElementById("grid").innerHTML = output;
}
function drawMiniGrid() {
    output = "";
    for (var i=0; i<16; i++) {
      output += "<div>";
      output += "</div>";
    }
    document.getElementById("miniGrid").innerHTML = output;
}

    const grid = document.querySelector('.grid ');
    let squares = Array.from(document.querySelectorAll('.grid div'));
    let miniSquares = Array.from(document.querySelectorAll('.miniGrid div'));
    const scoreDisplay = document.querySelector('#score')
    const startBtn = document.querySelector('#start-button')
    const width = 10 ;
    let nextRandom = 0
    const displayBlock = document.querySelectorAll('.miniGrid div');
    const displayWidth = 4
    let displayIndex = 0
    let timerId = null
    let score = 0
    const colors = ['orange', 'red','purple','green','blue']

    //the blocks
    const Lblock = [
      [1, width +1, width *2+1,2],
      [width, width+1, width+2, width*2+2],
      [1, width+1,width*2+1,width*2],
      [width,width*2,width*2+1,width*2+2],
    ]

    const Zblock = [
      [width*2, width +1, width *2+1,width+2],
      [0, width, width+1, width*2+1],
      [width+2, width+1,width*2+1,width*2],
      [0,width,width+1,width*2+1],
    ]

    const Tblock = [
      [1, width, width+1,width+2],
      [1, width+1, width*2+1, width+2],
      [width,width+1,width+2,width*2+1],
      [1,width+1,width*2+1,width],
    ]

    const Oblock = [
      [0,1,width, width+1],
      [0,1,width, width+1],
      [0,1,width, width+1],
      [0,1,width, width+1],
    ]

    const Iblock = [
      [1,width+1,width*2+1,width*3+1],
      [width, width+1,width+2,width+3],
      [1,width+1,width*2+1,width*3+1],
      [width, width+1,width+2,width+3],
    ]

    const theBlocks = [Lblock,Zblock,Tblock,Oblock,Iblock];
    let currentPosition = 4
    let currentRotation = 0
    let random = Math.floor(Math.random()*theBlocks.length)
    let current = theBlocks[random][currentRotation]
    const edgeBlock = 200;

    function drawBlock(){
      current.forEach(index => {
        squares[currentPosition + index].classList.add('block')
        squares[currentPosition + index].style.backgroundColor = (colors[random])
      })
    }

    function undrawBlock(){
      current.forEach(index => {
        squares[currentPosition + index].classList.remove('block')
        squares[currentPosition + index].style.backgroundColor = ''
      })
    }

    function drawEdge(){    
      for (i=0;i<10;i++) {
        squares[edgeBlock + i].classList.add('taken')
      } 
    }

    drawEdge()

    function control(e) {
      if (e.keyCode === 65 ) {
      moveLeft()
    } else if (e.keyCode === 68 ) {
      moveRight()
    } else if (e.keyCode === 87 ) {
      rotate()
    } else if (e.keyCode === 83 ) {
      moveDown ()
    }
    }

    function moveDown(){
      undrawBlock()
      currentPosition += width
      drawBlock()
      freeze()
    }

    function freeze(){
      if (current.some(index =>squares[currentPosition+index+width].classList.contains('taken'))) {
        current.forEach(index => squares [currentPosition+index].classList.add('taken'))
        random = nextRandom
        nextRandom = Math.floor(Math.random()*theBlocks.length)
        current = theBlocks[random][currentRotation]
        currentPosition = 4
        drawBlock()
        displayMiniBlock()
        addScore()
        gameOver()
      
      }
    }

    function moveLeft(){
      undrawBlock()
      const isAtLeftEdge = current.some(index => (currentPosition + index) % width === 0)

      if (!isAtLeftEdge) currentPosition -=1

      if (current.some(index => squares[currentPosition + index].classList.contains('taken'))) {
      currentPosition += 1
      }

      drawBlock()
    }

    function moveRight(){
      undrawBlock()
      const isAtRightEdge = current.some(index => (currentPosition + index) % width === width -1)

      if (!isAtRightEdge) currentPosition +=1

      if (current.some(index => squares[currentPosition + index].classList.contains('taken'))) {
      currentPosition -= 1
      }

      drawBlock()
    }

    function rotate() {
      undrawBlock()
      currentRotation ++
      if(currentRotation === current.length){
        currentRotation = 0
      }
      current = theBlocks[random][currentRotation]
      drawBlock()
    }

   const upNextBlock = [
      [1, displayWidth +1, displayWidth *2+1,2],
      [displayWidth*2, displayWidth +1, displayWidth *2+1,displayWidth+2],
      [1, displayWidth, displayWidth+1,displayWidth+2],
      [0,1,displayWidth, displayWidth+1],
      [1,displayWidth+1,displayWidth*2+1,displayWidth*3+1],
    ]

    function displayMiniBlock() {
      displayBlock.forEach(square => {
        square.classList.remove('block')
        square.style.backgroundColor = ''
      })
      upNextBlock[nextRandom].forEach(index => {
        displayBlock[displayIndex + index].classList.add('block')
        displayBlock[displayIndex + index].style.backgroundColor = colors[nextRandom]
      })
    }

    function addScore(){
      for (let i=0;i<199;i +=width){
        const row = [i, i+1, i+2, i+3, i+4, i+5, i+6, i+7, i+8, i+9]

      if (row.every(index=> squares[index].classList.contains('taken'))){
        score += 10
        scoreDisplay.innerHTML = score 
        row.forEach(index=> {
          squares[index].classList.remove('taken')
          squares[index].classList.remove('block')
          squares[index].style.backgroundColor = ''
        })
       const squaresRemoved = squares.splice(i, width)
       squares = squaresRemoved.concat(squares)
       squares.forEach(cell => grid.appendChild(cell))
      }
    }
    }

    function gameOver() {
      if (current.some(index => squares[currentPosition+index].classList.contains('taken'))){
        scoreDisplay.innerHTML = 'end'
        clearInterval(timerId)
      }
    }

    startBtn.addEventListener('click', ()=>{
      if (timerId){
        clearInterval(timerId)
        timerId=null
      } else {
        drawBlock()
        timerId = setInterval(moveDown, 250)
        displayMiniBlock()
      }
    })

})