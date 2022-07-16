function addToDo(event) {
	event.preventDefault();
	span = document.getElementById("edit-span");
	task_id = span.value;
	console.log("EDITING NOW");
	let edited_data = {};

	for (let i = 0; i < event.target.length; i++) {
		let name = event.target[i].name;
		let value = event.target[i].value;

		edited_data[name] = value;
	}
	console.log(edited_data);
	axios
		.post("/edit/", edited_data)
		.then(function (response) {
			console.log(response.data.data);
			// task = response.data.data;

			// let list = document.getElementById("to-do-list");
			// let = document.createElement("li");
			// li.innerHTML = `
			// <span>${task.category}</span>
			// <span>${task.title}</span>
			// <span>${task.priority}</span>`;
			// // console.log(li)
			// list.appendChild(li);
			window.location.href = "/todos/"; //can be used to refresh page
		})
		.catch((response) => {
			console.log("something went wrong");
		});
}
