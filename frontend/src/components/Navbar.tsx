import { Link } from "react-router-dom";

export default function Navbar() {
    return (
        <nav className="navbar">
            <h1 className="logo">Movie Flex</h1>
            <ul className="nav-links">
                <li><Link to="/">Movies</Link></li>
                <li><Link to="/actors">Actors</Link></li>
                <li><Link to="/directors">Directors</Link></li>
                <li><Link to="/genres">Genres</Link></li>
            </ul>
        </nav>
    );
}
