#!/usr/bin/env python3
"""Собирает 4 страницы черновика из общих шапки, меню и подвала. Запуск: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
BRAND = "Nexora"
TG = "@buro_placeholder"
WA = "+XX XXX XXX XXX"
MAIL = "info@example.com"

HEAD = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@1,600&display=swap">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="draft">Черновик · контакты пока заглушки</div>
<header class="top">
  <div class="wrap">
    <a class="logo" href="index.html"><i></i>{brand}</a>
    <div class="lang" aria-label="Языки общения"><span class="on">RU</span><span>ES</span></div>
    <a class="ico" href="https://t.me/" aria-label="Telegram">✈</a>
    <a class="ico" href="contacts.html" aria-label="WhatsApp">☏</a>
    <a class="btn sm" href="contacts.html#form">Подобрать ВНЖ</a>
    <button class="burger" type="button" aria-label="Меню" aria-expanded="false"><span></span></button>
  </div>
</header>
<div class="menu" hidden>
  <nav class="menu-panel" aria-label="Меню">
    <div class="menu-head"><span class="logo"><i></i>{brand}</span><button class="menu-close" type="button" aria-label="Закрыть">×</button></div>
    <a class="item" href="services.html"><span>Услуги ВНЖ<small>По всем странам Европы</small></span>→</a>
    <a class="item" href="about.html"><span>О бюро<small>Кто мы и как работаем</small></span>→</a>
    <a class="item" href="contacts.html"><span>Контакты<small>Telegram, WhatsApp, почта</small></span>→</a>
    <div class="menu-foot">
      <a class="btn" href="contacts.html#form">Бесплатный разбор</a>
      <span>Telegram {tg}</span>
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
    <div style="display:grid;gap:8px"><span>Telegram {tg}</span><span>WhatsApp {wa}</span><span>{mail}</span></div>
  </div>
</footer>
<script src="assets/main.js"></script>
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
        <form class="lead" novalidate>
          <label for="{p}-name">Как к вам обращаться<input id="{p}-name" name="name" type="text" placeholder="Имя"></label>
          <label for="{p}-way">Где удобнее общаться<select id="{p}-way" name="way"><option>Telegram</option><option>WhatsApp</option><option>Телефон</option><option>Email</option></select></label>
          <label for="{p}-contact">Ваш контакт<input id="{p}-contact" name="contact" type="text" placeholder="@ник, номер или почта"></label>
          <label class="check" for="{p}-consent"><input id="{p}-consent" name="consent" type="checkbox">Согласен на обработку персональных данных. Контакт нужен только для ответа на заявку.</label>
          <p class="form-error" hidden></p>
          <button class="btn" type="submit">Получить разбор</button>
        </form>
        <div class="ok" hidden><b>Спасибо! Мы скоро напишем.</b><small>Это прототип: данные никуда не отправляются.</small></div>
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

COUNTRIES = [("🇪🇸","Испания"),("🇵🇹","Португалия"),("🇮🇹","Италия"),("🇫🇷","Франция"),("🇩🇪","Германия"),("🇳🇱","Нидерланды"),("🇦🇹","Австрия"),("🇬🇷","Греция"),("🇨🇾","Кипр"),("🇲🇹","Мальта"),("🇭🇷","Хорватия"),("🇸🇰","Словакия"),("🇨🇿","Чехия"),("🇵🇱","Польша"),("🇭🇺","Венгрия"),("🇲🇪","Черногория"),("🇷🇸","Сербия")]
COUNTRY_GRID = '<div class="countries rv">' + "".join(f'<a class="country" href="services.html#countries"><span class="fl">{f}</span>{n}</a>' for f, n in COUNTRIES) + '<a class="country more" href="contacts.html#form"><span class="fl">＋</span>Другие страны Европы</a></div>'

PAY = """<div class="pay">
  <div class="rv"><small>Этап 1 · старт</small><b>50%</b><p class="muted">Берём дело в работу: стратегия, расчёт требований, список документов.</p></div>
  <div class="rv"><small>Этап 2 · подача</small><b>+25%</b><p class="muted">Когда документы подготовлены и поданы.</p></div>
  <div class="rv"><small>Этап 3 · результат</small><b>+25%</b><p class="muted">Только после положительного решения.</p></div>
