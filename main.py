import requests
import codecs
from jinja2 import Environment, FileSystemLoader

# API endpoints
LIST_API_URL = "http://localhost:7171/api/list"
DETAIL_API_URL = "http://localhost:7171/api/detail/"

def get_screenshots():
    response = requests.get(LIST_API_URL)
    #print(response.json())
    return response.json()

def get_screenshot_detail(id):
    response = requests.get(DETAIL_API_URL + str(id))
    return response.json()

def generate_html(screenshots,perception_screenshots):
    env = Environment(loader=FileSystemLoader('templates'))

    template_table = env.get_template('table.html')
    template_gallery = env.get_template('gallery.html')
    template_perception = env.get_template('perception.html')

    # Генерируем HTML
    table_html_content = template_table.render(screenshots=screenshots)
    gallery_html_content = template_gallery.render(screenshots=screenshots)
    perception_html_content = template_perception.render(screenshots=perception_screenshots)

    with codecs.open('table.html', 'w', 'utf-8') as f:
        f.write(table_html_content)

    with codecs.open('gallery.html', 'w', 'utf-8') as f:
        f.write(gallery_html_content)

    with codecs.open('perception.html', 'w', 'utf-8') as f:
        f.write(perception_html_content)

def group_screenshots_by_perception(detailed_screenshots):
    grouped_data = {}
    # Группируем скриншоты по PerceptionHash
    for screenshot in detailed_screenshots:
        hash_key = screenshot['PerceptionHash']
        if hash_key not in grouped_data:
            grouped_data[hash_key] = {
                'URLS': [],
                'Title': screenshot['Title'],
                'ResponseCode': screenshot['ResponseCode'],
                'PerceptionHash': hash_key,
                'Filename': screenshot['Filename']
            }
        grouped_data[hash_key]['URLS'].append(screenshot['URL'])

    # Преобразуем словарь в список для удобства работы с шаблонами
    return list(grouped_data.values())

def main():
    screenshots_list = get_screenshots()
    detailed_screenshots = []


    # Получаем детальную информацию по каждому скриншоту
    for screenshot in screenshots_list:
        detail = get_screenshot_detail(screenshot['ID'])
        detailed_screenshots.append(detail)
        #print(detail)
        # if screenshot['ID'] == 300:
        #     break

    group_screenshots = group_screenshots_by_perception(detailed_screenshots)
    print(group_screenshots)


    # Генерация HTML
    generate_html(detailed_screenshots,group_screenshots)

if __name__ == "__main__":
    main()
