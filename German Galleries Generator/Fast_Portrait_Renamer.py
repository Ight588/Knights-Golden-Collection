from os import rename, listdir
from json import load, dump


def translit_to_jp(text: str) -> str:
    morphemes = {"ж": "j", "с": "s", "у": "u", "а": "a", "и": "i", "о": "o", "е": "e",
                 "н": "n", "к": "k", "р": "r", "т": "t", "ф": "f", "я": "ya", "ю": "yu",
                 "ш": "sh", "в": "w", "г": "g", "х": "h", "д": "d", "з": "z", "э": "e",
                 "й": "i", "ё": "yo", "в": "w", "б": "b", "м": "m", "ц":"ts", "п": "p",
                 "ч": "ch", "ы": "a", "ь": ""} 
    res = ""
    for i, elem in enumerate(text.lower()):
        if elem == "д" and text[i+1] == "ж": continue
        res += morphemes[elem]
    return res.capitalize()


names = [
#    "Аджии",
    "Аканэ",
    "Амай",
    "Аой",
#    "Асу",
    "Берумы",
    "Беши",
    "Борупена",
    "Будо",
    "Гаку",
    "Гейджу",
    "Гемы",
    "Гиты",
    "Дайроку",
    "Даку",
    "Дафуни",
    "Джуку",
    "Доры",
    "Инкью",
    "Ируки",
    "Итачи",
    "Каги",
    "Кашико",
    "Кенко",
    "Кибы",
#    "Кизаны",
    "Коконы",
    "Кокоро",
    "Кокумы",
    "Куроко",
    "Куу",
    "Кьюджи",
    "Май",
    "Маки",
    "Мантаро",
#    "Мегами",
    "Меки",
    "Мидори",
    "Мины",
    "Миюджи",
    "Мусуме",
#    "Оки",
    "Осаны",
#    "Осоро",
    "Отохико",
    "Пиппи",
    "Райбару",
    "Рику",
    "Роджасу",
    "Рюто",
    "Саки",
    "Сакуры",
    "Сакью",
    "Сейо",
    "Сенпая",
    "Сукуби",
    "Сумире",
    "Супаны",
    "Тоги",
    "Токуко",
    "Умеджи",
    "Унаги",
    "Уэкии",
    "Фуреддо",
    "Хазу",
    "Ханы",
#    "Ханако",
    "Хаянари",
    "Химари",
    "Ходжиро",
    "Хокуто",
    "Хому",
    "Хоро",
    "Хоруды",
    "Хошико",
    "Цубаки",
    "Цурузо",
    "Чоджо",
    "Шимы",
    "Шина",
    "Широми",
    "Шо",
    "Шозо",
    "Шоку",
    "Энпицу",
    "Эфуде",
    "Яку",
    "Аяно",
#    "Генки",
	"Карин",
	"Кахо_Канокоги",
	"Киоши",
#	"Кочо",
#	"Миды",
#	"Муджи",
	"Насу",
	"Нацуки",
	"Рейны",
	"Рино",
	"Шиори"
    ]

names_1980 = [
	"Кагуи",
	"Моэко",
	"Хонами",
	"Сумико",
	"Рицуко",
	"Ай",
	"Тейко",
	"Комако",
	"Чигусы",
	"Азумы",
	"Азусы",
	"Айки",
	"Акари",
	"Акифуми",
	"Банри",
	"Бунзо",
	"Ваки",
	"Ватару",
	"Гакуто",
	"Готы",
	"Дайзо",
	"Дайсаку",
	"Дайчи",
	"Джицуко",
	"Джозе",
	"Дорэми",
	"Зенджи",
	"Ивао",
	"Икуэ",
	"Ицуми",
	"Ичиэй",
	"Кагемори",
	"Кахо",
	"Кена",
	"Кохару",
	"Мааи",
	"Махиро",
	"Меи",
	"Мурасаки",
	"Нагако",
	"Нагахару",
	"Окимото",
	"Оми",
	"Джокичи",
	"Райзо",
	"Райму",
	"Ран",
	"Рейичи",
	"Риобы",
	"Рюсея",
	"Сабуро",
	"Сачи",
	"Сачихико",
	"Сейширо",
	"Соноко",
	"Соры",
	"Соты",
	"Тадааки",
	"Тайчи",
	"Такако",
	"Тиру",
	"Того",
	"Уи",
	"Уманосукэ",
	"Умеко",
	"Фуджио",
	"Фуджиэ",
	"Фуюкичи",
	"Фуюми",
	"Ханаэ",
	"Харуто",
	"Хачиро",
	"Хаято",
	"Химеко",
	"Хозуми",
	"Хоноки",
	"Чидори",
	"Чизуру",
	"Чикао",
	"Чуджиро",
	"Шинако",
	"Шичиро",
	"Эйичи",
	"Эйко",
	"Эцуджи",
	"Эцуко",
	"Юи",
	"Юны",
	"Яхико",
	"Яэ",
	"Кёко",
	"Джури",
#	"Кочо_в_1989",
	"Маэ",
	"Муцуко",
	"Нориё",
	"Отомэ",
	"Рёко",
	"Сузуко",
	"Цуру"
]

