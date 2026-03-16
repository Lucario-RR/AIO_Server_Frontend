<script setup>
import { storeToRefs } from 'pinia'
import { useSettingsStore } from '@/stores/settings'
import { useI18n } from '@/i18n'

const { t } = useI18n()
const settingsStore = useSettingsStore()
const { theme, language, density, showDebugInfo } = storeToRefs(settingsStore)
</script>

<template>
  <section class="page-shell">
    <header class="page-header">
      <div>
        <h1 class="page-title">{{ t('settings.title') }}</h1>
        <p class="page-subtitle">
          {{ t('settings.subtitle') }}
        </p>
      </div>
    </header>

    <section class="settings-grid">
      <!-- 外观设置 -->
      <article class="settings-card">
        <h2 class="card-title">{{ t('settings.appearance.title') }}</h2>
        <p class="card-desc">
          {{ t('settings.appearance.desc') }}
        </p>

        <div class="field-group">
          <label class="field-label">{{ t('settings.appearance.themeLabel') }}</label>
          <div class="segmented-control" role="radiogroup">
            <button
              type="button"
              class="segment"
              :class="{ active: theme === 'light' }"
              @click="theme = 'light'"
            >
              {{ t('settings.appearance.themeLight') }}
            </button>
            <button
              type="button"
              class="segment"
              :class="{ active: theme === 'dark' }"
              @click="theme = 'dark'"
            >
              {{ t('settings.appearance.themeDark') }}
            </button>
            <button
              type="button"
              class="segment"
              :class="{ active: theme === 'system' }"
              @click="theme = 'system'"
            >
              {{ t('settings.appearance.themeSystem') }}
            </button>
          </div>
          <p class="field-hint">
            {{ t('settings.appearance.themeHint') }}
          </p>
        </div>

        <div class="field-group">
          <label class="field-label">{{ t('settings.appearance.densityLabel') }}</label>
          <select v-model="density" class="select">
            <option value="comfortable">
              {{ t('settings.appearance.densityComfortable') }}
            </option>
            <option value="compact">
              {{ t('settings.appearance.densityCompact') }}
            </option>
          </select>
          <p class="field-hint">
            {{ t('settings.appearance.densityHint') }}
          </p>
        </div>
      </article>

      <!-- 语言与地区 -->
      <article class="settings-card">
        <h2 class="card-title">{{ t('settings.locale.title') }}</h2>
        <p class="card-desc">
          {{ t('settings.locale.desc') }}
        </p>

        <div class="field-group">
          <label class="field-label">{{ t('settings.locale.languageLabel') }}</label>
          <select v-model="language" class="select">
            <option value="zh-CN">简体中文</option>
            <option value="en-US">English (US)</option>
          </select>
          <p class="field-hint">
            {{ t('settings.locale.hint') }}
          </p>
        </div>

        <div class="field-group">
          <label class="field-label">{{ t('settings.locale.dateCurrencyLabel') }}</label>
          <p class="fake-input">
            {{ t('settings.locale.dateCurrencyValue') }}
          </p>
          <p class="field-hint">
            {{ t('settings.locale.hint') }}
          </p>
        </div>
      </article>

      <!-- 开发者选项 / 调试 -->
      <article class="settings-card">
        <h2 class="card-title">{{ t('settings.dev.title') }}</h2>
        <p class="card-desc">
          {{ t('settings.dev.desc') }}
        </p>

        <label class="toggle-row">
          <input v-model="showDebugInfo" type="checkbox" class="toggle-input" />
          <span class="toggle-switch" aria-hidden="true"></span>
          <span class="toggle-text">
            <span class="toggle-title">{{ t('settings.dev.toggleTitle') }}</span>
            <span class="toggle-subtitle">
              {{ t('settings.dev.toggleSubtitle') }}
            </span>
          </span>
        </label>

        <div class="preview-box">
          <p class="preview-title">{{ t('settings.dev.previewTitle') }}</p>
          <ul class="preview-list">
            <li>
              {{ t('settings.dev.preview.theme') }}：{{ theme }}
            </li>
            <li>
              {{ t('settings.dev.preview.language') }}：{{ language }}
            </li>
            <li>
              {{ t('settings.dev.preview.density') }}：{{ density }}
            </li>
            <li>
              {{ t('settings.dev.preview.debug') }}：{{
                showDebugInfo ? t('settings.dev.preview.yes') : t('settings.dev.preview.no')
              }}
            </li>
          </ul>
        </div>
      </article>
    </section>
  </section>
