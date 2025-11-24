export const API_URL =
	process.env.REACT_APP_API_BASE || "http://localhost:8000";

export async function handleResponse(response) {
	const text = await response.text().catch(() => "");
	if (!response.ok) {
		let message = text || `${response.status} ${response.statusText}`;
		try {
			const json = JSON.parse(text);
			message = json.detail || json.message || JSON.stringify(json);
		} catch {
			throw new Error(message);
		}
	}
	return text ? JSON.parse(text) : null;
}

export function buildQuery(params = {}) {
	const query_params = new URLSearchParams();
	Object.entries(params).forEach(([k, v]) => {
		if (v !== undefined && v !== null && v !== "")
			query_params.append(k, String(v));
	});
	return query_params.toString();
}
