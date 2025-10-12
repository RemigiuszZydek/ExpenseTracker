import { Link } from "react-router-dom";

export default function ProgramCard({ title, description, link }) {
	return (
		<Link
			to={link}
			className="block bg-white hover:bg-blue-50 border border-gray-200 rounded-2xl shadow-sm p-6 transition-all duration-200 hover:shadow-lg"
		>
			<h2 className="text-xl font-semibold mb-2">{title}</h2>
			<p className="text-gray-600">{description}</p>
		</Link>
	);
}
