import requests

def drinks_by_name(cocktail_name):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_name}"
    response = requests.get(url)
    return response.json()

def drink_by_id(drink_id):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    response = requests.get(url)
    return response.json()

def extract_api_drink(drink_id):
    drink_dict_total = drink_by_id(drink_id)
    drink_dict ={}
    drink_dict['id'] = drink_dict_total['drinks'][0]['idDrink']
    drink_dict['name'] = drink_dict_total['drinks'][0]['strDrink']
    drink_dict['main_ingredient'] = drink_dict_total['drinks'][0]['strIngredient1']
    drink_dict['recipe'] = drink_dict_total['drinks'][0]['strInstructions']
    return drink_dict

def extract_ingredients(drink_id):
    drink_dict_total = drink_by_id(drink_id)
    drink_dict_access = drink_dict_total['drinks']
    drink_ingredients = []
    drink_name_and_ingredients = {}
    for key, value in drink_dict_access.items():
        if 'strIngredient' in key and value != 'null':
            drink_ingredients.append(value)        
        drink_name_and_ingredients= {'name': drink_dict_access['strIngredient'], 'ingredients': drink_ingredients}
    return drink_name_and_ingredients

def extract_ingredients_and_amounts(drink_id):
    name_and_ingredients = extract_ingredients(drink_id)
    drink_dict_total = drink_by_id(drink_id)
    drink_dict_access = drink_dict_total['drinks']
    drink_ingredients = []
    drink_measurements = []
    for key, value in drink_dict_access.items():
        if 'strMeasure' in key and value != 'null':
            drink_measurements.append(value)
    for key, value in drink_dict_access.items():
        if 'strIngredient' in key and value != 'null':
            drink_ingredients.append(value)
    ingredients_amounts = list(zip(drink_ingredients, drink_measurements))
    return {'name': drink_dict_access['strIngredient'], 'ingredients_amounts': ingredients_amounts}

def coerce_ingredients_amounts(ingredients_amounts):
    return [(drink[0], int(drink[1].strip(' oz'))) for drink in ingredients_amounts]
    