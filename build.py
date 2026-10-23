# Генератор страниц: общий header/footer, чтобы не дублировать код вручную.
BASE = "https://ВАШ-ПОДДОМЕН.ru"   # <-- замените на свой адрес
NAV = [("index","Главная"),("schedule","Расписание"),("tickets","Билеты"),("fleet","Флот"),("about","О нас"),("contacts","Контакты")]

def page(slug, title, desc, body, kind="WebPage"):
    nav = "".join(f'<li><a href="{s}.html"{" aria-current=\"page\"" if s==slug else ""}>{n}</a></li>' for s,n in NAV)
    url = f"{BASE}/{slug}.html"
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230E3B43'/%3E%3Cpath d='M5 21c4-4 7 4 11 0s7 4 11 0' stroke='%23F2B705' stroke-width='3' fill='none'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;700&amp;family=Unbounded:wght@500;700&amp;display=swap">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"{kind}","name":"{title}","url":"{url}","description":"{desc}","inLanguage":"ru"}}
</script>
</head>
<body>
<a class="skip" href="#main">К содержимому</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="logo" href="index.html" aria-label="Речной круг — на главную">Речной круг</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Меню</button>
    <nav id="nav" aria-label="Основное меню"><ul>{nav}</ul></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot">
    <div><strong>Речной круг</strong><p>Городское пассажирское пароходство.<br>Навигация: с 1 мая по 15 октября.</p></div>
    <address>г. Заволжск, наб. Строителей, 1<br><a href="tel:+78005550142">8 (800) 555-01-42</a><br><a href="mailto:info@rechnoy-krug.example">info@rechnoy-krug.example</a></address>
    <ul class="foot-links">{nav}</ul>
  </div>
  <p class="copy wrap">© 2026 Пароходство «Речной круг». Учебный проект, организация вымышленная.</p>
</footer>
<script src="js/script.js" defer></script>
</body>
</html>
'''

# ---------- данные ----------
LINES = [
 ("1","Центральная","Речной вокзал — Парк Победы — Остров Лесной — Старая пристань","40 мин","06:30 08:00 09:30 11:00 13:30 15:00 17:30 19:00"),
 ("2","Закатная","Речной вокзал — Мост Единства — Дачный берег","55 мин","10:00 12:00 14:00 16:00 18:00 20:00"),
 ("3","Экскурсионная","Круговой рейс с остановкой на острове Лесной","2 ч","11:00 14:00 17:00"),
]
FARE = [("Взрослый","120 ₽","350 ₽"),("Школьник, студент","60 ₽","200 ₽"),("Пенсионер","60 ₽","200 ₽"),("Ребёнок до 7 лет","бесплатно","бесплатно")]
SHIPS = [("«Заволжец»","Прогулочный теплоход","180 мест","1984, обновлён в 2022","Открытая верхняя палуба, буфет, пандус для колясок."),
         ("«Ласточка»","Скоростной катер","60 мест","2019","Линия 2, время в пути сокращено на 15 минут."),
         ("«Капитан Фомин»","Экскурсионный теплоход","120 мест","2008","Панорамные окна, аудиогид на русском и английском.")]

# ---------- страницы ----------
hero = '''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <h1>По реке быстрее, чем по набережной в час пик</h1>
      <p class="lead">Три маршрута, одиннадцать пристаней и один билет на всю поездку. Рейсы каждый день с 06:30 до 21:00.</p>
      <p class="actions"><a class="btn" href="schedule.html">Смотреть расписание</a><a class="btn ghost" href="tickets.html">Цены на билеты</a></p>
    </div>
    <figure class="route" aria-label="Схема маршрута: Речной вокзал, Парк Победы, Остров Лесной, Старая пристань">
      <svg viewBox="0 0 360 260" role="img" aria-labelledby="rt">
        <title id="rt">Схема линии 1</title>
        <path class="river" d="M-10 60 C80 20 120 120 200 110 S320 190 370 150" />
        <path class="line" d="M20 70 C90 40 130 120 200 112 S300 170 340 148" pathLength="1"/>
        <g class="stops"><circle cx="20" cy="70" r="7"/><circle cx="108" cy="82" r="7"/><circle cx="200" cy="112" r="7"/><circle cx="340" cy="148" r="7"/></g>
        <g class="names"><text x="20" y="100">Речной вокзал</text><text x="92" y="58">Парк Победы</text><text x="170" y="145">Остров Лесной</text><text x="238" y="190">Старая пристань</text></g>
      </svg>
    </figure>
  </div>
