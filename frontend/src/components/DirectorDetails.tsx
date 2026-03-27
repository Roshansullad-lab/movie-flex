import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function DirectorDetail() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [director, setDirector] = useState<any>(null);

    useEffect(() => {
        fetch(`http://localhost:8000/directors/${id}`)
            .then(res => res.json())
            .then(setDirector);
    }, [id]);

    if (!director) return <p>Loading...</p>;

    const prevId = Number(id) - 1;
    const nextId = Number(id) + 1;

    return (
        <div className="director-detail">
            <div className="nav-arrows">
                {prevId > 0 && (
                    <button onClick={() => navigate(`/directors/${prevId}`)}>← Previous</button>
                )}
                <button onClick={() => navigate(`/directors/${nextId}`)}>Next →</button>
            </div>
            <img src={director.poster_url} alt={director.name} className="poster1" />
            <h1>{director.name}</h1>
            <p><strong>Birth Year:</strong> {director.birth_year}</p>
            <p>{director.bio}</p>

            <h3>Movies Directed:</h3>
            <ul>
                {director.movies.map((m: any) => (
                    <li key={m.id}>{m.title} ({m.release_year})</li>
                ))}
            </ul>
        </div>
    );
}

