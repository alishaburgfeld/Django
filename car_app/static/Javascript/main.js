function edit_brand_name(brand_id) {
	axios({
		method: "post",
		url: "/<{{brand.id}}/edit/",
		data: {
			brand_id: brand_id,
			new_name: new_name,
		},
	}).then(function (response) {
		const elem = document.getElementById({response.data.brand_id}_name);
		elem.innerHTML = response.data.brand_name
	});
}

function edit_brand_name(brand_id) {
	axios({
		method: "post",
		url: "/<{{brand.id}}/edit/",
		data: {
			brand_id: brand_id,
			new_description: new_description,
		},
	}).then(function (response) {
		const elem = document.getElementById({response.data.brand_id}_description);
		elem.innerHTML = response.data.brand_description
	});
}