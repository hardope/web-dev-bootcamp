function remove(input) {
     document.getElementById(input).style.display = "none"
}

function count (){
     var number = 0

     while (true){
          document.getElementById("count").innerHTML = "" + number+1
     }
}