</section>'''
facts = '''<section class="wrap block">
  <h2>Почему выбирают реку</h2>
  <div class="cards">
    <article><h3>Без пробок</h3><p>Время в пути не зависит от дорожной ситуации: рейс идёт строго по графику.</p></article>
    <article><h3>Один билет</h3><p>Оплатите поездку один раз и пересаживайтесь между линиями в течение 60 минут.</p></article>
    <article><h3>Доступная среда</h3><p>Пандусы на пристанях и в двух теплоходах, помощь экипажа при посадке.</p></article>
    <article><h3>С велосипедом и коляской</h3><p>Перевозим велосипеды и детские коляски бесплатно, если есть место на палубе.</p></article>
  </div>
</section>
<section class="wrap block split">
  <div><h2>Ближайшие рейсы</h2><p>Полное расписание на каждый день — на странице «Расписание».</p><a class="btn" href="schedule.html">Все рейсы</a></div>
  <ol class="next">''' + "".join(f'<li><b>{l[4].split()[0]}</b> Линия {l[0]} «{l[1]}»<span>{l[3]}</span></li>' for l in LINES) + '''</ol>
</section>'''
index = page("index","Речной круг — городское пассажирское пароходство в Заволжске","Расписание, цены на билеты и маршруты речных трамваев в Заволжске. Три линии, одиннадцать пристаней, рейсы ежедневно.", hero+facts, "Organization")

rows = "".join(f'<tr data-line="{l[0]}"><th scope="row">Линия {l[0]} «{l[1]}»</th><td>{l[2]}</td><td>{l[3]}</td><td>{l[4].replace(" ",", ")}</td></tr>' for l in LINES)
schedule = page("schedule","Расписание речных трамваев — Речной круг","Расписание рейсов по трём линиям пароходства «Речной круг»: время отправления, маршрут и длительность.", f'''<section class="wrap block">
  <h1>Расписание</h1>
  <p class="lead">Время отправления от Речного вокзала. Расписание действует ежедневно в период навигации.</p>
  <fieldset class="filter"><legend>Показать линию</legend>
    <label><input type="radio" name="line" value="all" checked> Все</label>
    <label><input type="radio" name="line" value="1"> Линия 1</label>
    <label><input type="radio" name="line" value="2"> Линия 2</label>
    <label><input type="radio" name="line" value="3"> Линия 3</label>
  </fieldset>
  <div class="table-wrap"><table id="timetable"><caption>Рейсы по линиям</caption>
    <thead><tr><th scope="col">Линия</th><th scope="col">Маршрут</th><th scope="col">В пути</th><th scope="col">Отправление</th></tr></thead>
    <tbody>{rows}</tbody></table></div>
  <p class="note">В непогоду и при ограничении судоходства рейсы могут быть отменены. Следите за объявлениями на пристанях.</p>
</section>''')

frows = "".join(f"<tr><th scope='row'>{a}</th><td>{b}</td><td>{c}</td></tr>" for a,b,c in FARE)
tickets = page("tickets","Цены на билеты — Речной круг","Тарифы на проезд и экскурсии, калькулятор стоимости поездки и форма заявки на групповой билет.", f'''<section class="wrap block">
  <h1>Билеты и тарифы</h1>
  <div class="table-wrap"><table><caption>Стоимость проезда</caption>
    <thead><tr><th scope="col">Категория</th><th scope="col">Линии 1 и 2</th><th scope="col">Линия 3 (экскурсия)</th></tr></thead>
    <tbody>{frows}</tbody></table></div>
