#!/usr/bin/env python3
"""Собирает страницы Nexora из общих шапки, меню и подвала. Запуск: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
BRAND = "Nexora"
TG = "@Nexora_Dana"
TG_URL = "https://t.me/Nexora_Dana"
WA = "+34 684 748 027"
WA_URL = "https://wa.me/34684748027"
DOMAIN = "https://nexora-dana.eu"

HEAD = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="index,follow">
<title>{title} — {brand}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0E0F13">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{title} — {brand}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_RU">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@1,600&display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/flag-icons@7.2.3/css/flag-icons.min.css">
<link rel="stylesheet" href="assets/style.css?v=live-1">
</head>
<body>
<header class="top">
  <div class="wrap">
    <a class="logo" href="index.html"><i></i>{brand}</a>
    <div class="lang" aria-label="Общаемся по-русски и по-испански"><span>RU / ES</span></div>
    <a class="ico" href="{tg_url}" target="_blank" rel="noopener noreferrer" aria-label="Написать в Telegram">✈</a>
    <a class="ico" href="{wa_url}" target="_blank" rel="noopener noreferrer" aria-label="Написать в WhatsApp">☏</a>
    <a class="btn sm" href="contacts.html#form">Подобрать ВНЖ</a>
    <button class="burger" type="button" aria-label="Меню" aria-expanded="false"><span></span></button>
  </div>
</header>
<div class="menu" hidden>
  <nav class="menu-panel" aria-label="Меню">
    <div class="menu-head"><span class="logo"><i></i>{brand}</span><button class="menu-close" type="button" aria-label="Закрыть">×</button></div>
    <a class="item" href="services.html"><span>Услуги ВНЖ<small>По всем странам Европы</small></span>→</a>
    <a class="item" href="about.html"><span>О бюро<small>Кто мы и как работаем</small></span>→</a>
    <a class="item" href="contacts.html"><span>Контакты<small>Telegram и WhatsApp</small></span>→</a>
    <div class="menu-foot">
      <a class="btn" href="contacts.html#form">Бесплатный разбор</a>
      <a href="{tg_url}" target="_blank" rel="noopener noreferrer">Telegram {tg}</a>
      <a href="{wa_url}" target="_blank" rel="noopener noreferrer">WhatsApp {wa}</a>
      <span>Общаемся по-русски и по-испански</span>
    </div>
  </nav>
</div>
<main>
"""

FOOT = """</main>
<footer>
  <div class="wrap">
    <div style="display:grid;gap:10px"><span class="logo"><i></i>{brand}</span><span>Сопровождение от первого ВНЖ до гражданства в странах Европы. Работаем дистанционно.</span><span>DANA LEGAL CONSULTING S.L. · NIF B09790213</span><span>Avenida Cánovas del Castillo, 14, 1º derecha, Marbella</span></div>
    <nav><a href="services.html">Услуги ВНЖ</a><a href="about.html">О бюро</a><a href="contacts.html">Контакты</a></nav>
    <div style="display:grid;gap:8px"><a href="{tg_url}" target="_blank" rel="noopener noreferrer">Telegram {tg}</a><a href="{wa_url}" target="_blank" rel="noopener noreferrer">WhatsApp {wa}</a></div>
  </div>
</footer>
<script src="assets/main.js?v=live-1"></script>
</body>
</html>
"""

