import { computed } from 'vue'
import { useSettingsStore } from '@/stores/settings'

const messages = {
  'zh-CN': {
    nav: {
      home: '首页',
      schedule: '日程',
      about: '关于',
      around: '周边',
      settings: '设置',
      features: '功能',
    },
    home: {
      title: 'AIO Server 前端面板',
      subtitle: '为博客、账本、汇率对比、自行车日志和图库提供统一的可视化控制台。',
      modules: {
        blogs: {
          title: 'Blogs',
          desc: '博客列表、详情与编辑器的预留位。未来用于展示和管理你的文章。',
        },
        ledger: {
          title: 'Ledger',
          desc: '账单上传、流水解析与图表统计的入口卡片。适配自动账单解析后端。',
        },
        currency: {
          title: 'Bank Currency',
          desc: '多银行汇率对比与历史曲线展示的预留区域。',
        },
        account: {
          title: 'Account',
          desc: '登录、注册、2FA / Passkey 等账号安全相关页面的聚合入口。',
        },
        bike: {
          title: 'Bike',
          desc: '骑行记录与保养日志的可视化卡片，将来可以展示统计图与地图。',
        },
        gallery: {
          title: 'Gallery',
          desc: '图片展示墙的预留位，用于承载你的相册与插画资源。',
        },
        comingSoon: '即将上线',
      },
    },
    settings: {
      title: '设置',
      subtitle: '先把一些通用偏好先搭好界面，后面再接入真实配置与后端。',
      appearance: {
        title: '外观',
        desc: '控制前端面板的主题和信息密度。',
        themeLabel: '主题模式',
        themeLight: '浅色',
        themeDark: '深色',
        themeSystem: '跟随系统',
        themeHint: '当前仅前端占位，后续会联动全局主题切换。',
        densityLabel: '界面密度',
        densityComfortable: '舒适',
        densityCompact: '紧凑',
        densityHint: '影响列表与表单的垂直间距，方便在笔记本或大屏之间切换。',
      },
      locale: {
        title: '语言与地区',
        desc: '先预留语言与区域设置，后端准备好后对接。',
        languageLabel: '界面语言',
        dateCurrencyLabel: '日期 / 货币格式',
        dateCurrencyValue: '自动根据语言推断（占位中）',
        hint: '后续会根据账本和汇率模块的真实需求来细化。',
      },
      dev: {
        title: '开发者与调试',
        desc: '与 AIO Server 的调试和日志相关设置预留。',
        toggleTitle: '在前端显示调试信息',
        toggleSubtitle: '如当前环境、版本号、后端心跳状态等。',
        previewTitle: '预览（本地状态）',
        preview: {
          theme: '主题',
          language: '语言',
          density: '密度',
          debug: '展示调试信息',
          yes: '是',
          no: '否',
        },
      },
    },
    debugBar: {
      title: '调试信息',
      mode: '前端模式',
      baseUrl: '基础路径',
    },
  },
  'en-US': {
    nav: {
      home: 'Home',
      schedule: 'Schedule',
      about: 'About',
      around: 'Around',
      settings: 'Settings',
      features: 'Features',
    },
    home: {
      title: 'AIO Server Frontend Panel',
      subtitle:
        'Unified visual console for blogs, ledger, currency comparison, bike logs and gallery.',
      modules: {
        blogs: {
          title: 'Blogs',
          desc: 'Placeholder for post list, details and editor. Will manage your articles later.',
        },
        ledger: {
          title: 'Ledger',
          desc: 'Entry card for bill upload, transaction parsing and charting.',
        },
        currency: {
          title: 'Bank Currency',
          desc: 'Reserved area for multi-bank FX comparison and history curves.',
        },
        account: {
          title: 'Account',
          desc: 'Hub for login, registration, 2FA / Passkey and account security pages.',
        },
        bike: {
          title: 'Bike',
          desc: 'Visualization card for ride logs and maintenance records, later with stats/maps.',
        },
        gallery: {
          title: 'Gallery',
          desc: 'Placeholder gallery wall for your photos and illustrations.',
        },
        comingSoon: 'Coming soon',
      },
    },
    settings: {
      title: 'Settings',
      subtitle:
        'Prepare some common preferences UI first, then wire them to real config and backend.',
      appearance: {
        title: 'Appearance',
        desc: 'Control theme and density of the frontend panel.',
        themeLabel: 'Theme mode',
        themeLight: 'Light',
        themeDark: 'Dark',
        themeSystem: 'System',
        themeHint: 'Currently only affects frontend; will drive global theme later.',
        densityLabel: 'Interface density',
        densityComfortable: 'Comfortable',
        densityCompact: 'Compact',
        densityHint:
          'Affects vertical spacing of lists and forms, useful for laptops vs large screens.',
      },
      locale: {
        title: 'Language & region',
        desc: 'Language and region placeholders, to be wired when backend is ready.',
        languageLabel: 'UI language',
        dateCurrencyLabel: 'Date / currency format',
        dateCurrencyValue: 'Infer automatically from language (placeholder)',
        hint: 'Will be refined based on real needs from ledger and currency modules.',
      },
      dev: {
        title: 'Developer & debug',
        desc: 'Reserved options related to debugging and logs of AIO Server.',
        toggleTitle: 'Show debug info in frontend',
        toggleSubtitle: 'Such as current env, version, backend heartbeat, etc.',
        previewTitle: 'Preview (local state)',
        preview: {
          theme: 'Theme',
          language: 'Language',
          density: 'Density',
          debug: 'Show debug info',
          yes: 'Yes',
          no: 'No',
        },
      },
    },
    debugBar: {
      title: 'Debug',
      mode: 'Frontend mode',
      baseUrl: 'Base URL',
    },
  },
}

export function useI18n() {
  const settings = useSettingsStore()
  const locale = computed(() => settings.language)

  const t = (path) => {
    const dict = messages[locale.value] ?? messages['zh-CN']
    return path.split('.').reduce((obj, key) => (obj && obj[key] != null ? obj[key] : null), dict) ?? path
  }

  return { t, locale }
}

