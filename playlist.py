import json
from track import Track
class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracklist = [] # спсиок треков


    # 1.Показать треки
    def show_tracks(self):
        if not self.tracklist:
            print('Треков пока нет.')
            return

        for i, track in enumerate(self.tracklist, 1):
            print(f"--- Трек {i} ---")
            print(f'Автор - {track.executor}\nТрек - {track.name}\nИнформация - {track.information}.\n')

    # 2.Добавить трек
    def add_track(self):
        while True:
            print('\n1) Добавить трек')
            print('2) Меню.')

            try:
                option = input('Введите номер действия: ')
                if not option:
                    print('Ошибка! Ввод пустой строки.')
                    continue

                option = int(option)
                if option == 1:
                    name = input("Название трека: ")
                    author = input("Автор: ")
                    information = input("Информация: ")
                    if not name or not author or not information:
                        print('Ошибка: Ввод пустой строки!')
                        continue
                    else:
                        track = Track(author, name, information)
                        self.tracklist.append(track)
                        print(f'Трек "{name}" добавлен!')


                elif option == 2:
                    return
                else:
                    print('Такого номера задачи нет.')
            except ValueError:
                print('Ошибка! Ввод буквы или знака.\nНужно ввести номер(число) задачи.')

    # 3.Удалить трек
    def delete_track(self):
        self.show_tracks()

        if not self.tracklist:
            return
        while True:
            print('1) Удалить трек')
            print('2) Меню.')

            try:
                option = input('Введите номер действия: ')
                if not option:
                    print('Ошибка! Ввод пустой строки.\n')
                    continue

                option = int(option)
                if option == 1:
                    number = input("Введите номер трека для удаления: ")
                    if not number:
                        print('Ошибка: Ввод пустой строки!\n')
                        continue
                    elif not number.isdigit():
                        print("Нужно ввести номер(число)!\n")
                    else:
                        number = int(number)
                        if 1 <= number <= len(self.tracklist):
                            track = self.tracklist.pop(number - 1)
                            print(f'Трек "{track.name}" удалён.\n')
                        else:
                            print('Такого трека нет.\n')
                elif option == 2:
                    break
                else:
                    print('Такого номера задачи нет.')
            except ValueError:
                print('Ошибка! Ввод буквы или знака.\nНужно ввести номер(число) задачи.\n')

    # 4.Найти трек по номеру
    def find_the_track(self):
        print("Список треков:")
        self.show_tracks()

        if not self.tracklist:
            return

        number = input("Введите номер трека: ")
        if not number:
            print('Ошибка: ввод пустой строки!')
            return
        elif not number.isdigit():
            print("Нужно ввести номер(число)!")
        else:
            number = int(number)
            if 1 <= number <= len(self.tracklist):
                track = self.tracklist[number - 1]
                print("Название:", track.name)
                print("Автор:", track.executor)
                print("Информация:", track.information)

    # 5.Изменить трек
    def change_track(self):
        self.show_tracks()

        if not self.tracklist:
            return

        try:
            number = input("Введите номер трека: ")
            if not number:
                print('Ошибка: ввод пустой строки!')
                return

            number = int(number)
            if 1 <= number <= len(self.tracklist):
                track = self.tracklist[number - 1]

                while True:
                    print('1) Изменить только название трека')
                    print('2) Изменить только автора трека')
                    print('3) Изменить только информацию трека')
                    print('4) Изменить название, автора, информацию трека')
                    print('5) Выход.')

                    option = input('\nВведите номер действия: ')

                    option = int(option)
                    if option == 1:
                        new_name = input("Введите новое название: ")
                        if not new_name:
                            print('Ошибка: ввод пустой строки!')
                            continue
                        track.name = new_name
                        print("Название изменено!")
                        return

                    elif option == 2:
                        new_executor = input('Введите нового автора: ')
                        if not new_executor:
                            print('Ошибка: ввод пустой строки!')
                        track.executor = new_executor
                        print('Автор изменён!')
                        return

                    elif option == 3:
                        new_information = input('Введите новую информацию: ')
                        if not new_information:
                            print('Ошибка: ввод пустой строки!')
                        track.information = new_information
                        print('Информация изменена!')
                        return

                    elif option == 4:
                        new_name = input("Введите новое название: ")
                        new_executor = input('Введите нового автора: ')
                        new_information = input('Введите новую информацию: ')
                        if new_name == '' or new_executor == '' or new_information == '':
                            print('Ошибка: ввод пустой строки!\n')
                            continue
                        track.name = new_name
                        track.executor = new_executor
                        track.information = new_information
                        print('Всё изменено!')
                        return

                    elif option == 5:
                        print('Без изменений.')
                        break

            else:
                print('Трек не найден.')
        except ValueError:
            print('Ошибка! Ввод буквы или знака.\nНужно ввести номер(число) задачи.')

    # 6.Сохранить в JSON
    def save_to_json(self):
        self.show_tracks()

        if not self.tracklist:
            return

        try:
            number = input("Введите номер трека: ")
            if not number:
                print('Ошибка: ввод пустой строки!')
                return

            number = int(number)
            track = self.tracklist[number - 1]

            try:
                with open("tracklist.json", "r", encoding="utf-8") as file:
                    tracks = json.load(file)

                    if isinstance(tracks, dict):
                        tracks = [tracks]
            except (FileNotFoundError, json.JSONDecodeError):
                tracks = []
            tracks.append(track.to_dict())

            with open("tracklist.json", "w", encoding="utf-8") as file:
                json.dump(tracks, file, ensure_ascii=False, indent=4)
            print("Трек сохранена в JSON!")
        except ValueError:
            print('Ошибка! Ввод буквы или знака.\nНужно ввести номер(число) задачи.')
        except IndexError:
            print('Такого номера трека нет.')


    # 7.Загрузить из JSON
    def show_json(self):
        try:
            with open("tracklist.json", "r", encoding="utf-8") as file:
                tracks = json.load(file)
        except FileNotFoundError:
            print("Файл не найден!")
            return

        for i, track in enumerate(tracks, 1):
            print(i, "-", track["name"])

        try:
            number = input("Введите номер трека: ")
            if not number:
                print('Ошибка: ввод пустой строки!')
                return
            number = int(number)
            track = tracks[number - 1]

            print("\nНазвание:", track["name"])
            print("Автор:", track["executor"])
            print("Информация:", track["information"])
        except IndexError:
            print('Такого номера трека нет.')
        except ValueError:
            print('Ошибка! Ввод буквы или знака.\nНужно ввести номер(число) задачи.')