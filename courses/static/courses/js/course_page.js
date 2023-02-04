var player= document.getElementById('player')
var managelistwidth= document.getElementById('manageflow')
window.onload= maintainratio()
window.addEventListener("resize", maintainratio);
function maintainratio()
{   
    console.log(
        "cw:"+ player.clientWidth,
        "ch:"+ player.clientHeight,
        "w:"+ player.width,
       " h:"+ player.height
    )
    var w= player.clientWidth
    var h= (w*9)/16
    player.height= h
    console.log(w,h)
    managelistwidth.style.height= h+ "px"

}