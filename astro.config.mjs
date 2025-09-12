import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  base: '/data-analysis-projects/',
  site: 'https://GUYUSHU-zjd.github.io',
  integrations: [tailwind()],
  vite: {
    build: {
      rollupOptions: {
        // 确保正确处理文件路径
        external: []
      }
    },
    // 解决 Windows 路径问题
    server: {
      fs: {
        strict: false
      }
    }
  }
});