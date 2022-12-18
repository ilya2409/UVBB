# open file in read mode
file = open("../demo.txt", "r")
replaced_content = ""

# looping through the file
for line in file:
    # stripping line break
    line = line.strip()

    # replacing the texts
    new_line = line.replace("@", "<p> asd </p>" + "\n" + "\n" + "@")

    # concatenate the new string and add an end-line break
    replaced_content = replaced_content + new_line + "\n"

# close the file
file.close()

# Open file in write mode
write_file = open("../demo.txt", "w")

# overwriting the old file contents with the new/replaced content
write_file.write(replaced_content)

# close the file
write_file.close()