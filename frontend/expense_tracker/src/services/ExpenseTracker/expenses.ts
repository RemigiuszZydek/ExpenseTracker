import { API_URL, handleResponse } from "../api";

const expenses_url = `${API_URL}/expenses/`;

export async function getAllExpenses() {
	const res = await fetch(expenses_url);
	return handleResponse(res);
}
