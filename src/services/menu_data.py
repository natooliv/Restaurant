from src.models.dish import Dish, Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path) as restaurant_file_csv:
            data_reader = csv.DictReader(restaurant_file_csv)
            dish_map = {}

            for row in data_reader:
                dish_name = row["dish"]
                recipe_price = float(row["price"])
                ingredient_name = row["ingredient"]
                ingredient_amount = int(row["recipe_amount"])

                if dish_name not in dish_map:
                    dish_map[dish_name] = Dish(dish_name, recipe_price)

                dish_map[dish_name].add_ingredient_dependency(
                    Ingredient(ingredient_name), ingredient_amount)

            self.dishes = set(dish_map.values())
