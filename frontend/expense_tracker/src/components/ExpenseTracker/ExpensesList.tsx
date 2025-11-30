import { useEffect, useState } from "react";
import { getAllExpenses } from "../../services/ExpenseTracker/expenses";

export default function ExpenseList() {
	const [expenses, setExpenses] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState("");

	useEffect(() => {
		async function loadExpenses() {
			try {
				const data = await getAllExpenses();
				setExpenses(data);
			} catch (error) {
				setError(error.message);
			} finally {
				setLoading(false);
			}
		}
		loadExpenses();
	}, []);

	if (loading) return <div>...Ładowanie</div>;
	if (error) return <div>Bład: {error}</div>;

	return (
		<div className="flex justify-center mt-10">
			<div className="w-full max-w-6xl bg-white rounded-2xl shadow-2xl p-8">
				<h2 className="text-4xl font-bold mb-8 text-center text-blue-600">
					Lista wydatków
				</h2>

				<div className="overflow-hidden rounded-xl border border-gray-200">
					<table className="min-w-full">
						<thead className="bg-blue-600 text-white">
							<tr>
								<th className="py-4 px-6 text-left font-semibold">Tytuł</th>
								<th className="py-4 px-6 text-left font-semibold">Data</th>
								<th className="py-4 px-6 text-left font-semibold">Kategoria</th>
								<th className="py-4 px-6 text-right font-semibold">Kwota</th>
								<th className="py-4 px-6 text-center font-semibold">Akcje</th>
							</tr>
						</thead>

						<tbody className="divide-y divide-gray-200">
							{expenses.map((exp) => (
								<tr key={exp.id} className="hover:bg-blue-50 transition-all">
									<td className="py-4 px-6 text-gray-800 font-medium">
										{exp.title}
									</td>
									<td className="py-4 px-6 text-gray-600">
										{new Date(exp.date).toLocaleDateString()}
									</td>
									<td className="py-4 px-6">{exp.category}</td>
									<td className="py-4 px-6 text-right font-bold text-green-600">
										{exp.amount.toFixed(2)} zł
									</td>
									<td className="py-4 px-6 text-center flex justify-center gap-4">
										<button className="text-blue-600 hover:scale-110 transition"></button>
										<button className="text-red-600 hover:scale-110 transition"></button>
									</td>
								</tr>
							))}
						</tbody>
					</table>
				</div>
			</div>
		</div>
	);
}
