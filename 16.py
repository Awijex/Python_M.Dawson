# Доступ отовсюду
# Демонстрация работы с глобальными переменными


def read_global():
    print("В области видимости функции read_global() значение value равно", value)


def shadow_global():
    value = -10
    print("В области видимости функции shadow_global() значение value равно", value)


def change_global():
    global value
    value = -10
    print("В области видимости функции change_global() значение value равно", value)


value = 10
print("В глобальной области видимости значение переменной value теперь равно", value)
read_global()
print("Здесь value равно попрежнему", value)
shadow_global()
print("Здесь value равно попрежнему", value)
change_global()
print("Вернемся в глобальную область видимости, значение value изменилось на", value)



