import requests

url = 'http://localhost:8000/api/item/get'

def get_items():
    response = requests.get(url)
    item_dict = {}
    if response.status_code == 200:
        data = response.json()
        with open('itens.txt', 'w') as file:
            for item in data:
                item_name = item['item']
                x_value = item['x']
                y_value = item['y']
                file.write(f'O {item_name} se encontra em x: {x_value} e y: {y_value}\n')
                item_dict[(x_value, y_value)] = item_name
    else:
        print("Ocorreu um erro:", response.status_code)
    return item_dict

if __name__ == '__main__':
    items = get_items()
    print(items)
