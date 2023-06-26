
import text


def menu() -> int:
    print(text.main_menu)
    while True:
        choise = input(text.menu_choise)
        if choise.isdigit() and 0 < int(choise) < 9:
            return int(choise)
        print(text.input_error)

def show_contacts(book: list[dict[str, str]]):
    if book:
        print('\n' + '=' * 67)
        for contact in book:
            user_id = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{user_id:>3}. {name:<20} {phone:<20} {comment:<20}')
        print('=' * 67 + '\n')
    else:
        print(text.book_error)

def print_message(message: str):
    lenght = len(message)
    print('\n' + '=' * lenght)
    print(message)
    print('=' * lenght + '\n')

def input_contact(message: str) -> dict[str, str]:
    print(message)
    name = input(text.new_contact[0])
    phone = input(text.new_contact[1])
    comment = input(text.new_contact[2])
    return {'name': name, 'phone': phone, 'comment': comment}

def input_return(message: str) -> str:
    return input(message)

