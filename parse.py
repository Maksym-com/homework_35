# Быбліотеки які потрібно встановити
import requests
from bs4 import BeautifulSoup


# Сайт з якого парсим інофрмацію
site_link = "https://xmovies8.stream"
r = requests.get(url=site_link, verify=True)
soup = BeautifulSoup(r.content, "html.parser")

# Сайти для парсингу фільмів за жанрами:

# Драма
drama = 'https://xmovies8.stream/genre/drama/'
dr = requests.get(url=drama, verify=True)
soup0 = BeautifulSoup(dr.content, "html.parser")

# Триллер
thriller = 'https://xmovies8.stream/genre/thriller/'
th = requests.get(url=thriller, verify=True)
soup1 = BeautifulSoup(th.content, "html.parser")

# Романтичний
romance = 'https://xmovies8.stream/genre/romance/'
rm = requests.get(url=romance, verify=True)
soup2 = BeautifulSoup(rm.content, "html.parser")

# Кримінал
crime = 'https://xmovies8.stream/genre/crime/'
cr = requests.get(url=crime, verify=True)
soup3 = BeautifulSoup(cr.content, "html.parser")

# Пригоди
adventure = 'https://xmovies8.stream/genre/adventure/'
ad = requests.get(url=adventure, verify=True)
soup4 = BeautifulSoup(ad.content, "html.parser")

# Фентезі
fantasy = 'https://xmovies8.stream/genre/fantasy/'
fn = requests.get(url=fantasy, verify=True)
soup5 = BeautifulSoup(fn.content, "html.parser")

# Науковий / Майбутнє
science_fiction = 'https://xmovies8.stream/genre/science-fiction/'
sf = requests.get(url=science_fiction, verify=True)
soup6 = BeautifulSoup(sf.content, "html.parser")

# Анімаційний
animation = 'https://xmovies8.stream/genre/animation/'
an = requests.get(url=animation, verify=True)
soup7 = BeautifulSoup(an.content, "html.parser")

# Вестерн
western = 'https://xmovies8.stream/genre/western/'
wt = requests.get(url=western, verify=True)
soup8 = BeautifulSoup(wt.content, "html.parser")

# Війна і Політика
war_politics = 'https://xmovies8.stream/genre/war-politics/'
wp = requests.get(url=war_politics, verify=True)
soup9 = BeautifulSoup(wp.content, "html.parser")

# Комедія
comedy = 'https://xmovies8.stream/genre/comedy/'
cm = requests.get(url=comedy, verify=True)
soup10 = BeautifulSoup(cm.content, "html.parser")

# Екшн
action = 'https://xmovies8.stream/genre/action/'
act = requests.get(url=action, verify=True)
soup11 = BeautifulSoup(act.content, "html.parser")

# Жахи
horror = 'https://xmovies8.stream/genre/horror/'
hr = requests.get(url=horror, verify=True)
soup12 = BeautifulSoup(hr.content, "html.parser")

# Документальний
documentary = 'https://xmovies8.stream/genre/documentary/'
doc = requests.get(url=documentary, verify=True)
soup13 = BeautifulSoup(doc.content, "html.parser")

# Загадка / Детектив
mystery = 'https://xmovies8.stream/genre/mystery/'
mt = requests.get(url=mystery, verify=True)
soup14 = BeautifulSoup(mt.content, "html.parser")

# Сіменйний
family = 'https://xmovies8.stream/genre/family/'
fm = requests.get(url=family, verify=True)
soup15 = BeautifulSoup(fm.content, "html.parser")

# Історичний
history = 'https://xmovies8.stream/genre/history/'
hst = requests.get(url=history, verify=True)
soup16 = BeautifulSoup(hst.content, "html.parser")

# Дитячий
kids = 'https://xmovies8.stream/genre/kids/'
kd = requests.get(url=kids, verify=True)
soup17 = BeautifulSoup(kd.content, "html.parser")

# Музичний
musical = 'https://xmovies8.stream/genre/musical/'
ms = requests.get(url=musical, verify=True)
soup18 = BeautifulSoup(ms.content, "html.parser")

