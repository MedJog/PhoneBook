
from console import menu, show_contacts, print_message, input_contact, input_return
import model
import text

def start():
    while True:
        choise = menu()
        match choise:
            case 1:
                model.open_file()
                print_message(text.open_successful)
            case 2:
                model.save_file(model.phone_book)
                show_contacts(model.phone_book)
            case 3:
                show_contacts(model.phone_book)
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_new_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index)-1].get('name')
                print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))
            case 7:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index_del)
                model.delete_contact(int(index))
                print_message(text.contact_deleted())
               
            case 8:
                break