</template>

<style scoped>
.page-shell {
  padding: 32px 0;
}

.page-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 24px;
}

.page-title {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 4px;
}

.page-subtitle {
  color: #6b7280;
  font-size: 14px;
}

.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 18px;
}

.settings-card {
  padding: 16px 18px;
  border-radius: 18px;
  background: var(--color-background-soft);
  box-shadow:
    0 10px 25px rgba(15, 23, 42, 0.08),
    0 0 0 1px var(--color-border);
  transition:
    transform 0.18s ease,
    box-shadow 0.18s ease,
    background-color 0.18s ease;
}

.card-title {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 4px;
}

.card-desc {
  font-size: 13px;
  color: #6b7280;
  margin-bottom: 12px;
}

.field-group {
  margin-top: 10px;
}

.field-label {
  display: block;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 6px;
}

.field-hint {
  margin-top: 4px;
  font-size: 12px;
  color: #6b7280;
}

.segmented-control {
  display: inline-flex;
  padding: 2px;
  border-radius: 999px;
  background: #f3f4f6;
  box-shadow: inset 0 0 0 1px rgba(148, 163, 184, 0.4);
}

.segment {
  border: none;
  background: transparent;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  cursor: pointer;
  color: #4b5563;
  transition:
    background-color 0.16s ease,
    color 0.16s ease,
    box-shadow 0.16s ease;
}

.segment.active {
  background: #ffffff;
  color: #111827;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.16);
}

.select {
  width: 100%;
  padding: 6px 10px;
  border-radius: 10px;
  border: 1px solid #d1d5db;
  font-size: 13px;
}

.fake-input {
  padding: 6px 10px;
  border-radius: 10px;
  border: 1px dashed #d1d5db;
  font-size: 13px;
  color: #6b7280;
  background: #f9fafb;
}

.toggle-row {
  margin-top: 8px;
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  user-select: none;
}

.toggle-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.toggle-switch {
  width: 42px;
  height: 24px;
  border-radius: 999px;
  background: #e5e7eb;
  position: relative;
  box-shadow: inset 0 0 0 1px rgba(148, 163, 184, 0.7);
  transition: background-color 0.18s ease;
}

.toggle-switch::after {
  content: '';
  position: absolute;
  top: 3px;
  left: 3px;
  width: 18px;
  height: 18px;
  border-radius: 999px;
  background: #ffffff;
  box-shadow: 0 1px 3px rgba(15, 23, 42, 0.25);
  transition: transform 0.18s ease;
}

.toggle-input:checked + .toggle-switch {
  background: #22c55e;
}

.toggle-input:checked + .toggle-switch::after {
  transform: translateX(18px);
}

.toggle-text {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.toggle-title {
  font-size: 13px;
  font-weight: 600;
}

.toggle-subtitle {
  font-size: 12px;
  color: #6b7280;
}

.preview-box {
  margin-top: 14px;
  padding: 10px 12px;
  border-radius: 12px;
  background: #f9fafb;
  border: 1px dashed #d1d5db;
}

.preview-title {
  font-size: 12px;
  font-weight: 600;
  margin-bottom: 4px;
  color: #6b7280;
}

.preview-list {
  font-size: 12px;
  color: #374151;
  padding-left: 16px;
}

@media (max-width: 640px) {
  .page-shell {
    padding-top: 20px;
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .settings-grid {
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .settings-card {
    padding: 14px 14px;
    border-radius: 14px;
  }
}

.settings-card:hover {
  transform: translateY(-3px);
  box-shadow:
    0 12px 28px rgba(15, 23, 42, 0.14),
    0 0 0 1px var(--color-border-hover);
}
</style>

