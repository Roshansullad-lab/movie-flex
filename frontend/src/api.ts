import axios from "axios";

const API_BASE = "http://localhost:8000"; // backend FastAPI URL

// Fetch movies with optional filters
export const fetchMovies = async (filters: Record<string, string | number>) => {
  const params = new URLSearchParams(filters as any).toString();
  const res = await axios.get(`${API_BASE}/movies?${params}`);
  return res.data;
};

// Fetch single movie by ID
export const fetchMovieById = async (id: number) => {
  const res = await axios.get(`${API_BASE}/movies/${id}`);
  return res.data;
};

// Fetch actors
export const fetchActors = async () => {
  const res = await axios.get(`${API_BASE}/actors`);
  return res.data;
};

export const fetchActorsById = async (id: number) => {
    const res = await axios.get(`${API_BASE}/actors/${id}`);
    return res.data;
};

// Fetch directors
export const fetchDirectors = async () => {
  const res = await axios.get(`${API_BASE}/directors`);
  return res.data;
};

export const fetchDirectorsById = async (id: number) => {
    const res = await axios.get(`${API_BASE}/directors/${id}`);
    return res.data;
};

// Fetch genres
export const fetchGenres = async () => {
  const res = await axios.get(`${API_BASE}/genres`);
  return res.data;
};

export const fetchGenresById = async (id: number) => {
    const res = await axios.get(`${API_BASE}/genres/${id}`);
    return res.data;
};

// Fetch reviews for a movie
export const fetchReviews = async (movieId: number) => {
  const res = await axios.get(`${API_BASE}/movies/${movieId}/reviews`);
  return res.data;
};

// Fetch average rating for a movie
export const fetchAverageRating = async (movieId: number) => {
  const res = await axios.get(`${API_BASE}/movies/${movieId}/rating`);
  return res.data;
};
