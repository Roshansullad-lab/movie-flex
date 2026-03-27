import { useEffect, useState } from "react";
import { fetchMovies } from "../api";
import { Link } from "react-router-dom";


 export default function MovieList({ searchQuery = "" }: { searchQuery?: string }) {
     const [movies, setMovies] = useState<any[]>([]);

     useEffect(() => {
         //fetch("http://localhost:8000/movies")
         fetch(`${import.meta.env.VITE_API_URL}movies`)
             .then(res => res.json())
             .then(setMovies);
     }, []);

     // Always show all movies if searchQuery is empty
     const filteredMovies = movies.filter((m) => {
         if (!searchQuery) return true;  // <-- important fix

         const query = searchQuery.toLowerCase();
         return (
             m.title.toLowerCase().includes(query) ||
             (m.director?.name?.toLowerCase().includes(query)) ||
             m.actors.some((a: any) => a.name.toLowerCase().includes(query)) ||
             m.genres.some((g: any) => g.name.toLowerCase().includes(query)) ||
             String(m.release_year).includes(query)
         );
     });

     return (
         <div className="movie-grid">
             {filteredMovies.map((m) => (
                 <Link to={`/movies/${m.id}`} key={m.id} className="movie-card">
                     <img src={m.poster_url || "/posters/placeholder.jpg"} alt={m.title} className="poster" />
                     <div className="movie-info">
                         <h2>{m.title}</h2>
                         <p><strong>Year:</strong> {m.release_year}</p>
                         <p><strong>Director:</strong> {m.director?.name}</p>
                         <p><strong>Genres:</strong> {m.genres.map((g: any) => g.name).join(", ")}</p>
                         <p><strong>Actors:</strong> {m.actors.map((a: any) => a.name).join(", ")}</p>
                     </div>
                 </Link>
             ))}
         </div>
     );
}

//export default function MovieList() {
//  const [movies, setMovies] = useState([]);

//  useEffect(() => {
//    fetchMovies({}).then(setMovies);
//  }, []);

//  return (

//    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
//        <div className="movie-grid">
//          {movies.map((m: any) => (

//              <Link to={`/movies/${m.id}`} key={m.id} className="movie-card">
//                  <img src={m.poster_url} alt={m.title} className="poster"  />
//                  <div className="movie-info">
//                      <h2>{m.title}</h2>
//                      <p><strong>Year:</strong> {m.release_year}</p>
//                      <p><strong>Director:</strong> {m.director?.name}</p>
//                      <p><strong>Description:</strong> {m.description}</p>
//                      <p><strong>Genres:</strong> {m.genres.map((g: any) => g.name).join(", ")}</p>
//                      <p><strong>Actors:</strong> {m.actors.map((a: any) => a.name).join(", ")}</p>

//                  </div>
//              </Link>

//          ))}
//      </div>



  
//</div>


//  );
//}
