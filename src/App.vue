<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { computed, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useSettingsStore } from '@/stores/settings'
import { useI18n } from '@/i18n'

const { t } = useI18n()
const settingsStore = useSettingsStore()
const { showDebugInfo } = storeToRefs(settingsStore)

const tabs = computed(() => [
  { path: '/', label: t('nav.home'), icon: '🏠' },
  { path: '/schedule', label: t('nav.schedule'), icon: '📅' },
  { path: '/about', label: t('nav.about'), icon: '👤' },
  { path: '/around', label: t('nav.around'), icon: '🛍️' },
  { path: '/settings', label: t('nav.settings'), icon: '⚙️' },
])

const featureTabs = computed(() => [
  { path: '/blogs', label: t('home.modules.blogs.title') },
  { path: '/ledger', label: t('home.modules.ledger.title') },
  { path: '/currency', label: t('home.modules.currency.title') },
  { path: '/account', label: t('home.modules.account.title') },
  { path: '/bike', label: t('home.modules.bike.title') },
  { path: '/gallery', label: t('home.modules.gallery.title') },
])

const featureOpen = ref(false)

/** 与 public/favicon.ico 同源，换图标只改一处 */
const avatarSrc = `${import.meta.env.BASE_URL}favicon.ico`

const debugInfo = {
  mode: import.meta.env.MODE,
  baseUrl: import.meta.env.BASE_URL,
}
</script>

<template>
  <div class="app-shell">
    <header class="top-nav">
      <div class="top-nav-inner">
        <button class="avatar-pill" type="button">
          <span class="avatar-ring">
            <img :src="avatarSrc" alt="Logo" class="avatar-img" />
          </span>
        </button>

        <div class="nav-row">
          <nav class="tab-nav primary" aria-label="Main navigation">
            <RouterLink
              v-for="tab in tabs"
              :key="tab.path"
              :to="tab.path"
              class="tab-item"
            >
              <span class="tab-icon">{{ tab.icon }}</span>
              <span class="tab-label">{{ tab.label }}</span>
            </RouterLink>
          </nav>

          <div
            class="feature-menu"
            @mouseenter="featureOpen = true"
            @mouseleave="featureOpen = false"
          >
            <button class="tab-item feature-trigger" type="button">
              <span class="tab-label">{{ t('nav.features') }}</span>
            </button>
            <div class="feature-dropdown" v-if="featureOpen">
              <RouterLink
                v-for="tab in featureTabs"
                :key="tab.path"
                :to="tab.path"
                class="dropdown-item"
              >
                {{ tab.label }}
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </header>

    <main class="app-main">
      <RouterView v-slot="{ Component }">
        <transition name="fade-slide" mode="out-in">
          <component :is="Component" />
        </transition>
      </RouterView>
    </main>

    <footer v-if="showDebugInfo" class="debug-bar">
      <div class="debug-inner">
        <span class="debug-title">{{ t('debugBar.title') }}</span>
        <span class="debug-item">
          {{ t('debugBar.mode') }}: <code>{{ debugInfo.mode }}</code>
        </span>
        <span class="debug-item">
          {{ t('debugBar.baseUrl') }}: <code>{{ debugInfo.baseUrl }}</code>
        </span>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.top-nav {
  display: flex;
  justify-content: center;
  margin-top: 24px;
  padding: 0 12px;
}

.top-nav-inner {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 10px 18px;
  border-radius: 999px;
  background: var(--color-background-soft);
  box-shadow:
    0 10px 24px rgba(15, 23, 42, 0.12),
    0 0 0 1px rgba(148, 163, 184, 0.35);
}

.avatar-pill {
  border: none;
  padding: 0;
  background: radial-gradient(circle at 30% 0%, #ffd1e5, #f973a6);
  border-radius: 999px;
  padding: 3px;
  box-shadow:
    0 0 0 4px rgba(251, 113, 133, 0.2),
    0 10px 25px rgba(251, 113, 133, 0.45);
  cursor: pointer;
}

.avatar-ring {
  display: block;
  border-radius: inherit;
  background: #0f172a;
  padding: 3px;
}

.avatar-img {
  display: block;
  width: 40px;
  height: 40px;
  border-radius: 999px;
  object-fit: cover;
}

.tab-nav {
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-row {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tab-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-heading);
  background: var(--color-background);
  border: 1px solid var(--color-border);
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
  transition:
    background-color 0.18s ease,
    color 0.18s ease,
    box-shadow 0.18s ease,
    transform 0.12s ease;
}

.tab-item:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(15, 23, 42, 0.12);
}

.tab-item.router-link-exact-active {
  background: linear-gradient(135deg, #f9a8d4, #fb7185);
  color: #ffffff;
  border-color: transparent;
  box-shadow:
    0 10px 20px rgba(248, 113, 166, 0.45),
    0 0 0 1px rgba(255, 255, 255, 0.2);
}

.tab-item.router-link-exact-active .tab-icon {
  filter: drop-shadow(0 0 6px rgba(255, 255, 255, 0.8));
}

.tab-icon {
  font-size: 15px;
}

.tab-label {
  letter-spacing: 0.02em;
}

.feature-menu {
  position: relative;
}

.feature-trigger {
  font-size: 13px;
}

.feature-dropdown {
  position: absolute;
  top: 100%;
  right: 0;
  padding: 8px;
  border-radius: 14px;
  background: var(--color-background-soft);
  box-shadow:
    0 16px 40px rgba(15, 23, 42, 0.14),
    0 0 0 1px rgba(148, 163, 184, 0.4);
  min-width: 160px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  z-index: 10;
}

.dropdown-item {
  padding: 6px 10px;
  border-radius: 10px;
  font-size: 13px;
  color: var(--color-heading);
}

.dropdown-item:hover {
  background: var(--color-background-mute);
}

.app-main {
  flex: 1;
  padding-bottom: 24px;
}

/* 页面切换动画 */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition:
    opacity 0.25s ease,
    transform 0.25s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(8px);
}

.fade-slide-enter-to,
.fade-slide-leave-from {
  opacity: 1;
  transform: translateY(0);
}

.debug-bar {
  position: sticky;
  bottom: 0;
  margin-top: auto;
  padding-top: 4px;
}

.debug-inner {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 16px;
  align-items: center;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(15, 23, 42, 0.9);
  color: #e5e7eb;
  font-size: 11px;
}

.debug-title {
  font-weight: 600;
}

.debug-item code {
  padding: 1px 4px;
  border-radius: 4px;
  background: rgba(15, 23, 42, 0.75);
  color: #f97316;
}

@media (max-width: 640px) {
  .top-nav-inner {
    padding: 8px 10px;
    gap: 10px;
  }

  .tab-label {
    display: none;
  }

  .nav-row {
    flex-wrap: wrap;
    justify-content: flex-end;
  }

  .tab-item {
    padding-inline: 10px;
  }

  .debug-inner {
    border-radius: 12px;
  }
}
</style>
