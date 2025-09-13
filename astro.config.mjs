import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// 根据环境动态设置 base
const isGitHubPages = process.env.GITHUB_PAGES === 'true';
const base = isGitHubPages ? '/data-analysis-projects/' : '/';

export default defineConfig({
  base,
  site: 'https://GUYUSHU-zjd.github.io',
  integrations: [tailwind()],
  output: 'static'
});