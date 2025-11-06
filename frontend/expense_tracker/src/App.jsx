import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/Homepage";
import ExpenseTracker from "./pages/ExpenseTracker";

function App() {
	return (
		<Router>
			<div className="min-h-screen bg-gray-100 text-gray-800">
				<Routes>
					<Route path="/" element={<HomePage />} />
					<Route path="/expense-tracker" element={<ExpenseTracker />} />
				</Routes>
			</div>
		</Router>
	);
}

export default App;
