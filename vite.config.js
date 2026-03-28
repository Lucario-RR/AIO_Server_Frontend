import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import vueDevTools from 'vite-plugin-vue-devtools'

/** GitHub Pages: project sites need /<repo>/; user/org site repo `<user>.github.io` uses /. */
function githubPagesBase() {
  const repo = process.env.GITHUB_REPOSITORY
  if (!repo) return '/'
  const name = repo.split('/')[1]
  const owner = process.env.GITHUB_REPOSITORY_OWNER ?? ''
  if (name === `${owner}.github.io`) return '/'
  return `/${name}/`
}

// https://vite.dev/config/
export default defineConfig({
  base: githubPagesBase(),
  plugins: [
    vue(),
    vueJsx(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
