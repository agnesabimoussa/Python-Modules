def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = ["fire", "water", "earth", "air"]
    ing_list = ingredients.lower().strip().split(" ")
    for ing in ing_list:
        if ing not in valid_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
