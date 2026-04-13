import { initTelegram } from "./telegram.js";
import { initIntroFlow } from "./intro.js";
import { initLoginActions } from "./login.js";

function bootstrap() {
  initTelegram();
  initIntroFlow();
  initLoginActions();
}

bootstrap();