# Словник з списками фільмів за жанрами
db_of_films = {
        "Drama": [], # [{header, link, body_text}, {header, link, body_text}, {header, link, body_text}, ...]
        "Thriller": [],
        "Romance": [],
        "Crime": [],
        "Adventure": [],
        "Fantasy": [],
        "Science Fiction": [],
        "Animation": [],
        "Western": [],
        "War & Politics": [],
        "Comedy": [],
        "Action": [],
        "Horror": [],
        "Documentary": [],
        "Mystery": [],
        "Family": [],
        "History": [],
        "Kids": [],
        "Musical": []
    }

# Забирає зайві пробіли
def parse_body_text(soup_news: BeautifulSoup, selector: str):
    body_text_list = []
    for p in soup_news.select(selector):
        body_text_list.append(f"{p.text.strip()}\n")
    return " ".join(body_text_list)

# Список всіх фільмів
films_list = []

# Парсим всі фільми
for films in soup.select("h3 > a"):
    films_title0 = films.text
    # Забираєм зайві переноси
    films_title1 = ''.join([char for char in films_title0 if char != '\n'])
    films_href0 = films.get('href', '')
    films_href1 = ''.join([char for char in films_href0 if char != '\n'])
    # Додаєм до списку з всіма фільмами
    films_list.append(f'{films_title1} - {films_href1}.')

# Парсим фільми за жанрами

# Драма
for dra in soup0.select("h3 > a"):
    dramas_title0 = dra.text
    dramas_title1 = ''.join([char for char in dramas_title0 if char != '\n'])
    dramas_href0 = dra.get('href', '')
    dramas_href1 = ''.join([char for char in dramas_href0 if char != '\n'])
    # Додаєм до словника з жанрами в список
    db_of_films["Drama"].append(f'{dramas_title1} - {dramas_href1}.')

# Триллер
for thr in soup1.select("h3 > a"):
    thrillers_title0 = thr.text
    thrillers_title1 = ''.join([char for char in thrillers_title0 if char != '\n'])
    thrillers_href0 = thr.get('href', '')
    thrillers_href1 = ''.join([char for char in thrillers_href0 if char != '\n'])
    db_of_films['Thriller'].append(f'{thrillers_title1} - {thrillers_href1}.')

# Романтичний
for rom in soup2.select("h3 > a"):
    romance_title0 = rom.text
    romance_title1 = ''.join([char for char in romance_title0 if char != '\n'])
    romance_href0 = rom.get('href', '')
    romance_href1 = ''.join([char for char in romance_href0 if char != '\n'])
    db_of_films['Romance'].append(f'{romance_title1} - {romance_href1}.')

# Кримінал
for cri in soup3.select("h3 > a"):
    crime_title0 = cri.text
    crime_title1 = ''.join([char for char in crime_title0 if char != '\n'])
    crime_href0 = cri.get('href', '')
    crime_href1 = ''.join([char for char in crime_href0 if char != '\n'])
    db_of_films['Crime'].append(f'{crime_title1} - {crime_href1}.')

# Пригоди
for adv in soup4.select("h3 > a"):
    advent_title0 = adv.text
    advent_title1 = ''.join([char for char in advent_title0 if char != '\n'])
    advent_href0 = adv.get('href', '')
    advent_href1 = ''.join([char for char in advent_href0 if char != '\n'])
    db_of_films['Adventure'].append(f'{advent_title1} - {advent_href1}.')

# Фентезі
for fan in soup5.select("h3 > a"):
    fantasy_title0 = fan.text
    fantasy_title1 = ''.join([char for char in fantasy_title0 if char != '\n'])
    fantasy_href0 = fan.get('href', '')
    fantasy_href1 = ''.join([char for char in fantasy_href0 if char != '\n'])
    db_of_films['Fantasy'].append(f'{fantasy_title1} - {fantasy_href1}.')

# Науковий / Майбутнє
for scfi in soup6.select("h3 > a"):
    sciencef_title0 = scfi.text
    sciencef_title1 = ''.join([char for char in sciencef_title0 if char != '\n'])
    sciencef_href0 = scfi.get('href', '')
    sciencef_href1 = ''.join([char for char in sciencef_href0 if char != '\n'])
    db_of_films['Science Fiction'].append(f'{sciencef_title1} - {sciencef_href1}.')

# Анімаційний
for ani in soup7.select("h3 > a"):
    animation_title0 = ani.text
    animation_title1 = ''.join([char for char in animation_title0 if char != '\n'])
    animation_href0 = ani.get('href', '')
    animation_href1 = ''.join([char for char in animation_href0 if char != '\n'])
    db_of_films['Animation'].append(f'{animation_title1} - {animation_href1}.')