FORM = """<section id="form">
  <div class="wrap">
    <div class="lead-box rv">
      <div class="txt">
        <span class="eyebrow">Бесплатно и без обязательств</span>
        <h2>Подберём страну и основание <em>под вашу ситуацию</em></h2>
        <p class="muted">Расскажите коротко, откуда вы, чем занимаетесь и куда хотите переехать. Специалист разберёт ситуацию, назовёт рабочие варианты и первые шаги. Ответим в течение рабочего дня.</p>
        <p class="muted">Общаемся по-русски и по-испански.</p>
      </div>
      <div>
        <form class="lead" action="{wa_url}" method="get" target="_blank" rel="noopener noreferrer">
          <label for="{p}-name">Как к вам обращаться<input id="{p}-name" name="name" type="text" autocomplete="given-name" maxlength="100" placeholder="Имя"></label>
          <label for="{p}-situation">Коротко о вашей ситуации<textarea id="{p}-situation" name="situation" rows="4" maxlength="2000" placeholder="Где живёте, куда хотите переехать и какая помощь нужна"></textarea></label>
          <p class="form-note" id="{p}-note">Откроется WhatsApp с текстом заявки. Нажмите «Отправить» в чате, чтобы передать её специалисту.</p>
          <button class="btn" type="submit" aria-describedby="{p}-note">Продолжить в WhatsApp</button>
          <a class="form-alternative" href="{tg_url}" target="_blank" rel="noopener noreferrer">Или написать в Telegram →</a>
        </form>
        <noscript><p><a href="{wa_url}">Написать напрямую в WhatsApp</a></p></noscript>
      </div>
    </div>
  </div>
</section>
"""

PATH = """<ol class="path">
  <li class="rv"><h3>Подбор ВНЖ</h3><p>Сравниваем страны и основания под ваш доход, работу и семью. Выбираем путь, у которого больше всего опоры в законе.</p></li>
  <li class="rv"><h3>Накопление срока</h3><p>Получение ВНЖ, продления и смена основания вовремя. Следим, чтобы отъезды не прервали стаж проживания.</p></li>
  <li class="rv"><h3>Досье на гражданство</h3><p>Собираем документы о проживании, доходах, налогах и интеграции. Готовим переводы и легализацию.</p></li>
  <li class="rv"><h3>Экзамены</h3><p>Готовим к экзаменам по языку и знанию страны: какой уровень нужен, где сдавать, как подготовиться.</p></li>
  <li class="rv"><h3>Подача на гражданство</h3><p>Подаём заявление, отвечаем на запросы ведомства и ведём дело до решения.</p></li>
</ol>"""

COUNTRIES = [("es","Испания"),("pt","Португалия"),("it","Италия"),("fr","Франция"),("de","Германия"),("nl","Нидерланды"),("at","Австрия"),("gr","Греция"),("cy","Кипр"),("mt","Мальта"),("hr","Хорватия"),("sk","Словакия"),("cz","Чехия"),("pl","Польша"),("hu","Венгрия"),("me","Черногория"),("rs","Сербия")]
COUNTRY_GRID = '<div class="countries rv">' + "".join(f'<a class="country" href="services.html#countries"><span class="fl fi fi-{f}"></span>{n}</a>' for f, n in COUNTRIES) + '<a class="country more" href="contacts.html#form"><span class="fl plus">+</span>Другие страны</a></div>'

PAY = """<div class="pay">
  <div class="rv"><small>Этап 1 · старт</small><b>50%</b><p class="muted">Берём дело в работу: стратегия, расчёт требований, список документов.</p></div>
  <div class="rv"><small>Этап 2 · подача</small><b>+25%</b><p class="muted">Когда документы подготовлены и поданы.</p></div>
  <div class="rv"><small>Этап 3 · результат</small><b>+25%</b><p class="muted">Только после положительного решения.</p></div>
</div>
<p class="pay-note">Этапы, суммы и условия возврата фиксируем в договоре до первой оплаты. Госпошлины, переводы и легализацию документов оплачиваете отдельно, по квитанциям. Стоимость называем после бесплатного разбора.</p>"""

