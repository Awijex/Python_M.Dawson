# Демонстрация работы функции len() и оператора in
message = input("Введите текст: ")
print('\nДлина введенного вами текста составляет:', len(message))
print("\nСамая частая согласная, 'т',")
if "т" in message:
    print("встречается в вашем тексте.")
else:
    print("не встречается в вашем тексте.")
input("\n\nНажмите энтер,чтобы выйти.")