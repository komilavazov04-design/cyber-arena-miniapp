import { appState } from "./state.js";

export function initIntroFlow() {
  const intro = document.getElementById("intro-screen");
  const login = document.getElementById("login-screen");
  const startBtn = document.getElementById("start-btn");

  if (!intro || !login || !startBtn) return;

  startBtn.addEventListener("click", () => {
    if (appState.locked) return;
    appState.locked = true;
    appState.currentScreen = "transition";

    intro.classList.add("is-transitioning");

    setTimeout(() => {
      intro.classList.add("is-hidden");
      login.classList.remove("is-hidden");
      login.classList.add("revealed");
      appState.currentScreen = "login";
      appState.locked = false;
    }, 820);
  });
}
