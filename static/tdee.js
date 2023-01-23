
        
function getbmr(gender, age, weight, height, activity) {
    var gender = document.getElementById("gender").value;
    var age = document.getElementById("age").value;
    var weight = document.getElementById("weight").value;
    var height = document.getElementById("height").value;
    var activity = document.getElementById("activity").value;
    sum1 = (( parseInt(gender) + (10 * parseInt(weight) + 6.25 * parseInt(height) - 5 * parseInt(age)))* parseFloat(activity));  
    return alert(sum1) 
}

function bodytype(body,diet) {
    var body = document.getElementById("bodytype1").value;
    var diet = document.getElementsByName("gain").value;
        if (body = "option1"  && (diet = "option11")) {
            protein_gainecto = weight * 0.32
            sum2 = sum1 + (protein_gainecto * 4)
        return console.log(sum2)
        } 
        else if (body = "option1" &&(diet = "option22")){
            protein_mainecto = weight * 0.1
            sum3 = sum1 + (protein_mainecto * 4)
        return alert(sum3)
        }
}
