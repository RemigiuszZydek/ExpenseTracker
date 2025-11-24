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
		<div className="p-4 max-w-3xl mx-auto">
			<h2 className="text-2xl font-bold mb-4">Lista wydatków</h2>

			<ul className="space-y-3">
				{expenses.map((exp) => (
					<li
						key={exp.id}
						className="p-4 bg-gray-100 rounded-lg flex justify-between"
					>
						<div>
							<p className="font-semibold">{exp.title}</p>
							<p className="text-sm text-gray-600">{exp.date}</p>
							<p className="text-sm">{exp.category}</p>
						</div>
						<p className="font-bold">{exp.amount} zł</p>
					</li>
				))}
			</ul>
		</div>
	);
}
