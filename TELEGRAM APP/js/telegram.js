export function initTelegram() {
  const tg = window.Telegram?.WebApp;
  if (!tg) return null;

  tg.ready();
  tg.expand();

  const theme = tg.themeParams || {};
  if (theme.text_color) document.body.style.color = theme.text_color;

  return tg;
}
