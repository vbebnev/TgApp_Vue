let webApp = null;

export function initTelegramWebApp() {
  if (typeof window !== 'undefined' && window.Telegram?.WebApp) {
    webApp = window.Telegram.WebApp;
    webApp.expand();
    console.log('[Telegram] WebApp инициализирован:', webApp);
  } else {
    console.warn('[Telegram] WebApp не найден.');
  }
}

export function getTelegramWebApp() {
  return webApp;
}