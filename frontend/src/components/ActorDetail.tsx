import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

export default function ActorDetail() {
    const { id } = useParams();
    const navigate = useNavigate();
    const [actor, setActor] = useState<any>(null);

    useEffect(() => {
        fetch(`http://localhost:8000/actors/${id}`)
            .then(res => res.json())
            .then(setActor);
    }, [id]);

    if (!actor) return <p>Loading...</p>;

    const prevId = Number(id) - 1;
    const nextId = Number(id) + 1;

    return (
        <div className="actor-detail">
            <div className="nav-arrows">
                {prevId > 0 && (
                    <button onClick={() => navigate(`/actors/${prevId}`)}>← Previous</button>
                )}
                <button onClick={() => navigate(`/actors/${nextId}`)}>Next →</button>
            </div>

            <img src={actor.poster_url} alt={actor.name} className="poster1" />
            <h1>{actor.name}</h1>
            <p><strong>Birth Year:</strong> {actor.birth_year}</p>
            <p>{actor.bio}</p>
            <h3>Movies:</h3>
            <ul>
                {actor.movies.map((m: any) => (
                    <li key={m.id}>{m.title} ({m.release_year})</li>
                ))}
            </ul>

        </div>
    );
}



//export default function ActorDetail() {
//    const { id } = useParams();
//    const [actor, setActor] = useState<any>(null);

//    useEffect(() => {
//        fetch(`http://localhost:8000/actors/${id}`)
//            .then(res => res.json())
//            .then(setActor);
//    }, [id]);

//    if (!actor) return <p>Loading...</p>;

//    return (
//        <div className="actor-detail">
//            <img src={actor.poster_url} alt={actor.name} className="poster1" />
//            <h1>{actor.name}</h1>
//            <p><strong>Birth Year:</strong> {actor.birth_year}</p>
//            <p>{actor.bio}</p>
//            <h3>Movies:</h3>
//            <ul>
//                {actor.movies.map((m: any) => (
//                    <li key={m.id}>{m.title} ({m.release_year})</li>
//                ))}
//            </ul>
//        </div>
//    );
//}
