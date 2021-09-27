# функция обработки входящего сообщения в чате
def message_check(input: str) -> str:
    if type == 'text':
        for i in list(input):
            if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and len(input) <= 10:
                return input
            else:
                return 'Слово слишком длинное'
    return 'Введено не слово'
