from pathlib import Path

PROJECT_NAME = "TELEGRAM APP"

DIRS = [
    "assets/models",
    "css",
    "js",
]

FILES = {
    "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Cyber Arena</title>

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Orbitron:wght@500;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="./css/base.css" />
  <link rel="stylesheet" href="./css/intro.css" />
  <link rel="stylesheet" href="./css/login.css" />
  <link rel="stylesheet" href="./css/animations.css" />
  <link rel="stylesheet" href="./css/responsive.css" />

  <script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
  <script src="https://telegram.org/js/telegram-web-app.js"></script>
</head>
<body>
  <div id="app">
    <section id="intro-screen" class="screen intro-screen">
      <div class="bg-grid"></div>
      <div class="bg-noise"></div>
      <div class="aurora aurora-1"></div>
      <div class="aurora aurora-2"></div>

      <div class="intro-content">
        <div class="intro-copy">
          <div class="intro-kicker">TELEGRAM MINI APP</div>
          <h1 class="intro-title">CYBER ARENA</h1>
          <p class="intro-subtitle">NEXT-GEN COMPETITIVE GAMING</p>
          <div class="intro-chip">WELCOME // PRESS START</div>
        </div>

        <div class="intro-stage">
          <div class="ring ring-1"></div>
          <div class="ring ring-2"></div>
          <div class="ring-glow"></div>

          <div class="intro-model-shell glass-shell">
            <model-viewer
              id="intro-model"
              class="intro-model"
              src="./assets/models/logo.glb"
              alt="Cyber Arena 3D logo"
              interaction-prompt="none"
              shadow-intensity="1"
              exposure="1"
              environment-image="neutral"
              camera-target="0m 0m 0m"
              camera-orbit="0deg 78deg 6.8m"
              min-camera-orbit="auto auto 6.6m"
              max-camera-orbit="auto auto 6.9m"
              field-of-view="26deg"
              disable-pan
              disable-zoom>
            </model-viewer>
          </div>
        </div>

        <div class="start-wrap">
          <button id="start-btn" class="start-btn">START</button>
        </div>

        <div class="version-tag">— V2.0.1 —</div>
      </div>
    </section>

    <section id="login-screen" class="screen login-screen is-hidden">
      <div class="login-bg">
        <model-viewer
          id="login-model"
          class="login-model"
          src="./assets/models/logo.glb"
          alt="Cyber Arena background 3D logo"
          autoplay
          auto-rotate
          rotation-per-second="5deg"
          interaction-prompt="none"
          shadow-intensity="1"
          exposure="1"
          environment-image="neutral"
          camera-target="0m 0m 0m"
          camera-orbit="0deg 78deg 7.2m"
          field-of-view="28deg"
          disable-pan
          disable-zoom>
        </model-viewer>
      </div>

      <div class="login-overlay"></div>

      <div class="login-content">
        <div class="login-header">
          <div class="login-kicker">ACCESS PANEL</div>
          <h2 class="login-title">Enter Arena</h2>
          <p class="login-subtitle">Glass login card, 3D background, premium cyberpunk vibe.</p>
        </div>

        <div class="login-card glass-card">
          <div class="login-card-top">
            <span class="status-dot"></span>
            <span>SECURE ACCESS</span>
          </div>

          <h3 class="login-card-title">Choose a login method</h3>
          <p class="login-card-text">
            Hozircha starter view. Keyin Telegram auth yoki custom login ulaymiz.
          </p>

          <div class="login-actions">
            <button id="telegram-login-btn" class="glass-btn primary-btn">
              Continue with Telegram
            </button>

            <button id="guest-login-btn" class="glass-btn ghost-btn">
              Enter as Guest
            </button>
          </div>

          <div class="login-footer-note">
            Cyber Arena // secure gateway
          </div>
        </div>
      </div>
    </section>
  </div>

  <script type="module" src="./js/app.js"></script>
</body>
</html>
""",

    "css/base.css": """:root {
  --bg-1: #020814;
  --bg-2: #03111e;
  --bg-3: #06182a;
  --text: #eef6ff;
  --muted: #8fa5ba;
  --cyan: #31d8ff;
  --mint: #2df2c4;
  --blue: #40baff;
  --purple: #7d63ff;
  --line: rgba(110, 220, 255, 0.14);
  --glass: rgba(10, 25, 43, 0.58);
  --glass-2: rgba(10, 25, 43, 0.72);
  --white-line: rgba(255,255,255,0.08);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  min-height: 100%;
}

body {
  font-family: Inter, Arial, sans-serif;
  color: var(--text);
  background:
    radial-gradient(circle at 20% 12%, rgba(42, 214, 255, 0.12), transparent 30%),
    radial-gradient(circle at 82% 20%, rgba(125, 99, 255, 0.10), transparent 28%),
    linear-gradient(180deg, var(--bg-1) 0%, var(--bg-2) 42%, var(--bg-3) 100%);
  overflow-x: hidden;
}

button {
  font: inherit;
  border: none;
  cursor: pointer;
  color: inherit;
}

.screen {
  position: relative;
  min-height: 100dvh;
  width: 100%;
  overflow: hidden;
}

.is-hidden {
  display: none !important;
}

.glass-shell,
.glass-card,
.glass-btn {
  border: 1px solid var(--line);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.05),
    0 20px 44px rgba(0,0,0,0.30);
  backdrop-filter: blur(16px);
}

