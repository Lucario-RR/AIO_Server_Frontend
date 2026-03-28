import { execSync, spawnSync } from 'node:child_process'
import { fileURLToPath } from 'node:url'

const root = fileURLToPath(new URL('..', import.meta.url))

function deployBaseFromOrigin() {
  const url = execSync('git remote get-url origin', { encoding: 'utf8', cwd: root }).trim()
  const m = url.match(/[:/]([^/]+)\/([^/.]+)(?:\.git)?$/i)
  if (!m) throw new Error('无法从 git remote 解析仓库名，请检查 origin')
  const owner = m[1]
  const name = m[2]
  if (name.toLowerCase() === `${owner.toLowerCase()}.github.io`) return '/'
  return `/${name}/`
}

const DEPLOY_BASE = deployBaseFromOrigin()
const r = spawnSync('npx', ['vite', 'build'], {
  cwd: root,
  stdio: 'inherit',
  env: { ...process.env, DEPLOY_BASE },
  shell: true,
})
process.exit(r.status ?? 1)