model_names = [
	"Аджиа_Ашитоми",
	"Аканэ_Ториясу",
	"Амай_Одаяка",
	"Аой_Рюгоку",
	"Берума_Динкури",
	"Беши_Такамине",
	"Борупен_Сайшики",
	"Будо_Масута",
	"Гаку_Хикицури",
	"Гейджу_Цука",
	"Гема_Таку",
	"Гита_Ямахато",
	"Дайроку_Сурикизу",
	"Даку_Ацу",
	"Дафуни_Бурейку",
	"Джуку_Рен",
	"Дора_Тамамото",
	"Инкью_Басу",
	"Ирука_Доруфино",
	"Итачи_Заметора",
	"Кага_Куша",
	"Кашико_Мурасаки",
	"Кенко_Сукояка",
	"Киба_Каваито",
	"Кокона_Харука",
	"Кокоро_Момоиро",
	"Кокума_Джуцу",
	"Куроко_Каменага",
	"Куу_Дере",
	"Кьюджи_Конагава",
	"Май_Вайфу",
	"Мака_Тансей",
	"Мантаро_Сашимасу",
	"Мека_Никару",
	"Мидори_Гурин",
	"Мина_Раи",
	"Миюджи_Шан",
	"Мусуме_Роншаку",
	"Осана_Наджими",
	"Отохико_Меичи",
	"Пиппи_Осу",
	"Райбару_Фумецу",
	"Рику_Сома",
	"Роджасу_Норубиру",
	"Рюто_Иппонго",
	"Саки_Мию",
	"Сакура_Хагивара",
	"Сакью_Басу",
	"Сейо_Аканиши",
	"Таро_Ямада",
	"Сукуби_Дубиду",
	"Сумире_Сузуки",
	"Супана_Чуру",
	"Тога_Табара",
	"Токуко_Китагава",
	"Умеджи_Кизугучи",
	"Унаги_Денкашиза",
	"Уэкия_Энгейка",
	"Фуреддо_Джонзу",
	"Хазу_Кашибучи",
	"Хана_Дайдайяма",
	"Хаянари_Цумеато",
	"Химари_Фуджита",
	"Ходжиро_Замеширо",
	"Хокуто_Фурукизу",
	"Хому_Курусу",
	"Хоро_Гураму",
	"Хоруда_Пуресу",
	"Хошико_Мизудори",
	"Цубаки_Уэсуги",
	"Цурузо_Ямазаки",
	"Чоджо_Текина",
	"Шима_Шия",
	"Шин_Хигаку",
	"Широми_Тораёши",
	"Шо_Кунин",
	"Шозо_Куросава",
	"Шоку_Цубурая",
	"Энпицу_Бьёга",
	"Эфуде_Нуримоно",
	"Яку_Заиши",
	"Аяно_Аиши",
	"Карин_Ханабуса",
	"Кахо_Канокоги",
	"Киоши_Тачикава",
	"Насу_Канкоши",
	"Нацуки_Абурая",
	"Рейна_Набатаме",
	"Рино_Фукахори",
	"Шиори_Рикитаке"
]
model_names_1980 = [
	"Кагуя_Вакайзуми",
	"Моэко_Ракуёна",
	"Хонами_Ходошима",
	"Сумико_Тачибана",
	"Рицуко_Чиканари",
	"Ай_Доруяши",
	"Тейко_Набатасай",
	"Комако_Фунакоши",
	"Чигуса_Бусуджима",
	"Азума_Такахоши",
	"Азуса_Мицуиши",
	"Айка_Исери",
	"Акари_Комияку",
	"Акифуми_Анно",
	"Банри_Масаюки",
	"Бунзо_Ота",
	"Вака_Ямага",
	"Ватару_Мурата",
	"Гакуто_Имакаке",
	"Гота_Кушида",
	"Дайзо_Момосэ",
	"Дайсаку_Арагаки",
	"Дайчи_Сузуки",
	"Джицуко_Фурусава",
	"Джозе_Шиуба",
	"Дорэми_Шимахара",
	"Зенджи_Шинокура",
	"Ивао_Сато",
	"Икуэ_Яйтабаши",
	"Ицуми_Юуки",
	"Ичиэй_Накаяма",
	"Кагемори_Такаги",
	"Кахо_Мики",
	"Кен_Кёнашима",
	"Кохару_Хината",
	"Маая_Оши",
	"Махиро_Хонда",
	"Меи_Мио",
	"Мурасаки_Нобумото",
	"Нагако_Андо",
	"Нагахару_Курудо",
	"Окимото_Фурукава",
	"Оми_Охара",
	"Джокичи_Юдасей",
	"Райзо_Мориока",
	"Райму_Ичиджо",
	"Ран_Учимара",
	"Рейичи_Танаами",
	"Риоба_Аиши",
	"Рюсей_Коки",
	"Сабуро_Мешино",
	"Сачи_Ёнеяма",
	"Сачихико_Фукуока",
	"Сейширо_Саданага",
	"Соноко_Саканоуэ",
	"Сора_Сосуке",
	"Сота_Юки",
	"Тадааки_Сунада",
	"Тайчи_Хиранака",
	"Такако_Уэда",
	"Тиру_Суторику",
	"Того_Атацума",
	"Уи_Тунесу",
	"Уманосукэ_Ёшинари",
	"Умеко_Учияма",
	"Фуджио_Кио",
	"Фуджиэ_Хайджима",
	"Фуюкичи_Като",
	"Фуюми_Тачики",
	"Ханаэ_Оно",
	"Харуто_Юто",
	"Хачиро_Исо",
	"Хаято_Харуки",
	"Химеко_Дерегучи",
	"Хозуми_Такеда",
	"Хонока_Киёкава",
	"Чидори_Икегами",
	"Чизуру_Ямагучи",
	"Чикао_Цурумаки",
	"Чуджиро_Китасуме",
	"Шинако_Бунзай",
	"Шичиро_Куросапу",
	"Эйичи_Асари",
	"Эйко_Ногучи",
	"Эцуджи_Одака",
	"Эцуко_Хаяшибара",
	"Юи_Рио",
	"Юна_Хина",
	"Яхико_Онода",
	"Яэ_Огата",
	"Кёко_Коясу",
	"Джури_Нагасава",
	"Муцуко_Нишимура",
	"Нориё_Хирамацу",
	"Отомэ_Нагасако",
	"Рёко_Угаки",
	"Сузуко_Нака",
	"Цуру_Кария"
]

