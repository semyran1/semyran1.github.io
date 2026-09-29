/* ═══════════════════════════════════════════════════════════════════════════
   Воронка в Яндекс.Метрике: где посетитель отваливается.

   Счётчик уже стоит на страницах; этот файл добавляет к нему события-этапы.
   Цели в интерфейсе Метрики заводить по идентификатору «JavaScript-событие»,
   имена ниже. Полный список и что он значит — README-METRIKA.md.

   Этапы:
     view_hero        открыл сайт (первый экран)
     scroll_25/50/75  долистал до четверти / середины / трёх четвертей
     read_<секция>    секция провисела на экране больше 3 секунд (реально читал)
     play_preview     навёл на кейс и превью проигралось
     click_work       кликнул по работе (YouTube, Яндекс.Диск, кейс)
     click_youtube    кликнул именно по ссылке на YouTube
     cta_price        нажал «узнать стоимость»
     brief_open       открыл бриф
     brief_step_2..6  дошёл до шага брифа
     brief_submit     отправил заявку
     contact_telegram / contact_email  написал напрямую, минуя бриф
   ═══════════════════════════════════════════════════════════════════════════ */
(function () {
  var ID = 111134962;
  var fired = {};
  function goal(name, params) {
    if (fired[name]) return;                 // каждый этап считаем один раз за визит
    fired[name] = true;
    if (typeof ym === "function") ym(ID, "reachGoal", name, params || {});
  }
  window.funnelGoal = function (name, params) {   // для брифа и других страниц
    if (typeof ym === "function") ym(ID, "reachGoal", name, params || {});
  };
  /* какая версия портфолио: /ai — версия под AI-вакансии, корень — основная */
  var version = /\/ai(\/|$)/.test(location.pathname) ? "ai" : "main";
  if (typeof ym === "function") ym(ID, "params", { version: version });

  addEventListener("DOMContentLoaded", function () {
    goal("view_hero");

    /* глубина прокрутки */
    var marks = [[0.25, "scroll_25"], [0.5, "scroll_50"], [0.75, "scroll_75"]];
    addEventListener("scroll", function () {
      var h = document.documentElement.scrollHeight - innerHeight;
      if (h <= 0) return;
      var p = scrollY / h;
      marks.forEach(function (m) { if (p >= m[0]) goal(m[1]); });
    }, { passive: true });

    /* секция считается прочитанной, если провисела на экране 3 секунды */
    document.querySelectorAll("main section[id], footer[id]").forEach(function (sec) {
      var t = null;
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (e.isIntersecting && !t) t = setTimeout(function () { goal("read_" + sec.id); }, 3000);
          if (!e.isIntersecting && t) { clearTimeout(t); t = null; }
        });
      }, { threshold: 0.35 }).observe(sec);
    });

    /* клики по работам и контактам */
    addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest("a[href]");
      if (!a) return;
      var href = a.getAttribute("href") || "";
      if (a.dataset.goal) window.funnelGoal(a.dataset.goal);
      if (/youtu\.?be/.test(href)) { goal("click_youtube"); goal("click_work"); }
      else if (/disk\.yandex|instagram\.com/.test(href)) goal("click_work");
      if (/^mailto:/.test(href)) goal("contact_email");
      if (/t\.me\//.test(href)) goal("contact_telegram");
      if (/brief\.html/.test(href)) goal("brief_open");
    }, true);

    /* превью кейса реально проигралось */
    addEventListener("play", function (e) {
      if (e.target.tagName === "VIDEO" && e.target.classList.contains("sw")) goal("play_preview");
    }, true);
  });
})();
