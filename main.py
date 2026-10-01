from playlist import Playlist
playlist = Playlist("Мой плейлист")

def menu(playlist):
    while True:
        print('\n==Главное меню.==\nМеню действий: ')
        print('1.Показать треки')
        print('2.Добавить трек')
        print('3.Удалить трек')
        print('4.Найти трек по номеру')
        print('5.Изменить трек')
        print('6.Сохранить в JSON')
        print('7.Загрузить из JSON')
        print('8.Выход.\n')

        action = input('Введите номер действия: ')
        if action == '':
            print('Ошибка: ввод пустой строки.')
            continue
        elif not action.isdigit():
            print("Нужно ввести номер(число)!")
            continue
        else:
            action = int(action)
            if action == 1:
                playlist.show_tracks()

            elif action == 2:
                playlist.add_track()

            elif action == 3:
                playlist.delete_track()

            elif action == 4:
                playlist.find_the_track()

            elif action == 5:
                playlist.change_track()

            elif action == 6:
                playlist.save_to_json()

            elif action == 7:
                playlist.show_json()


            elif action == 8:
                print("Выход.")
                break

            else:
                print('Такого номера действия нет.')
menu(playlist)