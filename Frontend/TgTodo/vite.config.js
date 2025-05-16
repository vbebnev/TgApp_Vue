import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import htmlConfig from 'vite-plugin-html-config'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    htmlConfig({
      headScripts: [
        {
          src: `/telegram-web-app.js?v=${Date.now()}`,
        },
      ],
    })
  ],
  build: {
    rollupOptions: {
      output: {
        entryFileNames: `assets/[name].js?v=${Date.now()}`,
        chunkFileNames: `assets/[name]-[hash].js?v=${Date.now()}`,
        assetFileNames: `assets/[name]-[hash].[ext]?v=${Date.now()}`,
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
