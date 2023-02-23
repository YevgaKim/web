function show_hide_password(target){
	var input = document.getElementById('password-input');
	if (input.getAttribute('type') == 'password') {
		input.setAttribute('type', 'text');
	} else {
		input.setAttribute('type', 'password');
	}
	return false;
}

const password1 = document.querySelector("#password1"),
	  password2 = document.querySelector("#password2")

password1.addEventListener("click",(event)=>{
	event.preventDefault();
	const input = document.getElementById('password-input1');
	if (input.getAttribute('type') == 'password') {
		input.setAttribute('type', 'text');
	} else {
		input.setAttribute('type', 'password');
	}
});

password2.addEventListener("click",(event)=>{
	event.preventDefault();
	const input = document.getElementById('password-input2');
	if (input.getAttribute('type') == 'password') {
		input.setAttribute('type', 'text');
	} else {
		input.setAttribute('type', 'password');
	}
});