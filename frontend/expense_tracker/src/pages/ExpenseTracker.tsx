import { useState } from "react";
import AddExpenseForm from "../components/ExpenseTracker/AddExpense";
import ExpenseList from "../components/ExpenseTracker/ExpensesList";

export default function ExpenseTracker() {
	const [reload, setReload] = useState(false);
	return (
		<div className="min-h-screen bg-gray-100 py-10">
			<h1 className="text-4xl font-bold text-center text-blue-700 mb-10 drop-shadow-sm">
				Expense Tracker
			</h1>
			<AddExpenseForm onAdded={() => setReload(!reload)} />
			<ExpenseList />
		</div>
	);
}
