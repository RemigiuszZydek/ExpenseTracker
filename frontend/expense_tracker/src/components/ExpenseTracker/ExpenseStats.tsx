import { useEffect, useState } from "react";
import { statsExpense } from "../../services/ExpenseTracker/expenses";

export default function ExpenseStats({ reload }) {
	const [stats, setStats] = useState(null);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState("");

	useEffect(() => {
		async function loadStats() {
			setLoading(true);
			setError("");
			try {
				const data = await statsExpense();
				setStats(data);
			} catch (err) {
				setError(err.message);
			} finally {
				setLoading(false);
			}
		}
		loadStats();
	}, [reload]);

	if (loading)
		return (
			<div className="text-gray-200 text-center my-4">
				Ładowanie statystyk...
			</div>
		);
	if (error)
		return <div className="text-red-500 text-center my-4">Błąd: {error}</div>;
	if (!stats) return null;

	const formatAmount = (value: any) => {
		const num = Number(value);
		return isNaN(num) ? "0.00" : num.toFixed(2);
	};

	return (
		<div className="bg-gray-800 text-gray-200 p-6 rounded-xl shadow-lg mb-8 max-w-3xl mx-auto">
			<h3 className="text-xl font-bold text-orange-400 mb-4">
				Statystyki wydatków
			</h3>

			<div className="grid grid-cols-1 md:grid-cols-3 gap-4">
				<div className="p-4 bg-gray-700 rounded">
					<p className="text-sm text-gray-400">Suma wydatków</p>
					<p className="text-2xl font-bold text-green-400">
						{formatAmount(stats?.total)} zł
					</p>
				</div>

				<div className="p-4 bg-gray-700 rounded">
					<p className="text-sm text-gray-400">Średnio dziennie</p>
					<p className="text-2xl font-bold text-green-400">
						{formatAmount(stats?.average_per_day)} zł
					</p>
				</div>

				<div className="p-4 bg-gray-700 rounded">
					<p className="text-sm text-gray-400">Wydatki według kategorii</p>

					<ul className="mt-2 text-gray-200">
						{Object.entries(stats?.by_category || {}).map(([cat, amount]) => (
							<li key={cat}>
								{cat}:{" "}
								<span className="font-bold">{formatAmount(amount)} zł</span>
							</li>
						))}
					</ul>
				</div>
			</div>
		</div>
	);
}
