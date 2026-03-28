import { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import MovieList from "./components/MovieList";
import MovieDetail from "./components/MovieDetail";
import ActorList from "./components/ActorList";
import DirectorList from "./components/DirectorList";
import GenreList from "./components/GenreList";
import Navbar from "./components/Navbar";
import Searchbar from "./components/SearchBar";
import ActorDetail from "./components/ActorDetail"
import DirectorDetail from "./components/DirectorDetails";
import GenreDetail from "./components/GenreDetail";
import HeroBanner from "./components/HeroBanner";

export default function App() {
    const [searchQuery, setSearchQuery] = useState("");

    return (
        <div className="app-background">
            <Navbar />
            <Searchbar onSearch={setSearchQuery} />
            <HeroBanner />

            <Routes>

                <Route path="/" element={<MovieList searchQuery={searchQuery} />} />
                <Route path="/movies/:id" element={<MovieDetail />} />
                <Route path="/actors" element={<ActorList />} />
                <Route path="/actors/:id" element={<ActorDetail />} />  {/* <-- important */}
                <Route path="/directors" element={<DirectorList />} />
                <Route path="/directors/:id" element={<DirectorDetail />} />
                <Route path="/genres" element={<GenreList />} />
                <Route path="/genres/:id" element={<GenreDetail />} />
            </Routes>
            </div>
    );
}

