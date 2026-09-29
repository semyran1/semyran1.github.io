/* ═══════════════════════════════════════════════════════════════════════════
   Доставка заявки из брифа. ЕДИНСТВЕННОЕ место, где меняются адреса.

   TG_ENDPOINT   — адрес Cloudflare Worker, который пересылает заявку в Telegram.
                   Инструкция и код воркера: tools/telegram-worker.js
   FORM_ENDPOINT — адрес формы Formspree, письмо приходит на почту.
                   Завести на formspree.io, вставить сюда «https://formspree.io/f/xxxxxxx».

   Пока оба поля пустые, бриф работает по запасному пути: собирает текст заявки,
   копирует его в буфер и открывает чат Telegram — клиент вставляет и отправляет.
   ═══════════════════════════════════════════════════════════════════════════ */
window.LEAD = {
  TG_ENDPOINT: "",
  FORM_ENDPOINT: "",
  TG_CHAT: "https://t.me/semyran",
  MAIL: "semyran1@gmail.com",
};

/* Отправляет заявку всеми настроенными путями сразу.
   Возвращает {sent:[...], failed:[...], fallback:true|false} */
window.sendLead = async function (fields, text) {
  const L = window.LEAD, sent = [], failed = [];
  const jobs = [];
  if (L.TG_ENDPOINT) jobs.push(["telegram", fetch(L.TG_ENDPOINT, {
    method: "POST", headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text, fields, page: location.href, ref: document.referrer })
  })]);
  if (L.FORM_ENDPOINT) jobs.push(["email", fetch(L.FORM_ENDPOINT, {
    method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify(Object.assign({ _subject: "Заявка с сайта: расчёт стоимости", text, page: location.href }, fields))
  })]);
  for (const [name, p] of jobs) {
    try { const r = await p; (r.ok ? sent : failed).push(name); }
    catch (e) { failed.push(name); }
  }
  return { sent, failed, fallback: jobs.length === 0 || sent.length === 0 };
};
