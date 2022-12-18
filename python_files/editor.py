def add_text(text):
    file = open('../html_pages/index_page.html', 'a', encoding='utf-8')
    file.writelines('\n' + f"<p>{text}</p>" + '\n' + '@')


def add_image(text):
    file = open('../html_pages/index_page.html', 'a', encoding='utf-8')
    file.writelines("\n" + '<img class="images" src=' + '"' + text + '"' + ">" + '\n' + '@')


def del_text():
    file = open('html_pages/index_page.html', 'r', encoding='utf-8')
    lines = file.readlines()
    lines = lines[:-1]

    with open('  html_pages/index_page.html', 'w', encoding='utf-8') as f:
        f.writelines(lines)