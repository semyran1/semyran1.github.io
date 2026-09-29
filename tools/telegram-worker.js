/* ═══════════════════════════════════════════════════════════════════════════
   Cloudflare Worker: принимает заявку с сайта и присылает её в Telegram.

   Зачем нужен: токен бота нельзя класть в код сайта — его увидит любой
   посетитель. Воркер держит токен у себя, сайт просто стучится к воркеру.

   Как поставить (10 минут, всё в браузере):

   1. Бот. В Telegram напишите @BotFather → /newbot → имя и username бота.
      BotFather пришлёт токен вида 1234567890:AA... — он понадобится в шаге 3.
   2. Ваш chat_id. Напишите @userinfobot → он ответит числом Id. Это ваш chat_id.
      Затем откройте своего нового бота и нажмите «Старт», иначе он не сможет
      вам писать.
   3. Воркер. dash.cloudflare.com → Workers & Pages → Create → Start with Hello
      World → Deploy. Затем Edit code: удалите пример, вставьте этот файл, Deploy.
   4. Секреты. В воркере: Settings → Variables and Secrets → Add:
      BOT_TOKEN = токен из шага 1, CHAT_ID = число из шага 2. Тип — Secret. Deploy.
   5. Адрес. Скопируйте адрес воркера (вида https://имя.ваш-аккаунт.workers.dev)
      и пришлите мне — я вставлю его в js/lead.js в поле TG_ENDPOINT.
      Или вставьте сами: это единственная строчка, которую нужно поменять.

   Проверка: откройте адрес воркера в браузере — должно ответить «lead worker ok».
   ═══════════════════════════════════════════════════════════════════════════ */

const ALLOWED = [
  "https://semyran1.github.io",
  "http://localhost:8080",
];

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const cors = {
      "Access-Control-Allow-Origin": ALLOWED.includes(origin) ? origin : ALLOWED[0],
      "Access-Control-Allow-Methods": "POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };
    if (request.method === "OPTIONS") return new Response(null, { headers: cors });
    if (request.method !== "POST") return new Response("lead worker ok", { headers: cors });
    if (origin && !ALLOWED.includes(origin)) return new Response("no", { status: 403, headers: cors });

    let data = {};
    try { data = await request.json(); } catch (e) {}
    const text = String(data.text || "").slice(0, 3500);
    if (!text) return new Response("empty", { status: 400, headers: cors });

    const message = text + "\n\nстраница: " + String(data.page || "—").slice(0, 300) +
                    (data.ref ? "\nпришёл с: " + String(data.ref).slice(0, 300) : "");

    const tg = await fetch(`https://api.telegram.org/bot${env.BOT_TOKEN}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ chat_id: env.CHAT_ID, text: message, disable_web_page_preview: true }),
    });

    return new Response(JSON.stringify({ ok: tg.ok }), {
      status: tg.ok ? 200 : 502,
      headers: { ...cors, "Content-Type": "application/json" },
    });
  },
};
