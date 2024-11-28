

def read_recipes_from_file(file):
    cook_book = {}
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = f.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[dish_name] = ingredients
    return cook_book

def main():
    file = 'hello.txt'
    cook_book = read_recipes_from_file(file)
    print(cook_book)

if __name__ == '__main__':
    main()