.bg-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(67, 214, 255, 0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(67, 214, 255, 0.05) 1px, transparent 1px);
  background-size: 28px 28px;
  mask-image: linear-gradient(to bottom, rgba(0,0,0,0.96), rgba(0,0,0,0.55));
}

.bg-noise {
  position: absolute;
  inset: 0;
  opacity: 0.035;
  background-image: radial-gradient(circle, #ffffff 1px, transparent 1px);
  background-size: 20px 20px;
}

.aurora {
  position: absolute;
  border-radius: 999px;
  filter: blur(95px);
  pointer-events: none;
}

.aurora-1 {
  width: 340px;
  height: 340px;
  background: rgba(49, 216, 255, 0.16);
  top: 4%;
  left: 50%;
  transform: translateX(-50%);
}

.aurora-2 {
  width: 280px;
  height: 280px;
  background: rgba(125, 99, 255, 0.14);
  bottom: 10%;
  right: 4%;
}
""",

    "css/intro.css": """.intro-screen {
  display: grid;
  place-items: center;
  padding: 24px 16px;
}

.intro-content {
  position: relative;
  z-index: 2;
  width: min(100%, 420px);
  text-align: center;
}

.intro-copy {
  animation: screenEnter .75s cubic-bezier(.2,.8,.2,1);
}

.intro-kicker {
  font-family: Orbitron, Arial, sans-serif;
  letter-spacing: 0.22em;
  font-size: 0.82rem;
  color: var(--cyan);
}

.intro-title {
  margin-top: 14px;
  font-family: Orbitron, Arial, sans-serif;
  font-size: clamp(2.4rem, 10vw, 4.2rem);
  line-height: 0.94;
  font-weight: 800;
  letter-spacing: 0.10em;
  text-shadow:
    0 0 18px rgba(49, 216, 255, 0.18),
    0 0 34px rgba(49, 216, 255, 0.12);
}

.intro-subtitle {
  margin-top: 12px;
  color: var(--muted);
  font-family: Orbitron, Arial, sans-serif;
  font-size: 1rem;
  letter-spacing: 0.14em;
}

.intro-chip {
  width: fit-content;
  margin: 20px auto 0;
  padding: 11px 18px;
  border-radius: 18px;
  background: rgba(11, 26, 44, 0.46);
  border: 1px solid rgba(67, 214, 255, 0.12);
  font-family: Orbitron, Arial, sans-serif;
  font-size: 0.76rem;
  letter-spacing: 0.12em;
  color: #dff8ff;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.04),
    0 10px 28px rgba(0,0,0,0.20);
}

.intro-stage {
  position: relative;
  margin: 34px auto 0;
  width: min(100%, 390px);
  height: 320px;
  display: grid;
  place-items: center;
}

.intro-model-shell {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 100%;
  overflow: hidden;
  border-radius: 32px;
  background:
    radial-gradient(circle at center, rgba(49, 216, 255, 0.10), transparent 38%),
    linear-gradient(180deg, rgba(8, 18, 30, 0.86), rgba(7, 14, 28, 0.92));
}

.intro-model-shell::after {
  content: "";
  position: absolute;
  inset: 0;
  background:
    linear-gradient(135deg, rgba(255,255,255,0.03), transparent 30%, rgba(125,99,255,0.04));
  pointer-events: none;
}

.intro-model {
  width: 100%;
  height: 100%;
  display: block;
  background: transparent;
  --poster-color: transparent;
}

.ring,
.ring-glow {
  position: absolute;
  border-radius: 999px;
}

.ring {
  border: 1px solid rgba(49, 216, 255, 0.26);
  box-shadow: 0 0 20px rgba(49, 216, 255, 0.10);
  z-index: 1;
}

.ring-1 {
  width: 188px;
  height: 188px;
  top: -20px;
  animation: spinClockwise 10s linear infinite;
}

.ring-2 {
  width: 248px;
  height: 248px;
  top: -50px;
  animation: spinCounter 14s linear infinite;
}

.ring-glow {
  width: 130px;
  height: 130px;
  top: 8px;
  background: radial-gradient(circle, rgba(49, 216, 255, 0.22), transparent 70%);
  filter: blur(18px);
  z-index: 0;
  animation: pulseGlow 3.6s ease-in-out infinite;
}

.start-wrap {
  margin-top: 26px;
  animation: screenEnter .9s cubic-bezier(.2,.8,.2,1);
}

.start-btn {
  position: relative;
  width: min(100%, 320px);
  min-height: 62px;
  overflow: hidden;
  border-radius: 24px;
  font-family: Orbitron, Arial, sans-serif;
  font-size: 1.02rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  background:
    linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02)),
    linear-gradient(135deg, rgba(49,216,255,0.22), rgba(125,99,255,0.24));
  border: 1px solid rgba(255,255,255,0.10);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.12),
    inset 0 -1px 0 rgba(255,255,255,0.03),
    0 16px 34px rgba(0,0,0,0.26),
    0 0 24px rgba(49,216,255,0.10);
  transition: transform .28s ease, box-shadow .28s ease, border-color .28s ease;
}

