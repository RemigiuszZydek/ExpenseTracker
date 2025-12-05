import { API_URL, handleResponse } from "../api";

const expenses_url = `${API_URL}/expenses/`;

export async function getAllExpenses() {
	const res = await fetch(expenses_url);
	return handleResponse(res);
}

export async function deleteExpense(id) {
	const res = await fetch(`${expenses_url}${id}`, {
		method: "DELETE",
	});
	return handleResponse(res);
}

export async function updateExpense(data) {
	const res = await fetch(`${expenses_url}${data.id}`, {
		method: "PUT",
		headers: { "Content-type": "application/json" },
		body: JSON.stringify(data),
	});
	return handleResponse(res);
}

export async function addExepense(data) {
	const res = await fetch(expenses_url, {
		method: "POST",
		headers: {
			"Content-type": "application/json",
		},
		body: JSON.stringify(data),
	});

	return handleResponse(res);
}
