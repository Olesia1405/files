with (open('2.txt', 'r', encoding='utf-8') as f2,
      open('1.txt', 'r', encoding='utf-8') as f1,
      open('3.txt', 'r', encoding='utf-8') as f3,
      open('output.txt', 'w', encoding='utf-8') as f):
    files = [('file2.txt', f2), ('file1.txt', f1), ('file3.txt', f3)]
    for file_name, file in files:
        lines = file.readlines()
        line_count = len(lines)
        f.write(f"{file_name}\n")
        f.write(f"{line_count}\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"Строка номер {i} файла номер {file_name[4:]}: {line}")

