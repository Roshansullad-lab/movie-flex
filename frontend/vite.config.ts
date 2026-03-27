import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
    plugins: [react()],
    root: ".", // ensures Vite looks in project root for index.html
    server: { port: 3000 }
});

// https://vitejs.dev/config/
//export default defineConfig({
//    plugins: [react()],
//    root: ".", // ensures Vite looks in project root for index.html

//    server: {
//        port: 3000, // local dev port
//    },
//    build: {
//        outDir: 'dist', // Vercel expects dist folder
//    },
//    base: '/', // important: ensures assets resolve correctly on Vercel
//})

