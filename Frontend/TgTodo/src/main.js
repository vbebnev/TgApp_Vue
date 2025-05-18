import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { initTelegramWebApp } from './telegram'

const app = createApp(App)

if(window.Telegram?.WebApp) {
    console.log('Telega is here')
    window.Telegram.WebApp.ready();
    window.Telegram.WebApp.expand();
}
else {
  console.log("Telega isn''t here")
}
document.addEventListener('DOMContentLoaded', () => {
  initTelegramWebApp()
})
app.use(router)
app.mount('#app')