STEPS = """<ol class="steps">
  <li class="rv"><span class="n">1</span><div><h3>Бесплатный разбор</h3><p>Смотрим гражданство, доход, семью и цели. Честно говорим, какие варианты реальны, а какие нет.</p></div></li>
  <li class="rv"><span class="n">2</span><div><h3>Договор и план</h3><p>Фиксируем этапы, список документов и сроки. Вы видите весь путь заранее.</p></div></li>
  <li class="rv"><span class="n">3</span><div><h3>Подготовка документов</h3><p>Справки, переводы, легализация, подтверждение дохода и страховка по требованиям страны.</p></div></li>
  <li class="rv"><span class="n">4</span><div><h3>Подача и сопровождение</h3><p>Записываемся, подаём, отслеживаем статус и отвечаем на запросы ведомства.</p></div></li>
  <li class="rv"><span class="n">5</span><div><h3>ВНЖ и дальше</h3><p>Ведём по календарю: продления, накопление срока, экзамены и подача на гражданство.</p></div></li>
</ol>"""

INDEX = f"""<script defer src="assets/hero-motion.js?v=docs-1"></script>
<section class="hero hero-portrait">
  <div class="wrap hero-layout">
    <div class="hero-copy">
    <span class="badge"><i></i>ВНЖ и гражданство в странах Европы</span>
    <h1>От первого ВНЖ до паспорта Европы, <em>даже в сложных случаях</em></h1>
    <p class="lead">Подбираем страну и основание для ВНЖ, помогаем накопить нужный срок проживания, собираем досье, готовим к экзаменам и подаём на гражданство. Работаем дистанционно с клиентами по всему миру.</p>
    <div class="actions"><a class="btn" href="contacts.html#form">Подобрать ВНЖ бесплатно</a><a class="btn ghost" href="services.html">Все услуги</a></div>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <div class="hero-halo"></div>
      <div class="hero-enter">
        <div class="hero-person">
          <img src="assets/hero-advisor-1024.webp" srcset="assets/hero-advisor-640.webp 640w, assets/hero-advisor-1024.webp 1024w" sizes="(max-width: 759px) 92vw, (max-width: 1100px) 44vw, 520px" width="1024" height="1536" alt="" fetchpriority="high" decoding="async">
        </div>
      </div>
      <div class="hero-docs">
        <div class="doc-slot"><div class="doc doc-card">
          <span class="stars"></span>
          <span class="chip"></span>
          <b>Residencia</b>
          <small>Permiso de residencia y trabajo</small>
          <span class="photo"></span>
          <em>Válido hasta <strong>2031</strong></em>
        </div></div>
        <div class="doc-slot"><div class="doc doc-passport">
          <span class="stars"></span>
          <b>Unión Europea</b>
          <small>Pasaporte</small>
        </div></div>
        <div class="doc-slot"><div class="doc doc-contract">
          <b>Contrato</b>
          <small>de prestación de servicios</small>
          <p>Primera. Objeto. El bufete asume la preparación del expediente de residencia y su presentación ante la administración competente.</p>
          <p>Segunda. Honorarios. El pago se realiza por etapas: inicio, presentación y resolución favorable.</p>
          <svg class="sign" viewBox="0 0 120 40" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 30c10-18 18-22 20-12s-6 18-2 16 12-26 18-20-2 22 6 14 14-20 22-10 4 18 12 8 10-14 18-6 8 10 16 4"/></svg>
          <span class="stamp">N</span>
        </div></div>
      </div>
    </div>
  </div>
</section>
<div class="wrap"><div class="trust-bar rv"><span>Договор до оплаты</span><span>Оплата по этапам</span><span>Один специалист на всё дело, без колл-центра</span><span>По-русски и по-испански</span></div></div>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Пять этапов <em>до гражданства</em></h2><p>Можно прийти на любом этапе: только начинаете или уже живёте в Европе и готовитесь к подаче на паспорт.</p></div>
    {PATH}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Работаем по всем <em>странам Европы</em></h2><p>Не привязаны к одной стране. Если в одной требования не подходят, сравним условия соседних и предложим путь надёжнее.</p></div>
    {COUNTRY_GRID}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Кажется, что вы <em>не подходите?</em></h2><p>Мы разбираем ситуацию и ищем законное основание и страну, требованиям которых она отвечает. Решение всегда за ведомством, поэтому одобрение не обещаем, но за свою работу отвечаем.</p>
    <div class="note-box"><b>Сложный случай?</b> Отказ в прошлом, доход сложно подтвердить, нет истории поездок. Это повод для бесплатного разбора, а не для отказа.</div></div>
    <div class="cases">
      <div class="case rv"><h3>«Не понимаю, какая страна мне подходит»</h3><p>Сравниваем требования к доходу, срокам до гражданства, языку и налогам. Показываем два или три реальных варианта, а не один «универсальный».</p></div>
      <div class="case rv"><h3>«Доход есть, но подтвердить его сложно»</h3><p>Работаем с самозанятыми и доходом из нескольких источников. Собираем договоры, выписки и декларации так, чтобы их приняли.</p></div>
      <div class="case rv"><h3>«Боюсь потерять стаж проживания»</h3><p>Длинные отъезды и пропущенное продление обнуляют срок. Ведём календарь статуса и предупреждаем заранее.</p></div>
      <div class="case rv"><h3>«Не сдам экзамен на гражданство»</h3><p>Объясняем, какой уровень языка нужен в вашей стране, где сдавать и как подготовиться без лишних затрат.</p></div>
      <div class="case rv"><h3>«Были долги или судимость»</h3><p>Смотрим, что попадёт в справку и как это читается по правилам страны. Подбираем основание и страну с меньшим риском.</p></div>
      <div class="case rv"><h3>«Страшно платить дистанционно»</h3><p>Договор вы видите до оплаты. Всю сумму сразу не вносите: оплата идёт по этапам, последняя часть после результата.</p></div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Пакет «под ключ», <em>оплата в три этапа</em></h2></div>
    {PAY}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Как проходит <em>работа</em></h2></div>
    {STEPS}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Частые <em>вопросы</em></h2></div>
    <div class="faq rv">
      <details><summary>Сколько стоит сопровождение?</summary><p>Зависит от страны и этапа. Точную сумму называем после бесплатного разбора, оплата идёт по этапам.</p></details>
      <details><summary>Сколько лет до гражданства?</summary><p>В большинстве стран Европы от 5 до 10 лет легального проживания. Срок, требования к языку и интеграции у каждой страны свои, на разборе посчитаем именно ваш.</p></details>
      <details><summary>Нужно ли знать язык страны?</summary><p>Для ВНЖ обычно нет. Для гражданства почти везде нужен экзамен по языку, а иногда и по знанию страны. Подскажем уровень и поможем подготовиться.</p></details>
      <details><summary>Можно ли работать полностью дистанционно?</summary><p>Да. Разбор, договор, подготовка документов и связь идут онлайн. Личное присутствие нужно только там, где его требует ведомство.</p></details>
      <details><summary>На каком языке вы общаетесь?</summary><p>С вами по-русски или по-испански, с ведомствами на языке страны подачи.</p></details>
    </div>
  </div>
</section>
"""

