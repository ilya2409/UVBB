import os


def create(content_type, title, content, author: str = "ANONIM"):

    global replaced_content
    in_tag = "tag_in"
    out_tag = "tag_out"

    if content_type in ("txt", "text"):
        form_in = """<a href="#up_up" class="dop_key" id="k_1">@</a>"""
        form_out = f"""
<p id="{title}"> {author} | {title}<br><br> {content}</p>
            
<br><a href="#up_up" class="dop_key" id="k_1">@</a>
"""

        with open("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html", "r", encoding="utf-8") as file:
            replaced_content = ""
            for line in file:
                line = line.strip()

                new_line = line.replace(form_in, form_out)
                replaced_content = replaced_content + new_line + "\n"

        with open("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html", "w", encoding="utf-8") as write_file:
            write_file.write(replaced_content)

    elif content_type in ("img", "image"):
        in_tag = "tag_in"
        out_tag = "tag_out"

        form_in = """<a href="#up_up" class="dop_key" id="k_2">@</a>"""
        form_out = f"""
<div class="img"><img src="{content}" alt="{title}"></div>
   
<br><a href="#up_up" class="dop_key" id="k_2">@</a>
"""

        with open("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html", "r", encoding="utf-8") as file:
            replaced_content = ""
            for line in file:
                line = line.strip()

                new_line = line.replace(form_in, form_out)
                replaced_content = replaced_content + new_line + "\n"

        with open("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html", "w", encoding="utf-8") as write_file:
            write_file.write(replaced_content)

    else:
        content_type = "txt"
        title = "ERROR"


def search_2(stroka):
    with open("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html", encoding="utf-8") as infile:
        for line in infile:
            if str(stroka) in line:
                # print(f"line: {line}")
                # print(f"s_line: {s_line}")
                return line


def dell_2(id):
    FIND = str(id)
    INFILE = "C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html"
    OUTFILE = "C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_1.html"
    ENC = "utf-8"

    with open(INFILE, encoding=ENC) as infile, open(OUTFILE, "w", encoding=ENC) as outfile:
        for line in infile:
            if FIND not in line:
                outfile.write(line)

    os.remove("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html")
    os.rename("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_1.html", "C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page_0.html")