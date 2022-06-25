from pprint import pprint
my_file = 'recipes.txt'



def menu_reader(file_name: str) -> dict:
    with open(file_name, encoding="utf-8") as menu:
        cook_book = {}
        for line in menu:
            dish = line.strip()
            # print(f'Название блюда: {dish}')
            foods = []
            quantity = menu.readline()
            # print(quantity)
            # print('Состав блюда:')
            for dish_part in range(int(quantity)):
                food = menu.readline().strip()
                food = food.split('|')
                # print(food)
                food_divided = {}
                food_divided['ingredient_name'] = food[0].strip()
                food_divided['quantity'] = food[1].strip()
                food_divided['measure'] = food[2].strip()
                foods.append(food_divided)
                # print(menu.readline().strip())
            cook_book[dish] = foods
            menu.readline()

    return cook_book

cook_book = menu_reader(my_file)
# pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    print(f'Количество персон {person_count}')
    for dish in dishes:
        for ingridient in cook_book[dish]:
          if ingridient['ingredient_name'] not in shop_list:
            ingridient_info = {}
            ingridient_info['measure'] = ingridient['measure']
            total_amount = int(ingridient['quantity']) * person_count
            ingridient_info['quantity'] = total_amount
            shop_list[ingridient['ingredient_name']] = ingridient_info
          else:
            ingridient_info = {}
            ingridient_info['measure'] = ingridient['measure']
            total_amount = int(ingridient['quantity']) * person_count
            ingridient_info['quantity'] = total_amount + shop_list[ingridient['ingredient_name']]['quantity']
            shop_list[ingridient['ingredient_name']] = ingridient_info
    return(shop_list)


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Омлет'], 1))
