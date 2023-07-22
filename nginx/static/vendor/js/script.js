
const password1 = document.querySelector?.("#password-input1"),
	  password2 = document.querySelector?.("#password-input2"),
	  password = document.querySelector?.("#password-input"),
	  b1 = document.querySelector?.("#b1"),
	  b2 = document.querySelector?.("#b2"),
	  b3 = document.querySelector?.("#b3");


function change(pass,b){
	if(b===null) return
	b.addEventListener("click",(event)=>{
		event.preventDefault();
		if (pass.getAttribute('type') == 'password') {
			pass.setAttribute('type', 'text');
		} else {
			pass.setAttribute('type', 'password');
		}});
}

change(password,b1);
change(password1,b2);
change(password2,b3);