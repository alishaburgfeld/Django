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
			if (response.data.Success === true) {
				console.log("log-in-works!");
				console.log(response.data);
				window.location.href = "/todos/";
			} else if (response.data.Success === false) {
				console.log(response.data);
				login_alert = document.getElementById("log-in-alert");
				login_alert.innerHTML = `Sorry, ${response.data.reason}!`;
			}
			// fail works but now my success isn't workin
		});
}
