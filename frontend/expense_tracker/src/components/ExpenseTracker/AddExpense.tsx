import { useState } from "react";
import { addExepense } from "../../services/ExpenseTracker/expenses";

export default function AddExpenseForm({ onAdded }) {
	const [form, setForm] = useState({
		title: "",
		amount: "",
		category: "",
		date: "",
	});

	const [loading, setLoading] = useState(false);
	const [error, setError] = useState("");

	function handleChange(e) {
		setForm({ ...form, [e.target.name]: e.target.value });
	}

	async function handleSubmit(e) {
		e.preventDefault();
		setLoading(true);
		setError("");

		try {
			const data = {
				...form,
				amount: parseFloat(form.amount),
			};
			const result = await addExepense(data);

			if (onAdded) onAdded(result);
			setForm({ title: "", amount: "", category: "", date: "" });
		} catch (err) {
			setError(err.message);
		} finally {
			setLoading(false);
		}
	}

	return (
		<form
			onSubmit={handleSubmit}
			className="bg-gray-800 shadow-lg rounded-xl p-6 mb-8 w-full max-w-3xl mx-auto"
		>
			<h3 className="text-2xl font-bold mb-4 text-center text-orange-500">
				Dodaj wydatek
			</h3>

			<div className="grid grid-cols-1 md:grid-cols-2 gap-4">
				<input
					type="text"
					name="title"
					placeholder="Tytuł"
					className="p-3 rounded-lg border border-gray-600 bg-gray-700 text-gray-100"
					value={form.title}
					onChange={handleChange}
					required
				/>
				<input
					type="number"
					name="amount"
					placeholder="Kwota"
					className="p-3 rounded-lg border border-gray-600 bg-gray-700 text-gray-100"
					value={form.amount}
					onChange={handleChange}
					step="0.01"
					required
				/>
				<input
					type="text"
					name="category"
					placeholder="Kategoria"
					className="p-3 rounded-lg border border-gray-600 bg-gray-700 text-gray-100"
					value={form.category}
					onChange={handleChange}
					required
				/>
				<input
					type="date"
					name="date"
					className="p-3 rounded-lg border border-gray-600 bg-gray-700 text-gray-100"
					value={form.date}
					onChange={handleChange}
					required
				/>
			</div>

			{error && (
				<p className="text-red-500 mt-3 text-center text-sm">{error}</p>
			)}

			<button
				type="submit"
				disabled={loading}
				className="w-full bg-orange-600 hover:bg-orange-800 text-white font-semibold py-3 rounded-lg mt-6 transition"
			>
				{loading ? "Dodawanie..." : "Dodaj wydatek"}
			</button>
		</form>
	);
}
