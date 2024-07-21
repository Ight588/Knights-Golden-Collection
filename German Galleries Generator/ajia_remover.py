import os

names = [
	"Аджии",
	"Аканэ",
	"Амай",
	"Аой",
	"Асу",
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
	"Кизаны",
	"Коконы",
	"Кокоро",
	"Кокумы",
	"Куроко",
	"Куу",
	"Кьюджи",
	"Май",
	"Маки",
	"Мантаро",
	"Мегами",
	"Меки",
	"Мидори",
	"Мины",
	"Миюджи",
	"Мусуме",
	"Оки",
	"Осаны",
	"Осоро",
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
	"Ханако",
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
	"Генки",
	"Карин",
	"Кахо_Канокоги",
	"Киоши",
	"Кочо",
	"Миды",
	"Муджи",
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
#	"Маэ",
	"Муцуко",
	"Нориё",
	"Отомэ",
	"Рёко",
	"Сузуко",
	"Цуру"
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

#for j in names_1980:
#	current_folder_files = os.listdir(f"images/1980/{j}/Портреты")
#	for i in current_folder_files: 
#		if i[0] in "QWERTYUIOPASDFGHJKLZXCVBNM":
#			os.remove(f"images/1980/{j}/Портреты/{i}")

#for i in names_1980:
#    current_folder_files = os.listdir(f"images/1980/{i}")
#    os.mkdir(f"images/1980/{i}/Портреты/{j}")
#    for j in current_folder_files:
#        os.replace(f"images/1980/{i}/{j}", f"images/1980/{i}/Портреты/{j}")
            
#for i in ("202X", "1980"):
#	for j in os.listdir(f"images/{i}"):
#		for k in ("Модель", "Репутация", "Портреты", "Профили", "Интересы"):
#			try:
#				for g in os.listdir(f"images/{i}/{j}/{k}"): 
#					os.replace(f"images/{i}/{j}/{k}/{g}", f"images/{g}")
#			except FileNotFoundError:
#				continue

for i in ("202X", "1980"):
    for j in os.listdir(f"images/{i}"):
        for k in ("Модель", "Репутация", "Портреты", "Профили", "Интересы"):
            pass