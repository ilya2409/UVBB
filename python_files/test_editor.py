
def add_2(tip, content, author):

    tag = "qwerty"
    end_tag = "qwerty_end"

    if tip in ("txt", "text", "commit", "coment", "текст", "комент", "коментарий"):
        tag = "<p>"
        end_tag = "</p>"

    elif tip in ("img", "image", "gif", "pictures"):
        tag = "img"
        end_tag = " "

    else: print("Вы указали неверный тип файла(")

    # open file in read mode
    file = open("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page.html", "r", encoding="utf-8")
    replaced_content = ""

    # looping through the file
    for line in file:
        # stripping line break
        line = line.strip()

        # replacing the texts
        if tip in ("txt", "text", "commit", "coment", "текст", "комент", "коментарий"):
            new_line = line.replace(

                """<a href="#up_up" class="dop_key" id="k_1">@</a>""",
                str(tag) + f"{author}:" +
                "<br>" + f"{content}" +
                str(end_tag) + "\n" + "\n" +
                """<a href="#up_up" class="dop_key" id="k_1">@</a>""")

        elif tip in ("img", "image", "gif", "pictures"):
            new_line = line.replace(
                """<a href="#up_up" class="dop_key" id="k_2">@</a>""",
                "<" + str(tag) + f""" alt="{author}:" """ +
                """ class="images" """ + f""" src="{content}" """ + ">"
                + "\n" + "\n" +
                """<a href="#up_up" class="dop_key" id="k_2">@</a>""")

        else: new_line = line.replace("@", str(tag) + f"{content}" + str(end_tag) + "\n" + "\n" + "@")

        # concatenate the new string and add an end-line break
        replaced_content = replaced_content + new_line + "\n"

    # close the file
    file.close()

    # Open file in write mode
    write_file = open("C:/Users/PC/PycharmProjects/pythonProject/html_pages/index_page.html", "w", encoding="utf-8")

    # overwriting the old file contents with the new/replaced content
    write_file.write(replaced_content)

    # close the file
    write_file.close()