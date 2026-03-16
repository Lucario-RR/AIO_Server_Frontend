import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/schedule',
      name: 'schedule',
      component: () => import('../views/ScheduleView.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/around',
      name: 'around',
      component: () => import('../views/AroundView.vue'),
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/SettingsView.vue'),
    },
    {
      path: '/blogs',
      name: 'blogs',
      component: () => import('../views/BlogsView.vue'),
    },
    {
      path: '/ledger',
      name: 'ledger',
      component: () => import('../views/LedgerView.vue'),
    },
    {
      path: '/currency',
      name: 'currency',
      component: () => import('../views/CurrencyView.vue'),
    },
    {
      path: '/account',
      name: 'account',
      component: () => import('../views/AccountView.vue'),
    },
    {
      path: '/bike',
      name: 'bike',
      component: () => import('../views/BikeView.vue'),
    },
    {
      path: '/gallery',
      name: 'gallery',
      component: () => import('../views/GalleryView.vue'),
    },
  ],
})

export default router
