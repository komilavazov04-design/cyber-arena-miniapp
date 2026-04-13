export function initTelegram() {
  const tg = window.Telegram?.WebApp;
  if (!tg) return null;

  tg.ready();
  tg.expand();

  if (tg.setHeaderColor) tg.setHeaderColor("#020814");
  if (tg.setBackgroundColor) tg.setBackgroundColor("#020814");

  return tg;
}