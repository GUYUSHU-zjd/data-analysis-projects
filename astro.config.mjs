// 📄 astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// ✅ 自动判断是否为开发环境（npm run dev）
const isDev = import.meta.env.DEV;

export default defineConfig({
  // ✅ 修复 site：必须包含完整子路径，否则 canonical、sitemap、OG 链接全错！
  site: 'https://guyushu-zjd.github.io/data-analysis-projects/',

  // ✅ 修复 base：开发环境用 '/'，部署环境用 '/data-analysis-projects/'
  //    → 本地访问 http://localhost:4321/ 即可，无需手动加路径
  base: isDev ? '/' : '/data-analysis-projects/',

  // ✅ 集成 Tailwind（确保已安装 npm install -D @astrojs/tailwind tailwindcss）
  integrations: [tailwind()],

  // ✅ 优化 Vite SSR 配置：确保 Chart.js 在服务端渲染时不被外部化
  vite: {
    ssr: {
      // 使用数组确保类型安全，避免字符串拼写错误
      noExternal: ['chart.js'],
    },
    // 🎯 Bonus 优化：开发体验增强
    server: {
      // 自动打开浏览器（可选）
      // open: true,
      // 端口冲突时自动换端口
      strictPort: false,
      port: 4321, // 保持你习惯的 4321 端口
    },
    // 🎯 Bonus 优化：构建优化
    build: {
      target: 'es2020',
      sourcemap: false, // 生产环境关闭 source map（减小体积）
    },
  },

  // 🎯 Bonus 优化：启用压缩和图片优化（如已安装相应插件）
  // compressHTML: true,
  // image: {
  //   service: {
  //     entrypoint: 'astro/assets/services/sharp',
  //   },
  // },
});