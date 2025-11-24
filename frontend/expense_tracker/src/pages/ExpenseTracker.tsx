import ExpenseList from "../components/ExpenseTracker/ExpensesList";

export default function ExpenseTracker() {
	return (
		<div className="flex flex-col items-center justify-center min-h-screen px-4">
			<h1 className="text-3xl font-bold mb-8 text-center">Expense Tracker</h1>
			<ExpenseList />
		</div>
	);
}
