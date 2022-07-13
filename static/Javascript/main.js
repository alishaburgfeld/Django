document.getElementById("button-test-two").addEventListener("submit", (event) => {
	event.preventDefault();
});
function log_in() {
	email_input = document.getElementById("log_in_email_input");
	password_input = document.getElementById("log_in_password_input");
	email = document.getElementById("log_in_email_input").value;
	console.log(email);
	password = document.getElementById("log_in_password_input").value;
	console.log(password);
	axios
		.post("/log_in/", {
			email: email,
			password: password,
		})
		.then((response) => {
			console.log("log-in-test");
			console.log(response.data);
		});
}

document.getElementById("button-test").addEventListener("submit", (event) => {
	event.preventDefault();
});
function sign_up() {
	// do we need to prevent default? do we need to pass in event?
	email_input = document.getElementById("sign_up_email_input");
	password_input = document.getElementById("sign_up_password_input");
	email = document.getElementById("sign_up_email_input").value;
	console.log(email);
	password = document.getElementById("sign_up_password_input").value;
	console.log(password);
	axios
		.post("/sign_up/", {
			email: email,
			password: password,
			username: email,
		})
		.then((response) => {
			// const elem = document.getElementById("tester");
			// elem.innerHTML = response.data.email;
			console.log("pretty please");
			console.log(response);
		});
}
