tulemus = ['4', '2', 'B', '-2', '+', 'A']
# tulemus = ['A', '4', '2', 'B', '-2', '+', 'A']
# tulemus = ['B', '4', '2', 'B', '-2', '+', 'A']
# tulemus = ['+', '4', '2', 'B', '-2', '+', 'A']
# tulemus = [4, 2, 'B', -2, '+', 'A']
# tulemus = []


COND_1 = "длина массива tulemus может быть от 1 от 100"

COND_2 = "в массиве tulemus могут быть только символы " \
             "A, B, + или строковые представления чисел " \
             "от - 100 до 100"

COND_3 = "перед применением операции + должны быть доступны " \
         "счёты двух предыдущих раундов"

COND_4 = "перед применением операций A или B должен быть" \
         " доступен счёт предыдущего раунда"


def show_input_test_result(array, condition):
    print(f"Массив {array} не проходит проверку условия: {condition}")


def calculation(array):
    res_list = []

    for symbol in array:
        if isinstance(symbol, str):
            try:
                symbol = int(symbol)

                if symbol >= -100 & symbol <= 100:
                    res_list.append(int(symbol))
                else:
                    show_input_test_result(array, COND_2)
                    res_list.clear()
                    break

            except ValueError:
                if symbol == '+':
                    try:
                        res_list.append(res_list[-1] + res_list[-2])
                    except IndexError:
                        show_input_test_result(array, COND_3)
                        break
                elif symbol == 'A':
                    try:
                        res_list.append(res_list[-1] * 2)
                    except IndexError:
                        show_input_test_result(array, COND_4)
                        break
                elif symbol == 'B':
                    try:
                        res_list.pop()
                    except IndexError:
                        show_input_test_result(array, COND_4)
                        break
                else:
                    show_input_test_result(array, COND_2)
                    break
        else:
            show_input_test_result(tulemus, COND_2)
            res_list.clear()
            break

    if res_list != []:
        return print(sum(res_list))

if __name__ == "__main__":

    if len(tulemus) < 1 or len(tulemus) > 100:
        show_input_test_result(tulemus, COND_1)
    else:
        calculation(tulemus)