.start-btn::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg, transparent 20%, rgba(255,255,255,0.18) 50%, transparent 80%);
  transform: translateX(-120%);
  transition: transform .8s ease;
}

.start-btn:hover {
  transform: translateY(-2px) scale(1.015);
  border-color: rgba(49, 216, 255, 0.20);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.12),
    0 18px 38px rgba(0,0,0,0.28),
    0 0 30px rgba(49,216,255,0.14);
}

.start-btn:hover::before {
  transform: translateX(120%);
}

.version-tag {
  margin-top: 32px;
  color: rgba(143, 165, 186, 0.72);
  font-family: Orbitron, Arial, sans-serif;
  font-size: 0.74rem;
  letter-spacing: 0.16em;
}

.intro-screen.is-transitioning .intro-copy,
.intro-screen.is-transitioning .start-wrap,
.intro-screen.is-transitioning .version-tag {
  animation: introTextOut .35s ease forwards;
}

.intro-screen.is-transitioning .intro-stage {
  animation: introStageZoom .95s cubic-bezier(.2,.8,.2,1) forwards;
}
""",

    "css/login.css": """.login-screen {
  display: grid;
  place-items: center;
  padding: 24px 16px;
  background:
    radial-gradient(circle at 20% 14%, rgba(49,216,255,0.10), transparent 25%),
    linear-gradient(180deg, rgba(3,9,19,0.86), rgba(3,9,19,0.94));
}

