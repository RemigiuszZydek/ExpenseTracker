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
		<div className="flex justify-center items-start min-w-screen bg-gray-100 p-6">
			<div className="w-full max-w-6xl bg-white rounded-xl shadow-lg p-6">
				<h2 className="text-3xl font-bold mb-6 text-center">Lista wydatków</h2>

				<div className="overflow-x-auto">
					<table className="min-w-full border border-gray-200 rounded-lg">
						<thead className="bg-gray-200">
							<tr>
								<th className="text-left py-3 px-6 text-lg font-semibold">
									Tytuł
								</th>
								<th className="text-left py-3 px-6 text-lg font-semibold">
									Data
								</th>
								<th className="text-left py-3 px-6 text-lg font-semibold">
									Kategoria
								</th>
								<th className="text-right py-3 px-6 text-lg font-semibold">
									Kwota
								</th>
							</tr>
						</thead>
						<tbody>
							{expenses.map((exp) => (
								<tr
									key={exp.id}
									className="hover:bg-blue-50 transition-colors duration-200"
								>
									<td className="py-4 px-6 text-lg">{exp.title}</td>
									<td className="py-4 px-6 text-lg">{exp.date}</td>
									<td className="py-4 px-6 text-lg">{exp.category}</td>
									<td className="py-4 px-6 text-lg text-right font-bold">
										{exp.amount} zł
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
