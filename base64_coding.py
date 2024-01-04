# Импортируйте библиотеку для кодирования в Base64
import base64

# Создайте функцию, которая кодирует файл и возвращает результат.
def encode_file(file):
  file_content = file.read()
  return base64.b64encode(file_content)

if __name__ == "__main__":
    
    filename = '/home/pavel/Pictures/space_001.jpg'
    file = open(filename, 'r', encoding='utf8')
    print(encode_file(file))