SERVICES = f"""<div class="wrap crumbs"><a href="index.html">Главная</a> · Услуги ВНЖ</div>
<section class="hero" style="padding-top:28px">
  <div class="wrap">
    <span class="eyebrow">Услуги ВНЖ</span>
    <h1>ВНЖ и гражданство <em>во всех странах Европы</em></h1>
    <p class="lead">Ведём весь путь: от подбора ВНЖ и накопления срока проживания до подготовки досье, экзаменов и подачи заявления на гражданство. Можно подключиться на любом этапе.</p>
    <div class="actions"><a class="btn" href="contacts.html#form">Подобрать ВНЖ бесплатно</a></div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Что мы <em>делаем</em></h2></div>
    <div class="cards">
      <div class="card rv"><span class="eyebrow">Этап 1</span><h3>Подбор ВНЖ</h3><p>Сравниваем страны и основания под вашу ситуацию.</p><ul><li>ВНЖ для удалённой работы</li><li>ВНЖ на пассивный доход</li><li>Учёба, семья, бизнес</li><li>Расчёт требований к доходу</li></ul></div>
      <div class="card rv"><span class="eyebrow">Этап 2</span><h3>Накопление срока</h3><p>Сохраняем непрерывность проживания до нужного срока.</p><ul><li>Получение карты резидента</li><li>Продления без потери статуса</li><li>Смена основания</li><li>Календарь сроков и отъездов</li></ul></div>
      <div class="card rv"><span class="eyebrow">Этап 3</span><h3>Досье на гражданство</h3><p>Собираем полный комплект по требованиям страны.</p><ul><li>Подтверждение проживания</li><li>Доходы и налоги</li><li>Справки и легализация</li><li>Проверка перед подачей</li></ul></div>
      <div class="card rv"><span class="eyebrow">Этап 4</span><h3>Экзамены</h3><p>Готовим к экзаменам, которые требует страна.</p><ul><li>Язык нужного уровня</li><li>Знание истории и законов страны</li><li>Запись на экзамен</li><li>План подготовки</li></ul></div>
      <div class="card rv"><span class="eyebrow">Этап 5</span><h3>Подача на гражданство</h3><p>Подаём и ведём дело до решения.</p><ul><li>Заявление и запись</li><li>Ответы на запросы ведомства</li><li>Контроль статуса</li><li>Присяга и паспорт</li></ul></div>
    </div>
  </div>
</section>

<section style="padding-top:0" id="countries">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Страны</span><h2>Выберите страну <em>или доверьте выбор нам</em></h2><p>Требования, сроки до гражданства и экзамены в каждой стране свои. На разборе сравним подходящие варианты.</p></div>
    {COUNTRY_GRID}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Что входит <em>в сопровождение</em></h2></div>
    <dl class="facts rv">
      <div><dt>Диагностика</dt><dd>Оценка ситуации и документов, выбор страны и основания.</dd></div>
      <div><dt>Документы</dt><dd>Полный пакет: заявления, переводы, легализация.</dd></div>
      <div><dt>Подача</dt><dd>Запись, подача и общение с ведомством.</dd></div>
      <div><dt>Контроль сроков</dt><dd>Продления, стаж проживания, сроки экзаменов.</dd></div>
    </dl>
  </div>
</section>
"""

