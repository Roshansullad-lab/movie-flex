import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function DirectorList() {
    const [directors, setDirectors] = useState<any[]>([]);

    useEffect(() => {
        fetch("http://localhost:8000/directors")
            .then(res => res.json())
            .then(setDirectors);
    }, []);

    return (
        <div className="director-grid">
            {directors.map((d) => (
                <Link to={`/directors/${d.id}`} key={d.id} className="director-card">
                    <img src={d.poster_url} alt={d.name} className="poster1" />
                    <h2>{d.name}</h2>
                    <p><strong>Birth Year:</strong> {d.birth_year}</p>
                </Link>
            ))}
        </div>
    );
}
