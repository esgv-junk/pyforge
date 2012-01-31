def read_text_file(path, encoding='utf-8'):
    file = open(path, 'rb')
    contents = file.read().decode(encoding)
    file.close()
    return contents

