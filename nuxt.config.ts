// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: [
    'normalize.css',
  ],modules: [
    ['@nuxtjs/google-fonts', {
        families: {
          Inter: [400, 500, 900],
        }
    }],
  ],
})
