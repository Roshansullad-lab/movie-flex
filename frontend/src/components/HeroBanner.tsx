import { useEffect, useState } from "react";

export default function HeroBanner() {
    const [featured, setFeatured] = useState<any>(null);

    useEffect(() => {
        // Fetch a featured movie (could be random or marked in DB)
       // fetch("http://localhost:8000/movies/featured")
        fetch(`${import.meta.env.VITE_API_URL}movies/featured`)
            .then(res => res.json())
            .then(setFeatured);
    }, []);

    if (!featured) return null;

    return (
        <div className="hero-banner">
            <video
                className="hero-video"
            //src={featured.trailer_url}
                src={"/pics/prv1.mp4"}
                
                autoPlay
                muted
                loop
            />
            <div className="hero-overlay">
                <h1>{featured.title}</h1>
                <p>{featured.description}</p>
                <button className="play-btn">▶ Play</button>
                <button className="info-btn">ℹ More Info</button>
            </div>
        </div>
    );
}
