import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function GenreList() {
    const [genres, setGenres] = useState<any[]>([]);

    useEffect(() => {
        //fetch("http://localhost:8000/genres")
        fetch(`${import.meta.env.VITE_API_URL}genres`)
            .then(res => res.json())
            .then(setGenres);
    }, []);

    return (
        <div className="genre-grid">
            {genres.map((g) => (
                <Link to={`/genres/${g.id}`} key={g.id} className="genre-card">
                    <h2>{g.name}</h2>
                </Link>
            ))}
        </div>
    );
}
