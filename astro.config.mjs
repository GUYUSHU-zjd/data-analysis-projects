// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// 根据环境变量动态设置 base 路径
const isGitHubPages = process.env.GITHUB_PAGES === 'true';
const base = isGitHubPages ? '/data-analysis-projects/' : '/';

export default defineConfig({
  integrations: [tailwind()],
  base: base, // 动态设置 base 路径
  site: 'https://guyushu-zjd.github.io',
  output: 'static',
  trailingSlash: 'always',
  outDir: 'dist',
  vite: {
    build: {
      cssCodeSplit: false, // 禁用 CSS 代码分割，解决预加载问题
    },
  },
});