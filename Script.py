import fitz
import json

# Извлекаем элементы из PDF-файла
def extract_elements_from_pdf(pdf_file_path):
    pdf_document = fitz.open(pdf_file_path)
    elements = []

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text_blocks = page.get_text("blocks")

        for block in text_blocks:
            element = {
                "text": block[4],
                "x0": block[0],
                "y0": block[1],
                "x1": block[2],
                "y1": block[3]
            }
            elements.append(element)

    pdf_document.close()
    return elements

# Сравниваем элементов двух списков
def compare_elements(list1, list2):
    result = {}

    # Создаем множества из текстов элементов в списках
    set1 = set(element["text"] for element in list1)
    set2 = set(element["text"] for element in list2)

    # Сравниваем множества и находим различия
    result["list1"] = list(set1 - set2)
    result["list2"] = list(set2 - set1)

    return result

# Извлекаем элементы из обоих PDF-файлов
pdf_file_path1 = "pdf/task.pdf"
pdf_file_path2 = "pdf/task2.pdf"

elements_pdf1 = extract_elements_from_pdf(pdf_file_path1)
elements_pdf2 = extract_elements_from_pdf(pdf_file_path2)

# Сравниваем элементы
comparison_result = compare_elements(elements_pdf1, elements_pdf2)

# Выводим результат сравнения
pretty_json = json.dumps(comparison_result, indent=4, ensure_ascii=False)
print(pretty_json)

# Выводим элементы из "list1", которые отсутствуют в "list2"
list1 = comparison_result.get("list1")
if list1:
    print("\nЭлементы из 'list1', которые отсутствуют в 'list2':")
    for element in list1:
        print(element)
else:
    print("\nВсе элементы из 'list1' присутствуют в 'list2'.")

# Выводим список
all_elements_pdf1 = [element["text"] for element in elements_pdf1]
print("\nВсе элементы из task.pdf:")
print(all_elements_pdf1)