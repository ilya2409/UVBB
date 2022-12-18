from python_files.test_editor import add_2

bumashka_data = "| none |"

mini_key = "qwerty-off"


def mini_latter(latter_text):
    with open('hello.py') as latter_a:
        latter_a = sum(1 for _ in latter_a)
        print(latter_a)

    with open("hello.py", "a") as file_a:
        file_a.write(f"latter_number{latter_a + 1} = '{latter_text}'" + "\n")


def latter_prog(text_a):
    text_b = text_a.split("\n")
    print(text_b)
    if len(text_b) > 2:
        author_b = text_b[2]
    else:
        author_b = "Anonim)"
    tema = text_b[1]
    tip_b = "txt"
    add_2(tip_b, tema, author_b)
