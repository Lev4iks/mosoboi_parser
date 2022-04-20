import settings
import wallpapers_parser
import db_connector as db


def main():

    settings.URL = str(input("Введите ссылку : "))
    wallpapers_parser.run()


if __name__ == '__main__':
    try:
        main()
        print("Первые 5 значений : ", *db.get_first_five_items())
        print("Последние 5 значений : ", *db.get_last_five_items())
    except Exception as e:
        print("Произошла ошибка... \n"
              f"[ERROR] {e}")
    finally:
        input("Нажмите кнопку ENTER для окончания работы...")