</section>
<section class="wrap block split">
  <form class="card-form" id="calc" action="#" method="get" novalidate>
    <h2>Сколько стоит поездка</h2>
    <label for="cat">Категория</label>
    <select id="cat" name="cat"><option value="120|350">Взрослый</option><option value="60|200">Школьник, студент, пенсионер</option></select>
    <label for="route">Линия</label>
    <select id="route" name="route"><option value="0">Линия 1 или 2</option><option value="1">Линия 3 (экскурсия)</option></select>
    <label for="qty">Количество билетов</label>
    <input id="qty" name="qty" type="number" min="1" max="50" value="1">
    <p class="result" aria-live="polite">Итого: <output id="total" for="cat route qty">120 ₽</output></p>
  </form>
  <div><h2>Где купить</h2><ul class="plain"><li>В кассах на пристанях — наличными и картой</li><li>У экипажа на борту — только наличными</li><li>По телефону для групп от 10 человек</li></ul></div>
</section>''')

fleet = page("fleet","Флот пароходства — Речной круг","Теплоходы и катера пароходства «Речной круг»: вместимость, год постройки и особенности судов.", '<section class="wrap block"><h1>Наш флот</h1><div class="cards three">' + "".join(
 f'<article class="ship"><h2>{n}</h2><p class="kind">{k}</p><dl><dt>Вместимость</dt><dd>{c}</dd><dt>Год</dt><dd>{y}</dd></dl><p>{d}</p></article>' for n,k,c,y,d in SHIPS) + '</div></section>')

about = page("about","О пароходстве — Речной круг","История пароходства «Речной круг», миссия, безопасность на воде и вакансии для капитанов и матросов.", '''<section class="wrap block narrow">
  <h1>О пароходстве</h1>
  <p>«Речной круг» возит горожан по реке с 1952 года. Сегодня мы управляем тремя линиями и обслуживаем более 400 тысяч пассажиров за сезон.</p>
  <h2>Как мы работаем</h2>
  <p>Каждое судно проходит технический осмотр перед выходом на линию. На борту есть спасательные жилеты для всех пассажиров, включая детские размеры.</p>
  <h2>История</h2>
  <ol class="timeline">
    <li><b>1952</b> Первый рейс от Речного вокзала до Старой пристани.</li>
    <li><b>1984</b> В эксплуатацию вошёл теплоход «Заволжец».</li>
    <li><b>2019</b> Открыта скоростная линия 2 на катере «Ласточка».</li>
    <li><b>2022</b> Обновлены пристани, добавлены пандусы.</li>
  </ol>
  <h2>Работа у нас</h2>
  <p>Приглашаем капитанов, механиков и матросов. Резюме отправляйте на info@rechnoy-krug.example.</p>
</section>''')

contacts = page("contacts","Контакты — Речной круг","Адрес, телефон, режим работы касс и форма обратной связи пароходства «Речной круг».", '''<section class="wrap block split">
  <div>
    <h1>Контакты</h1>
    <address><p>г. Заволжск, наб. Строителей, 1</p><p><a href="tel:+78005550142">8 (800) 555-01-42</a></p><p><a href="mailto:info@rechnoy-krug.example">info@rechnoy-krug.example</a></p></address>
    <h2>Режим работы касс</h2>
    <p>Ежедневно с 06:00 до 21:00, в период навигации.</p>
  </div>
  <form class="card-form" action="#" method="post">
    <h2>Написать нам</h2>
    <label for="name">Имя</label>
    <input id="name" name="name" type="text" required minlength="2" autocomplete="name">
    <label for="email">Электронная почта</label>
    <input id="email" name="email" type="email" required autocomplete="email">
    <label for="topic">Тема</label>
    <select id="topic" name="topic"><option>Вопрос по рейсу</option><option>Групповая заявка</option><option>Жалоба или предложение</option></select>
    <label for="msg">Сообщение</label>
    <textarea id="msg" name="msg" rows="5" required></textarea>
    <label class="check"><input type="checkbox" required> Согласен на обработку персональных данных</label>
    <button class="btn" type="submit">Отправить сообщение</button>
  </form>
</section>''', "ContactPage")

for s,c in [("index",index),("schedule",schedule),("tickets",tickets),("fleet",fleet),("about",about),("contacts",contacts)]:
    open(f"{s}.html","w",encoding="utf-8").write(c)

open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE}/{s}.html</loc></url>\n" for s,_ in NAV) + '</urlset>\n')
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
