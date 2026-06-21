document
.getElementById("contactForm")
.addEventListener("submit", function(event){


event.preventDefault();


let data = {

name:
document.getElementById("name").value,


email:
document.getElementById("email").value,


message:
document.getElementById("message").value

};



fetch("http://127.0.0.1:5000/contact",
{

method:"POST",

headers:
{
"Content-Type":"application/json"
},


body:
JSON.stringify(data)

})


.then(response=>response.json())


.then(result=>{

document.getElementById("result").innerHTML =
result.message;

});


});
