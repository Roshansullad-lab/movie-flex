import { useEffect, useState } from "react";
import axios from "axios";

export default function MovieReviews({ movieId }: { movieId: number }) {
  const [reviews, setReviews] = useState([]);
  const [rating, setRating] = useState(null);

  useEffect(() => {
    axios.get(`http://localhost:8000/movies/${movieId}/reviews`)
      .then(res => setReviews(res.data));
    axios.get(`http://localhost:8000/movies/${movieId}/rating`)
      .then(res => setRating(res.data.average_rating));
  }, [movieId]);

  return (
    <div>
      <h3 className="text-lg font-bold">Reviews</h3>
      {rating && <p>⭐ Average Rating: {rating.toFixed(1)}/10</p>}
      {reviews.map((r: any) => (
        <div key={r.id} className="border p-2 mb-2">
          <p><strong>{r.reviewer_name}</strong> ⭐ {r.rating}/10</p>
          <p>{r.review_text}</p>
        </div>
      ))}
    </div>
  );
}
