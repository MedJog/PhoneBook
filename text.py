
main_menu = '''Главное меню
1. Открыть файл
2. Сохранить файл
3. Показать все контакты
4. Создать новый контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
8. Выход
'''
menu_choise = 'Выберите пункт меню: '
input_error = 'Некорректный ввод. Введите число от 1 до 8.'
book_error = 'Телефонная книга пуста или файл не открыт.'
open_successful = 'Телефонная книга успешно открыта.'
input_new_contact = 'Введите данные нового контакта: '
new_contact = ['Введите имя контакта: ', 'Введите телефонный номер:', 'Введите комментарий: ']
search_word = 'Введите искомый элемент: '
input_index = 'Введите индекс изменяемого контакта: '
input_change_contact = 'Введите данные изменяемого контакта или Enter, чтобы оставить без изменеий.'
input_index_del = 'Введите индекс контакта, который хотите удалить: '

def contact_saved(name: str):
    return f'Контакт {name} успешно сохранён.'

def contact_changed(name: str):
    return f'Контакт {name} успешно изменён.'

def contact_deleted():
    return f'Контакт удалён.'
