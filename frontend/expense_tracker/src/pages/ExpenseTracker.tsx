import { useState } from "react";
import AddExpenseForm from "../components/ExpenseTracker/AddExpense";
import ExpenseList from "../components/ExpenseTracker/ExpensesList";
import ExpenseStats from "../components/ExpenseTracker/ExpenseStats";

export default function ExpenseTracker() {
	const [reload, setReload] = useState(false);
	return (
		<div className="min-h-screen bg-gray-900 py-10">
			<h1 className="text-4xl font-bold text-center text-orange-500 mb-10 drop-shadow-sm">
				Expense Tracker
			</h1>
			<AddExpenseForm onAdded={() => setReload(!reload)} />
			<ExpenseStats reload={reload} />
			<ExpenseList reload={reload} setReload={setReload} />
		</div>
	);
}
