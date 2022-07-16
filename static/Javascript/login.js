function log_in(event) {
	event.preventDefault();
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
			window.location.href = "/todos/";
			// works! yay!
		});
}
