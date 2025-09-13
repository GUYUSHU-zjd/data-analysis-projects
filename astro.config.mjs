// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  
  // 添加这行配置，将 /data-analysis-projects/ 替换为你的仓库名
  base: '/data-analysis-projects/',
  
  // 如果你的仓库是 username.github.io，则使用 base: '/'
  // base: '/',
  
  // 设置站点 URL（可选但推荐）
  site: 'https://guyushu-zjd.github.io',
  
  // 确保输出为静态文件
  output: 'static',
});