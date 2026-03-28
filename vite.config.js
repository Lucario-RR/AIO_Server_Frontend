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
  if (name.toLowerCase() === `${owner.toLowerCase()}.github.io`) return '/'
  return `/${name}/`
}

function pagesBase() {
  const explicit = process.env.DEPLOY_BASE
  if (explicit != null && explicit !== '') return explicit
  return githubPagesBase()
}

// https://vite.dev/config/
export default defineConfig(({ command }) => ({
  base: pagesBase(),
  plugins: [
    vue(),
    vueJsx(),
    command === 'serve' && vueDevTools(),
  ].filter(Boolean),
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
}))
