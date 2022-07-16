function addToDo(event) {
	event.preventDefault();
	console.log("IN JS");
	let new_task = {};

	for (let i = 0; i < event.target.length; i++) {
		let name = event.target[i].name;
		let value = event.target[i].value;

		new_task[name] = value;
	}
	console.log(event.target);
	console.log(new_task);
	axios
		.post("/addtask/", new_task)
		.then(function (response) {
			console.log(response.data.data);
			// task = response.data.data

			// let list = document.getElementById('list')
			// let li = document.createElement('li')

			// console.log(customer)

			// li.innerHTML= `Customer: ${customer.first_name} ${customer.last_name}`
			// console.log(li)
			// list.appendChild(li)
			// window.location.href=''      //can be used to refresh page
		})
		.catch((response) => {
			console.log("something went wrong");
		});
}
