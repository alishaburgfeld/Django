function edittask(event) {
	event.preventDefault();
	let span = document.getElementById("edit-span");
	let task_id = span.value;
	console.log(`EDITING NOW: ${task_id} ${span}`);
	let edited_data = {};

	for (let i = 0; i < event.target.length; i++) {
		let name = event.target[i].name;
		let value = event.target[i].value;

		edited_data[name] = value;
	}
	console.log(edited_data);
	axios
		.post(`/task/edit/${task_id}`, edited_data)
		.then(function (response) {
			console.log(response.data.data);
			window.location.href = "/todos/"; //can be used to refresh page
		})
		.catch((response) => {
			console.log("something went wrong");
		});
}
