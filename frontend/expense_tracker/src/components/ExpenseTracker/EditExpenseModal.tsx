import { useState, useEffect, use } from "react";
import { updateExpense } from "../../services/ExpenseTracker/expenses";

export default function EditExpenseModal({
	expense,
	isOpen,
	onClose,
	onUpdated,
}) {
	const [form, setForm] = useState({
		title: "",
		amount: "",
		category: "",
		date: "",
	});
	const [loading, setLoading] = useState(false);
	const [error, setError] = useState("");

	useEffect(() => {
		if (expense) {
			setForm({
				title: expense.title,
				amount: expense.amount,
				category: expense.category,
				date: expense.date,
			});
		}
	}, [expense]);

	const handleChange = (e) =>
		setForm({ ...form, [e.target.name]: e.target.value });

	const handleSubmit = async (e) => {
		e.preventDefault();
		setLoading(true);
		setError("");

		try {
			const updatedData = {
				id: expense.id,
				...form,
				amount: parseFloat(form.amount),
			};

			await updateExpense(updatedData);

			if (onUpdated) onUpdated(updatedData);
			onClose();
		} catch (err) {
			setError(err.message || "Błąd podczas aktualizacji");
		} finally {
			setLoading(false);
		}
	};

	if (!isOpen || !expense) return null;

	return (
		<div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
			<div className="bg-gray-800 text-gray-200 rounded-xl p-6 w-full max-w-md shadow-xl">
				<h3 className="text-2xl font-bold mb-4 text-orange-400">
					Edytuj wydatek
				</h3>

				<form onSubmit={handleSubmit} className="space-y-4">
					<input
						type="text"
						name="title"
						value={form.title}
						onChange={handleChange}
						className="w-full p-2 rounded border border-gray-600 bg-gray-700"
						required
					/>
					<input
						type="number"
						name="amount"
						value={form.amount}
						onChange={handleChange}
						step="0.01"
						className="w-full p-2 rounded border border-gray-600 bg-gray-700"
						required
					/>
					<input
						type="text"
						name="category"
						value={form.category}
						onChange={handleChange}
						className="w-full p-2 rounded border border-gray-600 bg-gray-700"
						required
					/>
					<input
						type="date"
						name="date"
						value={form.date}
						onChange={handleChange}
						className="w-full p-2 rounded border border-gray-600 bg-gray-700"
						required
					/>

					{error && <p className="text-red-500">{error}</p>}

					<div className="flex justify-end gap-4 mt-4">
						<button
							type="button"
							onClick={onClose}
							className="px-4 py-2 bg-gray-600 rounded hover:bg-gray-500"
						>
							Anuluj
						</button>
						<button
							type="submit"
							disabled={loading}
							className="px-4 py-2 bg-orange-500 rounded hover:bg-orange-400"
						>
							{loading ? "Zapisywanie..." : "Zapisz"}
						</button>
					</div>
				</form>
			</div>
		</div>
	);
}
