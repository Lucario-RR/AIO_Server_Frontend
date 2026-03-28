import { ref, watchEffect } from 'vue'
import { defineStore } from 'pinia'

export const useSettingsStore = defineStore('settings', () => {
  const theme = ref(localStorage.getItem('aio_theme') || 'system')
  const language = ref(localStorage.getItem('aio_language') || 'zh-CN')
  const density = ref(localStorage.getItem('aio_density') || 'comfortable')
  const showDebugInfo = ref(localStorage.getItem('aio_show_debug') === '1')

  watchEffect(() => {
    const root = document.documentElement
    root.dataset.theme = theme.value
    root.dataset.density = density.value

    localStorage.setItem('aio_theme', theme.value)
    localStorage.setItem('aio_language', language.value)
    localStorage.setItem('aio_density', density.value)
    localStorage.setItem('aio_show_debug', showDebugInfo.value ? '1' : '0')
  })

  return {
    theme,
    language,
    density,
    showDebugInfo,
  }
})

