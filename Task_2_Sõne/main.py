sõne = "()[{}(())]"
# sõne = "]]]]"
# sõne = "(({[]}){})"
# sõne = "{{()[}}]abra"
# sõne = 'abra'

sõne_copy = sõne[:]


def show_test_result(string_brackets, result):
    if result:
        result = "correct"
    else:
        result = "NOT correct"
    print(f"The string of brackets {string_brackets} is {result}.")


if len(sõne) % 2 != 0:
    show_test_result(sõne, False)


while True:
    if '()' in sõne_copy or '[]' in sõne_copy or '{}' in sõne_copy:
        for pair in ['()', '[]', '{}']:
            sõne_copy = sõne_copy.replace(pair, '')
    elif sõne_copy == '':
        show_test_result(sõne, True)
        break
    else:
        show_test_result(sõne, False)
        break
