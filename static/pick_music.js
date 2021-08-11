var i=0

function musicAdded() {
    if (this.style.backgroundColor === "rgb(23, 98, 167)"){
        this.style.backgroundColor = "rgb(86, 90, 101)"
        i--
    }    
    else {
        this.style.backgroundColor ="rgb(23, 98, 167)"
        i++
    }
    console.log(i)
    if(i==1){
        document.getElementById("playlistAdd").removeAttribute("disabled");
        document.getElementById("playlistAdd").style.backgroundColor= "#1762A7";
        document.getElementById("playlistAdd").style.color= "#ffffff"
    }
    else if(i==0){
        document.getElementById("playlistAdd").disabled=true
        document.getElementById("playlistAdd").style.backgroundColor= "#696a70"
        document.getElementById("playlistAdd").style.color= "#525357"
    }
        
}
