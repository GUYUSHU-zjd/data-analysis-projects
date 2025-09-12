/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'muted': {
          blue: '#9BB7D4',
          green: '#A5C0B8',
          grey: '#C4C4C4',
          beige: '#D3C0B2',
          dustypink: '#D4A5A5',
          dark: '#495867',
        }
      },
    },
  },
  plugins: [],
}