# from python_files.test_editor import add_2, dell_2, search_2
from python_files.editor_2 import create, dell_2, search_2

mini_key = "qwerty-off"
new_type = "new_type"
new_header = "new_header"
new_content = "new_content"
new_author = "new_author"


def latter_prog(text_a):
    text_b = text_a.split("\n")
    global new_type, new_header, new_content, new_author
    print("\n")
    print(f"text_b: {text_b}")

    new_type = text_b[0].split()[0]
    new_header = text_b[0][2:-1]
    new_content = text_b[1]
    new_author = text_b[2]

    print(f"new_header: {new_header}")

    if new_type == "#comment":
        create("txt", new_header, new_content, new_author)

    elif new_type == "#image":
        create("img", new_header, new_content, new_author)

    elif "#delete" in text_a:
        com = search_2(text_a.split()[1])
        print(f"serch_2.com: {com}")
        dell_2(com)

    else:
        create("txt", new_header, new_content, new_author)


def mini_latter(latter_text):
    global new_header

    with open('hello.py') as latter_a:
        latter_a = sum(1 for _ in latter_a)
        print(f"latter_a: {latter_a}")
    latter_out = latter_text.split("\n")

    with open("hello.py", "a") as file_a:
        file_a.write(f"""latter_{new_header} = {latter_out} """ + "\n")
        # file_a.write(f'latter_number{latter_a + 1} = """{latter_text}"""' + "\n")


# latter_out = "latter result"
# latter_result = latter_out.split("\n")
