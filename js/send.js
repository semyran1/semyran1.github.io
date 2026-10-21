/* ═══════════════════════════════════════════════════════════════════════════
   Способы отправить заявку или смету без сервера. Подключается на brief.html и в калькуляторах.

   mail    — письмо с готовым текстом: mailto, а также ссылки на Gmail и Яндекс.Почту (если на
             устройстве нет почтовой программы). Письмо не уходит само: человек нажимает «отправить».
   pdf     — PDF через печать страницы («Сохранить как PDF»). Файл человек отправляет любым способом.
   share   — системное меню «Поделиться» (телефон, часть браузеров): любое установленное приложение.
   copy    — копия текста в буфер.

   Адрес почты берётся из LEAD.MAIL (js/lead.js). Telegram и прямая доставка живут в lead.js.
   ═══════════════════════════════════════════════════════════════════════════ */
(function () {
  var MAIL = (window.LEAD && window.LEAD.MAIL) || "semyran1@gmail.com";
  var MAXBODY = 1800;                       // длинные письма mailto обрезаются клиентами почты
  var CUT = "\n…(текст сокращён; полная версия в PDF или кнопкой «скопировать»)";
  var clip = function (t) { return t.length > MAXBODY ? t.slice(0, MAXBODY) + CUT : t; };
  var qs = function (o) { return Object.keys(o).map(function (k) { return k + "=" + encodeURIComponent(o[k]); }).join("&"); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };

  var style = document.createElement("style");
  style.textContent = "#printsheet{display:none}" +
    "@media print{html,body{background:#fff!important;color:#000!important}body>*:not(#printsheet){display:none!important}" +
    "#printsheet{display:block!important;font:14px/1.55 Manrope,Arial,sans-serif;color:#000;padding:0}" +
    "#printsheet h1{font-size:24px;line-height:1.2;margin:0 0 4px}#printsheet .pm{color:#555;font-size:12px;margin:0 0 18px}" +
    "#printsheet table{border-collapse:collapse;width:100%}#printsheet td{padding:7px 8px;border-bottom:1px solid #bbb;vertical-align:top}" +
    "#printsheet td:first-child{width:34%;color:#555;font-size:12px;text-transform:uppercase;letter-spacing:.04em}" +
    "#printsheet pre{white-space:pre-wrap;font:12.5px/1.5 Menlo,Consolas,monospace;margin:18px 0 0;padding:12px;border:1px solid #bbb}" +
    "#printsheet .pf{margin-top:22px;font-size:12px;color:#555}}";
  document.head.appendChild(style);

  window.SendKit = {
    mail: MAIL,
    mailto: function (subject, body) { return "mailto:" + MAIL + "?" + qs({ subject: subject, body: clip(body) }); },
    gmail: function (subject, body) { return "https://mail.google.com/mail/?" + qs({ view: "cm", fs: "1", to: MAIL, su: subject, body: clip(body) }); },
    yandex: function (subject, body) { return "https://mail.yandex.ru/compose?" + qs({ to: MAIL, subject: subject, body: clip(body) }); },
    canShare: function () { return typeof navigator.share === "function"; },
    share: function (title, text) { try { return navigator.share({ title: title, text: text }).catch(function () {}); } catch (e) { return Promise.resolve(); } },
    /* копия в буфер; возвращает true/false (старые приложения и браузеры отказывают без жеста) */
    copy: async function (text) {
      try { await navigator.clipboard.writeText(text); return true; } catch (e) {}
      try {
        var ta = document.createElement("textarea"); ta.value = text; ta.style.cssText = "position:fixed;opacity:0;top:0"; document.body.appendChild(ta);
        ta.select(); var ok = document.execCommand("copy"); document.body.removeChild(ta); return !!ok;
      } catch (e) { return false; }
    },
    /* PDF: печатный лист + системный диалог «Сохранить как PDF». Название документа становится именем файла. */
    pdf: function (o) {
      var old = document.getElementById("printsheet"); if (old) old.remove();
      var d = new Date(), date = d.toLocaleDateString(o.locale || "ru-RU", { year: "numeric", month: "long", day: "numeric" });
      var rows = (o.rows || []).map(function (r) { return "<tr><td>" + esc(r[0]) + "</td><td>" + esc(r[1]) + "</td></tr>"; }).join("");
      var el = document.createElement("div"); el.id = "printsheet";
      el.innerHTML = "<h1>" + esc(o.heading) + "</h1><p class='pm'>" + esc(o.author || "Серафим Панюшкин") + " · " + esc(date) + "</p>" +
        (rows ? "<table>" + rows + "</table>" : "") + (o.text ? "<pre>" + esc(o.text) + "</pre>" : "") +
        "<p class='pf'>" + esc(location.host) + " · " + esc(MAIL) + " · t.me/semyran</p>";
      document.body.appendChild(el);
      var prev = document.title; document.title = o.filename || o.heading;
      var done = function () { document.title = prev; window.removeEventListener("afterprint", done); };
      window.addEventListener("afterprint", done);
      setTimeout(function () { window.print(); setTimeout(done, 1500); }, 60);
    },
    goal: function (n) { try { if (window.funnelGoal) window.funnelGoal(n); else if (typeof window.ym === "function") window.ym(111134962, "reachGoal", n); } catch (e) {} }
  };
})();
