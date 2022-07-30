import requests

url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
food_item = input("Enter a food: ")
querystring = {"query":f"{food_item}"}

headers1 = headers = {
    "X-RapidAPI-Key": "YOUR-API-KEY",
    "X-RapidAPI-Host": "calorieninjas.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers1, params=querystring)

print(response.text)
print()

datafood = response.json()
try:
    name = datafood['items'][0]['name']
    servingsize = datafood['items'][0]['serving_size_g']
    sugar = datafood['items'][0]['sugar_g']
    fiber = datafood['items'][0]['fiber_g']
    sodium = datafood['items'][0]['sodium_mg']
    potassium = datafood['items'][0]['potassium_mg']
    saturated_fat = datafood['items'][0]['fat_saturated_g']
    total_fat = datafood['items'][0]['fat_total_g']
    calories = datafood['items'][0]['calories']
    cholesterol = datafood['items'][0]['cholesterol_mg']
    protein = datafood['items'][0]['protein_g']
    carbohydrates = datafood['items'][0]['carbohydrates_total_g']

    print("Food item:", name)
    print("Sugar:", sugar)
    print("Serving Size:", servingsize)
    print("Fiber:", fiber)
    print("Sodium:", sodium)
    print("Potassium:", potassium)
    print("Saturated fat:", saturated_fat)
    print("Total fat:", total_fat)
    print("Calories:", calories)
    print("Cholesterol:", cholesterol)
    print("Protein:", protein)
    print("Carbohydrates:", carbohydrates)

except IndexError:
    print(f"No food item called {food_item}.")