import { deleteExpense } from "../../services/ExpenseTracker/expenses";

export default function DeleteExpenseButton({ id, onDelete }) {
	const handleDelete = async () => {
		if (window.confirm("Na pewno chcesz usunąć ten wpis?")) {
			try {
				await deleteExpense(id);
				onDelete();
			} catch (err) {
				alert("Błąd przy usuwaniu: " + err.message);
			}
		}
	};

	return (
		<button
			onClick={handleDelete}
			className="text-red-500 hover:text-red-400 transition transform hover:scale-110"
		>
			❌
		</button>
	);
}
