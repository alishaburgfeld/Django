// document.getElementById("button-test").addEventListener("submit", (event) => {
// 	event.preventDefault();
// });
function sign_up(event) {
	event.preventDefault();
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
			if (response.data.Success === "True") {
				login_redirect = document.getElementById("log_in_redirect");
				login_redirect.innerHTML = 'You have successfully signed up! Login <a href="/log_in"> here </a>';
				// THIS ISN'T WORKING!!!!!!!!!
				//could you do another axios. post here with the datbase info sendin it to login to auto log in the user?
				alert("You have successfully signed up!");
			}
		});
}
