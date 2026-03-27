import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function ActorList() {
    const [actors, setActors] = useState<any[]>([]);

    useEffect(() => {
      //  fetch("http://localhost:8000/actors")
        fetch(`${import.meta.env.VITE_API_URL}actors`)

            .then(res => res.json())
            .then(setActors);
    }, []);

    return (
        <div className="actor-grid">
            {actors.map((a) => (
                <Link to={`/actors/${a.id}`} key={a.id} className="actor-card">
                    <img src={a.poster_url} alt={a.name} className="poster1" />
                    <div className="actor-info">

                    <h2>{a.name}</h2>
                        <p><strong>Birth Year:</strong> {a.birth_year}</p>
                    </div>
                </Link>
            ))}
        </div>
    );
}


//export default function ActorProfile({ actorId }: { actorId: number }) {
//  const [actor, setActor] = useState<any>(null);

//  useEffect(() => {
//    axios.get(`http://localhost:8000/actors/${actorId}`)
//      .then(res => setActor(res.data));
//  }, [actorId]);

//  if (!actor) return <p>Loading...</p>;

//  return (
//    <div>
//      <h1 className="text-2xl font-bold">{actor.name}</h1>
//      <p>Born: {actor.birth_year}</p>
//      <p>{actor.bio}</p>
//      <h3 className="mt-4 font-semibold">Movies:</h3>
//      <ul>
//        {actor.movies.map((m: any) => (
//          <li key={m.id}>{m.title} ({m.release_year})</li>
//        ))}
//      </ul>
//    </div>
//  );
//}
