import { render, screen } from "@testing-library/react";
import MovieList from "../src/components/MovieList";
import axios from "axios";

jest.mock("axios");
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe("MovieList Component", () => {
  it("renders movies from API", async () => {
    mockedAxios.get.mockResolvedValueOnce({
      data: [
        {
          id: 1,
          title: "Inception",
          release_year: 2010,
          director: { name: "Christopher Nolan" },
          genres: [{ name: "Sci-Fi" }]
        }
      ]
    });

    render(<MovieList />);
    const movieTitle = await screen.findByText("Inception");
    expect(movieTitle).toBeInTheDocument();
  });
});
