import { useEffect, useState } from "react";
import { getAllExpenses } from "../../services/ExpenseTracker/expenses";
import DeleteExpenseButton from "./DeleteExpenseButton";
import EditExpenseModal from "./EditExpenseModal";

export default function ExpenseList({ reload, setReload }) {
	const [expenses, setExpenses] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState("");
	const [editingExpense, setEditingExpense] = useState(null);
	const [isModalOpen, setIsModalOpen] = useState(false);

	useEffect(() => {
		async function loadExpenses() {
			try {
				const data = await getAllExpenses();
				console.log(data);
				setExpenses(data);
			} catch (error) {
				setError(error.message);
			} finally {
				setLoading(false);
			}
		}
		loadExpenses();
	}, [reload]);

	if (loading) return <div>...Ładowanie</div>;
	if (error) return <div>Bład: {error}</div>;

	return (
		<div className="flex justify-center mt-10 px-4">
			<div className="w-full max-w-6xl bg-gray-800 rounded-2xl shadow-2xl p-8">
				<h2 className="text-4xl font-bold mb-8 text-center text-orange-400 drop-shadow-md">
					Lista wydatków
				</h2>

				<div className="overflow-x-auto rounded-xl border border-gray-700 shadow-inner">
					<table className="min-w-full text-gray-200">
						<thead className="bg-orange-600 text-white uppercase text-sm tracking-wider">
							<tr>
								<th className="py-3 px-6 text-left font-semibold">Tytuł</th>
								<th className="py-3 px-6 text-left font-semibold">Data</th>
								<th className="py-3 px-6 text-left font-semibold">Kategoria</th>
								<th className="py-3 px-6 text-right font-semibold">Kwota</th>
								<th className="py-3 px-6 text-center font-semibold">Akcje</th>
							</tr>
						</thead>

						<tbody className="divide-y divide-gray-700">
							{expenses.map((exp) => (
								<tr
									key={exp.id}
									className="hover:bg-gray-700 transition-colors duration-200 cursor-pointer"
								>
									<td className="py-4 px-6 font-medium">{exp.title}</td>
									<td className="py-4 px-6 text-gray-400">
										{new Date(exp.date).toLocaleDateString()}
									</td>
									<td className="py-4 px-6 text-gray-300">{exp.category}</td>
									<td className="py-4 px-6 text-right font-bold text-green-400">
										{exp.amount.toFixed(2)} zł
									</td>
									<td className="py-4 px-6 text-center flex justify-center gap-4">
										<button
											className="text-blue-400 hover:text-blue-300 transition transform hover:scale-110"
											onClick={() => {
												setEditingExpense(exp);
												setIsModalOpen(true);
											}}
										>
											✏
										</button>
										<DeleteExpenseButton
											id={exp.id}
											onDelete={() => setReload((prev) => !prev)}
										/>
									</td>
								</tr>
							))}
						</tbody>
					</table>
				</div>

				<EditExpenseModal
					expense={editingExpense}
					isOpen={isModalOpen}
					onClose={() => setIsModalOpen(false)}
					onUpdated={() => setReload((prev) => !prev)}
				/>
			</div>
		</div>
	);
}
