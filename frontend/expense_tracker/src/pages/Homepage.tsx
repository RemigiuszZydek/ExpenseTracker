import ProgramCard from "../components/ProgramCard";

export default function HomePage() {
	return (
		<div className="flex flex-col items-center justify-center min-h-screen px-4">
			<h1 className="text-3xl font-bold mb-8 text-center">Wybierz Program</h1>
			<div className="grid grid-cols-1 sm:grid-cols-2  gap-6 max-w-4xl w-full">
				<ProgramCard
					title="💰 Expense Tracker"
					description="Śledź swoje wydatki i zarządzaj budżetem."
					link="/expense-tracker"
				/>
				<ProgramCard
					title="📈 Investment Tracker"
					description="Monitoruj swoje inwestycje i portfel."
					link="#"
				/>
			</div>
		</div>
	);
}
