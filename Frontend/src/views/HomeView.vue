<script setup>
import { useI18n } from '@/i18n'

const { t } = useI18n()
</script>

<template>
  <main class="home-shell">
    <section class="hero">
      <h1 class="hero-title">{{ t('home.title') }}</h1>
      <p class="hero-subtitle">
        {{ t('home.subtitle') }}
      </p>
    </section>

    <section class="modules-grid">
      <article class="module-card">
        <h2>{{ t('home.modules.blogs.title') }}</h2>
        <p>{{ t('home.modules.blogs.desc') }}</p>
        <span class="badge">{{ t('home.modules.comingSoon') }}</span>
      </article>

      <article class="module-card">
        <h2>{{ t('home.modules.ledger.title') }}</h2>
        <p>{{ t('home.modules.ledger.desc') }}</p>
        <span class="badge">{{ t('home.modules.comingSoon') }}</span>
      </article>

      <article class="module-card">
        <h2>{{ t('home.modules.currency.title') }}</h2>
        <p>{{ t('home.modules.currency.desc') }}</p>
        <span class="badge">{{ t('home.modules.comingSoon') }}</span>
      </article>

      <article class="module-card">
        <h2>{{ t('home.modules.account.title') }}</h2>
        <p>{{ t('home.modules.account.desc') }}</p>
        <span class="badge">{{ t('home.modules.comingSoon') }}</span>
      </article>

      <article class="module-card">
        <h2>{{ t('home.modules.bike.title') }}</h2>
        <p>{{ t('home.modules.bike.desc') }}</p>
        <span class="badge">{{ t('home.modules.comingSoon') }}</span>
      </article>

      <article class="module-card">
        <h2>{{ t('home.modules.gallery.title') }}</h2>
        <p>{{ t('home.modules.gallery.desc') }}</p>
        <span class="badge">{{ t('home.modules.comingSoon') }}</span>
      </article>
    </section>
  </main>
</template>

<style scoped>
.home-shell {
  padding-top: 8px;
}

.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 16px;
}

.hero-text {
  flex: 1 1 auto;
}

.hero-title {
  font-size: 26px;
  font-weight: 800;
  letter-spacing: 0.03em;
  margin-bottom: 4px;
}

.hero-subtitle {
  color: #6b7280;
  font-size: 14px;
}

.modules-grid {
  margin-top: 24px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}

.module-card {
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

.module-card h2 {
  font-size: 16px;
  font-weight: 700;
  margin-bottom: 6px;
}

.module-card p {
  font-size: 13px;
  color: #6b7280;
  margin-bottom: 10px;
}

.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 600;
  color: #be185d;
  background: rgba(252, 231, 243, 0.9);
}

.module-card:hover {
  transform: translateY(-4px);
  box-shadow:
    0 14px 30px rgba(15, 23, 42, 0.16),
    0 0 0 1px var(--color-border-hover);
}

@media (max-width: 640px) {
  .hero {
    flex-direction: column;
    align-items: flex-start;
    gap: 12px;
  }

  .hero-title {
    font-size: 22px;
  }

  .hero-subtitle {
    font-size: 13px;
  }

  .modules-grid {
    margin-top: 16px;
    gap: 12px;
  }

  .module-card {
    padding: 14px 14px;
    border-radius: 14px;
  }
}
</style>
