# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__


def print_readable_names(func_name, *args):
    print(func_name.replace('_', " ").title()+':', *args)


def open_browser(browser_name):
    print_readable_names(open_browser.__name__, browser_name)


def go_to_companyname_homepage(page_url):
    print_readable_names(go_to_companyname_homepage.__name__, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_readable_names(find_registration_button_on_login_page.__name__, button_text, page_url)

open_browser('Chrome')
go_to_companyname_homepage('yandex.ru')
find_registration_button_on_login_page('yandex.ru',  'Вы в танцах')