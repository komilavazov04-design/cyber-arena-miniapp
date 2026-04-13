export function initLoginActions() {
  const telegramBtn = document.getElementById("telegram-login-btn");
  const guestBtn = document.getElementById("guest-login-btn");

  if (telegramBtn) {
    telegramBtn.addEventListener("click", () => {
      window.alert("Keyingi stepda Telegram auth ulaymiz bro ✅");
    });
  }

  if (guestBtn) {
    guestBtn.addEventListener("click", () => {
      window.alert("Keyingi stepda guest view yoki main menu transition qilamiz bro ✅");
    });
  }
}