ABOUT = f"""<div class="wrap crumbs"><a href="index.html">Главная</a> · О бюро</div>
<section class="hero" style="padding-top:28px">
  <div class="wrap">
    <span class="eyebrow">О бюро</span>
    <h1>Кто мы и как <em>помогаем с ВНЖ и гражданством</em></h1>
    <p class="lead">{BRAND} сопровождает русскоязычных клиентов по всему миру на пути в Европу: от выбора основания ВНЖ до подачи на гражданство. Работаем дистанционно, от первого созвона до решения ведомства.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Кто мы <em>юридически</em></h2></div>
    <dl class="kv rv">
      <div><dt>Компания</dt><dd>DANA LEGAL CONSULTING S.L., зарегистрирована в Испании в форме S.L. в 2024 году</dd></div>
      <div><dt>NIF</dt><dd>B09790213</dd></div>
      <div><dt>Адрес</dt><dd>Avenida Cánovas del Castillo, 14, 1º derecha, Marbella</dd></div>
      <div><dt>Администратор</dt><dd>Dan Anders Hjortsoe</dd></div>
      <div><dt>Деятельность</dt><dd>Юридические услуги, миграционные и административные процедуры, наследство и недвижимость</dd></div>
      <div><dt>Где мы</dt><dd>Марбелья, Испания. С клиентами работаем дистанционно по всему миру</dd></div>
      <div><dt>Языки</dt><dd>С вами по-русски и по-испански, с ведомствами на языке страны подачи</dd></div>
      <div><dt>Связь</dt><dd>Telegram и WhatsApp, см. <a href="contacts.html">контакты</a></dd></div>
    </dl>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Чем мы <em>занимаемся</em></h2><p>Иммиграционное сопровождение по действующим законным основаниям в странах Европы.</p></div>
    {PATH}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Наши <em>принципы</em></h2></div>
    <div class="facts rv">
      <div><h3>Только законные пути</h3><p>Не строим стратегий на нелегальном пребывании. Клиенты живут в Европе легально с первого дня.</p></div>
      <div><h3>Честная диагностика</h3><p>Если пока не проходите по доходу или документам, скажем это на первом созвоне, а не через месяцы.</p></div>
      <div><h3>Работа по первоисточникам</h3><p>Требования и сроки сверяем с официальными законами и разъяснениями ведомств каждой страны.</p></div>
      <div><h3>Прозрачная оплата</h3><p>Этапы, документы и сроки видны до старта. Оплата привязана к этапам, без стопроцентной предоплаты.</p></div>
      <div><h3>Не гарантируем решение за ведомство</h3><p>Решение принимает государство. Мы отвечаем за качество подготовки: верное основание, полный комплект, аккуратные переводы.</p></div>
      <div><h3>Конфиденциальность</h3><p>Паспортные, финансовые и семейные данные используем только для вашего дела.</p></div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Пакет «под ключ», <em>оплата в три этапа</em></h2></div>
    {PAY}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><h2>Как мы <em>работаем</em></h2></div>
    {STEPS}
  </div>
</section>
"""

