import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    plugins: [react()],
    root: ".", // ensures Vite looks in project root for index.html
    server: { port: 3000, host: "localhost" }
});
