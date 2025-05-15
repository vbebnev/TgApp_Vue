import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { initTelegramWebApp } from './telegram'

const app = createApp(App)

// if(window.Telegram?.WebApp) {
//     window.Telegram.WebApp.ready();
//     window.Telegram.WebApp.expand();
// }
document.addEventListener('DOMContentLoaded', () => {
  initTelegramWebApp()
})
app.use(router)
app.mount('#app')
