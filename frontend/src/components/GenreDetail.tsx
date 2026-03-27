import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

export default function GenreDetail() {
    const { id } = useParams();
    const [genre, setGenre] = useState<any>(null);

    useEffect(() => {
        fetch(`http://localhost:8000/genres/${id}`)
            .then(res => res.json())
            .then(setGenre);
    }, [id]);

    if (!genre) return <p>Loading...</p>;

    return (
        <div className="genre-detail">
            <h1>{genre.name}</h1>
            <h3>Movies:</h3>
            <ul>
                {genre.movies.map((m: any) => (
                    <li key={m.id}>{m.title} ({m.release_year})</li>
                ))}
            </ul>
        </div>
    );
}