</div>
<p class="pay-note">Этапы и суммы фиксируем в договоре до первой оплаты. Госпошлины, переводы и легализацию документов оплачиваете отдельно, по квитанциям. Стоимость называем после бесплатного разбора. <span class="ph">Схему оплаты и условия возврата уточнить</span></p>"""

STEPS = """<ol class="steps">
  <li class="rv"><span class="n">1</span><div><h3>Бесплатный разбор</h3><p>Смотрим гражданство, доход, семью и цели. Честно говорим, какие варианты реальны, а какие нет.</p></div></li>
  <li class="rv"><span class="n">2</span><div><h3>Договор и план</h3><p>Фиксируем этапы, список документов и сроки. Вы видите весь путь заранее.</p></div></li>
  <li class="rv"><span class="n">3</span><div><h3>Подготовка документов</h3><p>Справки, переводы, легализация, подтверждение дохода и страховка по требованиям страны.</p></div></li>
  <li class="rv"><span class="n">4</span><div><h3>Подача и сопровождение</h3><p>Записываемся, подаём, отслеживаем статус и отвечаем на запросы ведомства.</p></div></li>
  <li class="rv"><span class="n">5</span><div><h3>ВНЖ и дальше</h3><p>Ведём по календарю: продления, накопление срока, экзамены и подача на гражданство.</p></div></li>
</ol>"""

INDEX = f"""<section class="hero">
  <div class="wrap">
    <span class="badge"><i></i>ВНЖ и гражданство в странах Европы</span>
    <h1>От первого ВНЖ до паспорта Европы, <em>даже в сложных случаях</em></h1>
    <p class="lead">Подбираем страну и основание для ВНЖ, помогаем накопить нужный срок проживания, собираем досье, готовим к экзаменам и подаём на гражданство. Работаем дистанционно с клиентами по всему миру.</p>
    <div class="note-box"><b>Сложный случай?</b> Отказ в прошлом, доход сложно подтвердить, нет истории поездок. Это повод для бесплатного разбора, а не для отказа.</div>
    <div class="actions"><a class="btn" href="contacts.html#form">Подобрать ВНЖ бесплатно</a><a class="btn ghost" href="services.html">Все услуги</a></div>
    <div class="trust"><span>Договор до оплаты</span><span>Оплата по этапам</span><span>Один специалист на всё дело, без колл-центра</span><span>По-русски и по-испански</span></div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Весь путь в одном бюро</span><h2>Пять этапов <em>до гражданства</em></h2><p>Можно прийти на любом этапе: только начинаете или уже живёте в Европе и готовитесь к подаче на паспорт.</p></div>
    {PATH}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">География</span><h2>Работаем по всем <em>странам Европы</em></h2><p>Не привязаны к одной стране. Если в одной требования не подходят, сравним условия соседних и предложим путь надёжнее.</p></div>
    {COUNTRY_GRID}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Наша обычная работа</span><h2>Кажется, что вы <em>не подходите?</em></h2><p>Мы разбираем ситуацию и ищем законное основание и страну, требованиям которых она отвечает. Решение всегда за ведомством, поэтому одобрение не обещаем, но за свою работу отвечаем.</p></div>
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
    <div class="head rv"><span class="eyebrow">Оплата привязана к результату</span><h2>Пакет «под ключ», <em>оплата в три этапа</em></h2></div>
    {PAY}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Прозрачно</span><h2>Как проходит <em>работа</em></h2></div>
    {STEPS}
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="head rv"><span class="eyebrow">Вопросы</span><h2>Частые <em>вопросы</em></h2></div>
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
      <div><dt>Связь</dt><dd>Telegram, WhatsApp, почта, см. <a href="contacts.html">контакты</a></dd></div>
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
      <div><small>Telegram</small><b>{TG}</b></div>
      <div><small>WhatsApp</small><b>{WA}</b></div>
      <div><small>Почта</small><b>{MAIL}</b></div>
      <div><small>Часы работы</small><b>Пн-Пт, 10:00-19:00</b><span class="ph">часовой пояс: уточнить</span></div>
    </div>
  </div>
</section>
"""


def page(name, title, desc, body, form_prefix):
    html = HEAD.format(title=title, desc=desc, brand=BRAND, tg=TG) + body + FORM.format(p=form_prefix) + FOOT.format(brand=BRAND, tg=TG, wa=WA, mail=MAIL)
    (ROOT / name).write_text(html, encoding="utf-8")


page("index.html", "ВНЖ и гражданство в Европе", "Подбор ВНЖ, накопление срока, досье, экзамены и подача на гражданство во всех странах Европы.", INDEX, "i")
page("services.html", "Услуги ВНЖ в Европе", "Полный путь от ВНЖ до гражданства в странах Европы.", SERVICES, "s")
page("about.html", "О бюро", "Кто мы, принципы и порядок работы.", ABOUT, "a")
page("contacts.html", "Контакты бюро", "Telegram, WhatsApp, почта и форма бесплатного разбора.", CONTACTS, "c")
print("ok")
