# Define alcohol content for each ingredient (in grams of alcohol per gram of ingredient)
alcohol_content = [0.28, 0.43, 0.0, 0.0, 0.4, 0.21, 0.4, 0.0, 0.2, 0.0, 0.0, 0.4, 0.4, 0.0, 0.0, 0.0, 0.2, 0.0]  # Example, 0.2 equates to 20 % alcohol>

def calculate_alcohol_level(ingredient_list):
    total_alcohol = 0
    total_grams = 0
    for ing_id, ing_weight in ingredient_list:
        if ing_id < len(alcohol_content):
            alcohol = alcohol_content[ing_id] * ing_weight
            total_alcohol += alcohol
            total_grams += ing_weight
        else:
            print(f"Ingredient {ing_id} is not in the database. Skipping...")

    return total_alcohol, total_grams

def main():
    try:
        ingredient_input = input("Enter ingredient list (format: ingredient_id1.weight ingredient_id2.weight ...): ")
        ingredients = ingredient_input.split()

        if len(ingredients) == 1:
            ingredient_id, ing_weight = ingredients[0].split('.')
            ingredient_list = [(int(ingredient_id) - 1, float(ing_weight))]  # Adjusting the ingredient ID to match 0-based indexing
            total_grams = float(ing_weight)
        else:
            ingredient_list = [(int(ing.split('.')[0]) - 1, float(ing.split('.')[1])) for ing in ingredients]  # Adjusting the ingredient ID to match 0-based indexing
            total_grams = sum(weight for _, weight in ingredient_list)

        alcohol_level_grams, _ = calculate_alcohol_level(ingredient_list)

        # Calculate the alcohol content percentage using the total weight as total volume
        alcohol_content_percentage = (alcohol_level_grams / total_grams) * 100

        print(f"Total grams of the drink: {total_grams} grams")
        print(f"Alcohol content of the drink: {alcohol_content_percentage:.2f}%")

    except ValueError:
        print("Invalid input format. Please enter ingredient ID and weight pairs separated by space.")

if __name__ == "__main__":
    main()
