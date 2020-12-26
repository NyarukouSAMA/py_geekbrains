import re
from bs4 import BeautifulSoup as BS
# Нет страницы на сайте с которой нужно парсить! взял обычную страницу с учениками на курсе и запарсил данные


def get_text_from_file(path):
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            return f.read()
    except Exception as ex:
        print(f'Ошика в функции get_text_from_file - {ex}')


def show_all_students(list):
    for student in list:
        print(student)


def get_students_re(page):
    pattern_script = re.compile('<a class="mates-list__mate-image-block send_message_on_hover.*?data-name="(.*?)"',
                                re.DOTALL)
    return re.findall(pattern_script, page)


# парсинг со страницы где сбоку есть ментор и ученики
text = get_text_from_file('geekbrains.html')
if text:
    # Получаем с помощью RE
    list_students = get_students_re(text)
    show_all_students(list_students)
    print(f'RE - Количество студентов на курсе: {len(list_students)}')

    # Получаем с помощью BS4
    soup = BS(text, 'html.parser')
    li = soup.find_all("a", class_='mates-list__mate-image-block send_message_on_hover js-send-message')
    for n in li:
        print(n.get("data-name", ""))

    print(f'BS4 - Количество студентов на курсе: {len(li)}')