# Вестерн
for wts in soup8.select("h3 > a"):
    west_title0 = wts.text
    west_title1 = ''.join([char for char in west_title0 if char != '\n'])
    west_href0 = wts.get('href', '')
    west_href1 = ''.join([char for char in west_href0 if char != '\n'])
    db_of_films['Western'].append(f'{west_title1} - {west_href1}.')

# Війна і Політіка 
for wrp in soup9.select("h3 > a"):
    warpol_title0 = wrp.text
    warpol_title1 = ''.join([char for char in warpol_title0 if char != '\n'])
    warpol_href0 = wrp.get('href', '')
    warpol_href1 = ''.join([char for char in warpol_href0 if char != '\n'])
    db_of_films['War & Politics'].append(f'{warpol_title1} - {warpol_href1}.')

# Комедія
for cm in soup10.select("h3 > a"):
    comedy_title0 = cm.text
    comedy_title1 = ''.join([char for char in comedy_title0 if char != '\n'])
    comedy_href0 = cm.get('href', '')
    comedy_href1 = ''.join([char for char in comedy_href0 if char != '\n'])
    db_of_films['Comedy'].append(f'{comedy_title1} - {comedy_href1}.')

# Екшн
for atc in soup11.select("h3 > a"):
    action_title0 = atc.text
    action_title1 = ''.join([char for char in action_title0 if char != '\n'])
    action_href0 = atc.get('href', '')
    action_href1 = ''.join([char for char in action_href0 if char != '\n'])
    db_of_films['Action'].append(f'{action_title1} - {action_href1}.')

# Жахи
for hor in soup12.select("h3 > a"):
    horror_title0 = hor.text
    horror_title1 = ''.join([char for char in horror_title0 if char != '\n'])
    horror_href0 = hor.get('href', '')
    horror_href1 = ''.join([char for char in horror_href0 if char != '\n'])
    db_of_films['Horror'].append(f'{horror_title1} - {horror_href1}.')

# Документальний
for dot in soup13.select("h3 > a"):
    document_title0 = dot.text
    document_title1 = ''.join([char for char in document_title0 if char != '\n'])
    document_href0 = dot.get('href', '')
    document_href1 = ''.join([char for char in document_href0 if char != '\n'])
    db_of_films['Documentary'].append(f'{document_title1} - {document_href1}.')

# Загадка / Детектив
for mys in soup14.select("h3 > a"):
    mystery_title0 = mys.text
    mystery_title1 = ''.join([char for char in mystery_title0 if char != '\n'])
    mystery_href0 = mys.get('href', '')
    mystery_href1 = ''.join([char for char in mystery_href0 if char != '\n'])
    db_of_films['Mystery'].append(f'{mystery_title1} - {mystery_href1}.')

# Сімейний
for fam in soup15.select("h3 > a"):
    family_title0 = fam.text
    family_title1 = ''.join([char for char in family_title0 if char != '\n'])
    family_href0 = fam.get('href', '')
    family_href1 = ''.join([char for char in family_href0 if char != '\n'])
    db_of_films['Family'].append(f'{family_title1} - {family_href1}.')

# Історичний
for his in soup16.select("h3 > a"):
    history_title0 = his.text
    history_title1 = ''.join([char for char in history_title0 if char != '\n'])
    history_href0 = his.get('href', '')
    history_href1 = ''.join([char for char in history_href0 if char != '\n'])
    db_of_films['History'].append(f'{history_title1} - {history_href1}.')

# Дитячий
for kid in soup17.select("h3 > a"):
    kids_title0 = kid.text
    kids_title1 = ''.join([char for char in kids_title0 if char != '\n'])
    kids_href0 = kid.get('href', '')
    kids_href1 = ''.join([char for char in kids_href0 if char != '\n'])
    db_of_films['Kids'].append(f'{kids_title1} - {kids_href1}.')

# Музичний
for mus in soup18.select("h3 > a"):
    music_title0 = mus.text
    music_title1 = ''.join([char for char in music_title0 if char != '\n'])
    music_href0 = mus.get('href', '')
    music_href1 = ''.join([char for char in music_href0 if char != '\n'])
    db_of_films['Musical'].append(f'{music_title1} - {music_href1}.')


