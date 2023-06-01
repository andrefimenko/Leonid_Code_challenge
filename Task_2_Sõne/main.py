sõne = "()[{}(())]"
# sõne = "]]]]"
# sõne = "(({[]}){})"
# sõne = "{{()[}}]abra"
# sõne = 'abra'
# sõne = ""


def show_test_result(string_brackets, result):
    if result:
        result = "correct"
    else:
        result = "NOT correct"
    print(f"The string of brackets {string_brackets} is {result}.")


def string_decomposition(bracket_string):
    while True:
        if '()' in bracket_string or '[]' in bracket_string or '{}' in bracket_string:
            for pair in ['()', '[]', '{}']:
                bracket_string = bracket_string.replace(pair, '')
        elif bracket_string == '':
            show_test_result(sõne, True)
            break
        else:
            show_test_result(sõne, False)
            break


if __name__ == "__main__":

    sõne_copy = sõne[:]

    if not sõne:
        print("The string is empty!!!")
    elif len(sõne) % 2 != 0:
        show_test_result(sõne, False)
    else:
        string_decomposition(sõne_copy)
