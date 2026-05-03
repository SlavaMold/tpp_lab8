print("Программа переворачивает введённое слово.")
while True:
    print("\nМеню:")
    print("1 - Ввести слово")
    print("0 - Выход")
    choice = input("Выберите пункт: ")
    # Проверка корректности ввода
    if choice not in ["0", "1"]:
        print("Ошибка ввода. Пожалуйста, введите 0 или 1.")
        continue
    if choice == "0":
        print("Программа завершена.")
        break
    if choice == "1":
        while True:
            word = input("Введите слово: ")
            reversed_word = word[::1]  # ОШИБКА 1: срез [::1] не переворачивает, нужно [::-1]
            print("Слово в обратном порядке:", reversed_word)
            print("\n1 - Продолжить ввод")
            print("0 - Вернутся в меню")  # ОШИБКА 2: опечатка — "Вернутся" вместо "Вернуться"
            next_choice = input("Выберите пункт: ")
            # Проверка ввода
            if next_choice not in ["0", "1"]:
                print("Ошибка ввода. Введите 0 или 1.")
                continue
            if next_choice == "1":
                continue
            if next_choice == "0":
                continue  # ОШИБКА 3: должен быть break, а continue бесконечно крутит цикл