.login-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
  overflow: hidden;
}

.login-model {
  position: absolute;
  inset: 0;
  width: 120%;
  height: 110%;
  left: -10%;
  top: -2%;
  opacity: 0.52;
  filter: blur(0.2px);
  --poster-color: transparent;
}

.login-overlay {
  position: absolute;
  inset: 0;
  z-index: 1;
  background:
    radial-gradient(circle at center, rgba(3,9,19,0.16), rgba(3,9,19,0.62)),
    linear-gradient(180deg, rgba(3,9,19,0.26), rgba(3,9,19,0.78));
}

.login-content {
  position: relative;
  z-index: 2;
  width: min(100%, 420px);
}

.login-header {
  text-align: center;
  margin-bottom: 22px;
  animation: screenEnter .55s cubic-bezier(.2,.8,.2,1);
}

.login-kicker {
  color: var(--cyan);
  font-family: Orbitron, Arial, sans-serif;
  font-size: 0.8rem;
  letter-spacing: 0.18em;
}

.login-title {
  margin-top: 10px;
  font-family: Orbitron, Arial, sans-serif;
  font-size: clamp(2rem, 8vw, 3rem);
  letter-spacing: 0.10em;
  text-shadow: 0 0 16px rgba(49,216,255,0.16);
}

.login-subtitle {
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.5;
}

.login-card {
  padding: 22px;
  border-radius: 28px;
  background:
    linear-gradient(180deg, rgba(10,25,43,0.58), rgba(10,25,43,0.76)),
    linear-gradient(135deg, rgba(49,216,255,0.05), rgba(125,99,255,0.04));
  animation: screenEnter .8s cubic-bezier(.2,.8,.2,1);
}

.login-card-top {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.06);
  color: #dff8ff;
  font-family: Orbitron, Arial, sans-serif;
  font-size: 0.72rem;
  letter-spacing: 0.14em;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: var(--mint);
  box-shadow: 0 0 16px var(--mint);
}

.login-card-title {
  margin-top: 18px;
  font-size: 1.35rem;
  font-weight: 700;
}

.login-card-text {
  margin-top: 10px;
  color: var(--muted);
  line-height: 1.55;
}

.login-actions {
  display: grid;
  gap: 12px;
  margin-top: 22px;
}

.glass-btn {
  min-height: 56px;
  border-radius: 18px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}

.glass-btn:hover {
  transform: translateY(-1px);
}

.primary-btn {
  background:
    linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02)),
    linear-gradient(135deg, rgba(49,216,255,0.18), rgba(45,242,196,0.12));
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.10),
    0 10px 28px rgba(0,0,0,0.22),
    0 0 22px rgba(49,216,255,0.08);
  font-weight: 700;
}

.ghost-btn {
  color: #dcecff;
}

