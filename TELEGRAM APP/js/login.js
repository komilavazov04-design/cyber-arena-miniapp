export function initLoginActions() {
  const telegramBtn = document.getElementById("telegram-login-btn");
  const guestBtn = document.getElementById("guest-login-btn");

  if (telegramBtn) {
    telegramBtn.addEventListener("click", () => {
      console.log("Telegram login bosildi");
    });
  }

  if (guestBtn) {
    guestBtn.addEventListener("click", () => {
      console.log("Guest login bosildi");
    });
  }
}