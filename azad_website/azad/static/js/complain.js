let complains = document.querySelectorAll(".complain");
complains.forEach((complain)=>{
    if(complain.innerHTML.length>80){
        complain.innerHTML = complain.innerHTML.substring(0, 80)+"...";
    }
    
})