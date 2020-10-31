import telebot

from ..models import Menu as SelfString


# Main menu
def menu_main():

    menu_items = [i.name for i in Menu.objects.filter(is_public=True, parent__isnull=True)]

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    keyboard.add(
        SelfString.get_string('btn_filters_info'),
        *menu_items
    )

    return keyboard
