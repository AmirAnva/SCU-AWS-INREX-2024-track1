// // import { defineConfig } from 'vite';
// // import react from '@vitejs/plugin-react';

// // export default defineConfig({
// //   plugins: [react()],
// //   server: {
// //     proxy: {
// //       '/': {
// //         target: 'http://127.0.0.1:8080', // Use 127.0.0.1 explicitly
// //         changeOrigin: true,
// //         rewrite: (path) => path, // No rewrite needed; keep the root path
// //       },
// //     },
// //   },
// // });


// // vite.config.js
// export default {
//   // config options
// }
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})