.login-footer-note {
  margin-top: 18px;
  color: rgba(143, 165, 186, 0.72);
  text-align: center;
  font-family: Orbitron, Arial, sans-serif;
  font-size: 0.72rem;
  letter-spacing: 0.14em;
}
""",

    "css/animations.css": """@keyframes spinClockwise {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

@keyframes spinCounter {
  from { transform: rotate(360deg); }
  to { transform: rotate(0deg); }
}

@keyframes pulseGlow {
  0%, 100% {
    opacity: 0.52;
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(1.16);
  }
}

@keyframes auroraFloat1 {
  0%, 100% {
    transform: translateX(-50%) translateY(0) scale(1);
    opacity: 0.74;
  }
  50% {
    transform: translateX(-47%) translateY(14px) scale(1.12);
    opacity: 1;
  }
}

@keyframes auroraFloat2 {
  0%, 100% {
    transform: translate(0, 0) scale(1);
    opacity: 0.68;
  }
  50% {
    transform: translate(-18px, -16px) scale(1.14);
    opacity: 1;
  }
}

@keyframes screenEnter {
  from {
    opacity: 0;
    transform: translateY(16px) scale(0.985);
    filter: blur(6px);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
}

@keyframes introTextOut {
  to {
    opacity: 0;
    transform: translateY(-16px);
    filter: blur(8px);
  }
}

@keyframes introStageZoom {
  0% {
    opacity: 1;
    transform: scale(1);
    filter: blur(0);
  }
  65% {
    opacity: 1;
    transform: scale(1.18);
    filter: blur(0.5px);
  }
  100% {
    opacity: 0;
    transform: scale(1.36);
    filter: blur(7px);
  }
}

@keyframes loginReveal {
  from {
    opacity: 0;
    transform: scale(1.03);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.aurora-1 {
  animation: auroraFloat1 8s ease-in-out infinite;
}

.aurora-2 {
  animation: auroraFloat2 9s ease-in-out infinite;
}

.login-screen.revealed {
  animation: loginReveal .7s ease;
}
""",

    "css/responsive.css": """@media (max-width: 480px) {
  .intro-content,
  .login-content {
    width: min(100%, 390px);
  }

  .intro-stage {
    height: 300px;
  }

  .intro-model-shell {
    border-radius: 28px;
  }

  .intro-title {
    font-size: clamp(2.1rem, 12vw, 3.4rem);
  }

  .login-card {
    padding: 18px;
    border-radius: 24px;
  }

  .start-btn {
    min-height: 58px;
  }
}

@media (min-width: 700px) {
  .intro-content,
  .login-content {
    width: min(100%, 460px);
  }

  .intro-stage {
    height: 360px;
  }
}
""",

    "js/state.js": """export const appState = {
  currentScreen: "intro",
  locked: false,
};
""",

    "js/telegram.js": """export function initTelegram() {
  const tg = window.Telegram?.WebApp;
  if (!tg) return null;

  tg.ready();
  tg.expand();

  const theme = tg.themeParams || {};
  if (theme.text_color) document.body.style.color = theme.text_color;

  return tg;
}
""",

    "js/intro.js": """import { appState } from "./state.js";

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
""",

    "js/login.js": """export function initLoginActions() {
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
""",

    "js/app.js": """import { initTelegram } from "./telegram.js";
import { initIntroFlow } from "./intro.js";
import { initLoginActions } from "./login.js";

function bootstrap() {
  initTelegram();
  initIntroFlow();
  initLoginActions();
}

bootstrap();
""",

    "README.md": """# Cyber Arena - Phase 1

Flow:
1. Intro screen
2. Static 3D logo + rotating rings
3. Start button
4. Login screen
5. Backgroundda slow 3D logo + glass login card

## Important
3D model faylini shu joyga qo'y:
assets/models/logo.glb

## Run
Live Server bilan och.
""",
}


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"[create] {path}")


def print_tree(root: Path, prefix: str = "") -> None:
    items = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    total = len(items)

    for i, item in enumerate(items, start=1):
        connector = "└── " if i == total else "├── "
        print(prefix + connector + item.name)

        if item.is_dir():
            extension = "    " if i == total else "│   "
            print_tree(item, prefix + extension)


def main() -> None:
    base = Path.cwd() / PROJECT_NAME
    base.mkdir(parents=True, exist_ok=True)

    for directory in DIRS:
        target = base / directory
        target.mkdir(parents=True, exist_ok=True)
        print(f"[dir] {target}")

    for relative_path, content in FILES.items():
        write_file(base / relative_path, content)

    print("\\nProject tree:\\n")
    print(base.name)
    print_tree(base)

    print("\\nDone bro ✅")
    print(f"Project location: {base}")


if __name__ == "__main__":
    main()
