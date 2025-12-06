import { API_URL, handleResponse, buildQuery } from "../api";

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

export async function statsExpense(start_date?, end_date?) {
	const params = new URLSearchParams();

	// dodawaj tylko jeśli jest niepusty string
	if (start_date) params.append("start_date", start_date);
	if (end_date) params.append("end_date", end_date);

	// jeżeli params jest pusty, nie dodawaj '?'
	const queryString = params.toString();
	const url = queryString
		? `${expenses_url}stats?${queryString}`
		: `${expenses_url}stats`;

	const res = await fetch(url);
	return handleResponse(res);
}

export async function statsExpenseMonthly() {
	const res = await fetch(`${expenses_url}stats_monthly`);
	return handleResponse(res);
}
