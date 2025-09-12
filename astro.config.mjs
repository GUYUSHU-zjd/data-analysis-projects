import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// 简化配置，移除可能引起问题的复杂配置
export default defineConfig({
  base: '/data-analysis-projects/',
  site: 'https://GUYUSHU-zjd.github.io',
  integrations: [tailwind()],
  // 移除 vite 的复杂配置，使用默认值
});