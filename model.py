phone_book = []
path = 'phones.txt'

def open_file():
    with open(path, 'r', encoding = 'UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment = contact.strip() .split(':')
        phone_book.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})

def check_id():
    user_id_list = []
    for contact in phone_book:
        user_id_list.append(int(contact.get('id')))
    return {'id': max(user_id_list) + 1}

def add_new_contact(new: dict):
    new.update(check_id())
    phone_book.append(new)

def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result

def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index-1][key] = field

def delete_contact(index: int):
    del phone_book[int(index)-1]

def save_file(phone_book):
    with open(path, "w", encoding = 'UTF-8') as file:
        file.write('')
    with open(path, "a", encoding = 'UTF-8') as file:
        for contact in phone_book:
            file.write(str(contact.get('id'))+':'
                        +contact.get('name')+':'
                        +contact.get('phone')+':'
                        +contact.get('comment')+'\n')
  