CONTACTS = f"""<div class="wrap crumbs"><a href="index.html">Главная</a> · Контакты</div>
<section class="hero" style="padding-top:28px">
  <div class="wrap">
    <span class="eyebrow">Контакты</span>
    <h1>Напишите нам, <em>ответим в течение рабочего дня</em></h1>
    <p class="lead">Удобнее всего в мессенджере. Звоним только по вашему запросу. Общаемся по-русски и по-испански.</p>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="contacts rv">
      <div><small>Telegram</small><b><a href="{TG_URL}" target="_blank" rel="noopener noreferrer">{TG}</a></b><span>Написать специалисту</span></div>
      <div><small>WhatsApp</small><b><a href="{WA_URL}" target="_blank" rel="noopener noreferrer">{WA}</a></b><span>Обсудить вашу ситуацию</span></div>
      <div><small>Формат работы</small><b>Дистанционно</b><span>По-русски и по-испански</span></div>
    </div>
  </div>
</section>
"""


def page(name, title, desc, body, form_prefix):
    contact = dict(brand=BRAND, tg=TG, tg_url=TG_URL, wa=WA, wa_url=WA_URL)
    canonical = DOMAIN + ("/" if name == "index.html" else "/" + name)
    html = HEAD.format(title=title, desc=desc, canonical=canonical, **contact) + body + FORM.format(p=form_prefix, **contact) + FOOT.format(**contact)
    (ROOT / name).write_text(html, encoding="utf-8")


page("index.html", "ВНЖ и гражданство в Европе", "Подбор ВНЖ, накопление срока, досье, экзамены и подача на гражданство во всех странах Европы.", INDEX, "i")
page("services.html", "Услуги ВНЖ в Европе", "Полный путь от ВНЖ до гражданства в странах Европы.", SERVICES, "s")
page("about.html", "О бюро", "Кто мы, принципы и порядок работы.", ABOUT, "a")
page("contacts.html", "Контакты бюро", "Свяжитесь с Nexora через Telegram или WhatsApp для бесплатного разбора вашей ситуации.", CONTACTS, "c")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
urls = [DOMAIN + suffix for suffix in ["/", "/services.html", "/about.html", "/contacts.html"]]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{url}</loc></url>\n" for url in urls) + "</urlset>\n", encoding="utf-8")
print("ok")
