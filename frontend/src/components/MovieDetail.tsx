import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function MovieDetail() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [movie, setMovie] = useState<any>(null);

    useEffect(() => {
       // fetch(`http://localhost:8000/movies/${id}`)
        fetch(`${import.meta.env.VITE_API_URL}movies/${id}`)
            .then(res => res.json())
            .then(setMovie);
    }, [id]);

    if (!movie) return <p>Loading...</p>;

    const prevId = Number(id) - 1;
    const nextId = Number(id) + 1;

    return (
        <div className="movie-detail">
            <div className="nav-arrows">
                {prevId > 0 && (
                    <button onClick={() => navigate(`/movies/${prevId}`)}>← Previous</button>
                )}
                <button onClick={() => navigate(`/movies/${nextId}`)}>Next →</button>
            </div>
            <img src={movie.poster_url} alt={movie.title} className="poster" />
            <h1>{movie.title}</h1>
            <p><strong>Year:</strong> {movie.release_year}</p>
            <p><strong>Director:</strong> {movie.director?.name}</p>
            <p>{movie.description}</p>
        </div>
    );
}


//export default function MovieDetail() {
//    const { id } = useParams();
//    const [movie, setMovie] = useState<any>(null);

//    useEffect(() => {
//        fetch(`http://localhost:8000/movies/${id}`)
//            .then(res => res.json())
//            .then(setMovie);
//    }, [id]);

//    if (!movie) return <p>Loading...</p>;

//    return (
//        <div className="movie-detail">
//            <img src={movie.poster_url} alt={movie.title} className="poster" />
//            <h1>{movie.title}</h1>
//            <p><strong>Year:</strong> {movie.release_year}</p>
//            <p><strong>Director:</strong> {movie.director?.name}</p>
//            <p>{movie.description}</p>
//        </div>
//    );
//}
