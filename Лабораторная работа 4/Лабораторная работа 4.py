import json
import xml.etree.ElementTree as ET

# Функция для чтения JSON файла


def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Функция для конвертации данных в формат XML


def convert_to_xml(data):
    root = ET.Element("People")

    for person in data:
        person_element = ET.SubElement(root, "Person")

        for key, value in person.items():
            child = ET.SubElement(person_element, key)
            child.text = str(value)

    return ET.tostring(root, encoding='utf-8').decode('utf-8')

# Основная программа


def main():
    json_file_path = 'data.json'

    # Чтение данных из JSON файла
    data = read_json_file(json_file_path)

    # Конвертация в XML
    xml_data = convert_to_xml(data)

    # Сохранение XML данных в файл
    with open('data.xml', 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_data)

    print("Конвертация завершена! Данные сохранены в data.xml")


main()