exceptions = {
	"Ируки": "Irukas",
	"Аджии": "Ajias",
	"Берумы": "Berumas",
	"Борупена": "Borupens",
	"Гемы": "Gemas",
    "Гиты": "Gitas",
    "Доры": "Doras",
    "Каги": "Kagas",
    "Кибы": "Kibas",
    "Кизаны": "Kizanas",
    "Коконы": "Kokonas",
    "Кокумы": "Kokumas",
    "Маки": "Makas",
    "Меки": "Mekas",
    "Мины": "Minas",
    "Муджи": "Mujas",
    "Оки": "Okas",
    "Осаны": "Osanas",
    "Сакуры": "Sakuras",
    "Сенпая": "Senpais",
    "Супаны": "Supanas",
    "Тоги": "Togas",
    "Уэкии": "Uekiyas",
    "Ханы": "Hanas",
    "Хоруды": "Horudas",
    "Шимы": "Shimas",
    "Шина": "Shins",
    "Генки": "Genkas",
    "Кахо_Канокоги": "Kaho_Kanokogis",
    "Миды": "Midas",
    "Рейны": "Reinas",
    "Кагуи": "Kaguyas",
    "Чигусы": "Chigusas",
	"Азумы": "Azumas",
	"Азусы": "Azusas",
	"Айки": "Aikas",
	"Ваки": "Wakas",
	"Готы": "Gotas",
	"Кена": "Kens",
	"Мааи": "Maayas",
	"Риобы": "Ryobas",
	"Рюсея": "Ryuseis",
	"Соры": "Soras",
	"Соты": "Sotas",
	"Хоноки": "Honokas",
	"Юны": "Yunas"
}

"""for j in names_1980:
	res = []
	boo = False
	current_folder_files = listdir(f"images/1980/{j}/Портреты")
	for i in current_folder_files:
		a = i.split('_')
		if len(a) == 1:
			boo = True
			break
		if any(map(lambda x: x.isdigit(), list(a[2]))):
			if a[1] not in exceptions:
				res.append(f"{translit_to_jp(a[1])}s Porträt {a[2]}")
			else:
				res.append(f"{exceptions[a[1]]} Porträt {a[2]}")
		else:
			if a[1] not in exceptions:
				res.append(f"{translit_to_jp(a[1])}s Porträt (aktuell){a[2][-4:]}")
			else:
				res.append(f"{exceptions[a[1]]} Porträt (aktuell){a[2][-4:]}")
#		res.append("{0}_{1}_({2}ansicht){3}".format(
#													translit_to_jp(a[0]),
#													translit_to_jp(a[1]),
#													{"спереди":"vorder", "справа":"rechte ", "слева":"linke ", "сзади":"rücken"}[a[2].split()[1][:-5]],
#													a[2].split()[1][-4:]))
	if boo: continue
	print(res)
	input("Ok?")
	for i in range(len(current_folder_files)):
		rename(f"images/1980/{j}/Портреты/{current_folder_files[i]}", f"images/1980/{j}/Портреты/{res[i]}")
"""

res = []
list_ = []
with open("List.json", "r", encoding="utf8") as file:
    list_ = load(file)

for i in list_:
    res.append("_".join(map(translit_to_jp, i.split("_"))))

with open("List1.json", "w", encoding="utf8") as file:
    dump(res, file)