from flask import Flask, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__, static_folder="static", static_url_path="/static")

RECIPES = {
    "breakfast": {
        "meal": "Avocado Toast with Poached Eggs 🥑🍳",
        "time_range": "6 AM – 11 AM",
        "ingredients": [
            "2 slices sourdough bread",
            "1 ripe avocado",
            "2 eggs",
            "Salt, pepper, chili flakes",
            "Lemon juice"
        ],
        "steps": [
            "Toast the sourdough bread until golden.",
            "Mash avocado with lemon juice, salt & pepper.",
            "Poach eggs in simmering water for 3 minutes.",
            "Spread avocado on toast, top with poached eggs.",
            "Sprinkle chili flakes and serve immediately!"
        ],
        "fun_fact": "Avocados are technically a fruit, and they ripen faster next to bananas! 🍌",
        "emoji": "🌅"
    },
    "brunch": {
        "meal": "Fluffy Banana Pancakes 🥞🍌",
        "time_range": "11 AM – 1 PM",
        "ingredients": [
            "2 ripe bananas",
            "2 eggs",
            "1 cup flour",
            "1 cup milk",
            "1 tsp baking powder",
            "Butter & maple syrup"
        ],
        "steps": [
            "Mash bananas in a bowl until smooth.",
            "Mix in eggs, milk, flour, and baking powder.",
            "Heat a buttered pan over medium heat.",
            "Pour batter and cook until bubbles form, then flip.",
            "Stack high and drizzle with maple syrup!"
        ],
        "fun_fact": "Pancakes have been around since ancient Greece — they called them 'tagenites'! 🏛️",
        "emoji": "☀️"
    },
    "lunch": {
        "meal": "Grilled Chicken Caesar Wrap 🌯🥗",
        "time_range": "1 PM – 4 PM",
        "ingredients": [
            "1 grilled chicken breast",
            "Large flour tortilla",
            "Romaine lettuce",
            "Caesar dressing",
            "Parmesan cheese",
            "Croutons"
        ],
        "steps": [
            "Slice grilled chicken into strips.",
            "Toss lettuce with Caesar dressing.",
            "Lay tortilla flat and add lettuce mix.",
            "Add chicken, parmesan, and croutons.",
            "Roll tightly, slice diagonally, and enjoy!"
        ],
        "fun_fact": "The Caesar salad was invented in Tijuana, Mexico in 1924 — not Italy! 🇲🇽",
        "emoji": "🌞"
    },
    "snack": {
        "meal": "Honey Garlic Popcorn 🍿🍯",
        "time_range": "4 PM – 7 PM",
        "ingredients": [
            "½ cup popcorn kernels",
            "2 tbsp butter",
            "2 tbsp honey",
            "1 clove garlic (minced)",
            "Pinch of salt"
        ],
        "steps": [
            "Pop popcorn kernels in a large pot with a lid.",
            "Melt butter in a small pan over low heat.",
            "Add garlic and cook for 1 minute.",
            "Stir in honey and a pinch of salt.",
            "Drizzle over popcorn, toss well, and snack away!"
        ],
        "fun_fact": "Americans eat about 17 billion quarts of popcorn every year! 🎉",
        "emoji": "🌆"
    },
    "dinner": {
        "meal": "Creamy Tuscan Garlic Pasta 🍝🧄",
        "time_range": "7 PM – 10 PM",
        "ingredients": [
            "300g fettuccine pasta",
            "3 cloves garlic",
            "1 cup heavy cream",
            "½ cup sun-dried tomatoes",
            "2 cups spinach",
            "Parmesan cheese",
            "Olive oil, salt, pepper"
        ],
        "steps": [
            "Cook pasta according to package instructions.",
            "Sauté garlic in olive oil for 2 minutes.",
            "Add sun-dried tomatoes and cook 1 minute.",
            "Pour in cream and simmer until slightly thickened.",
            "Add spinach and cooked pasta, toss well.",
            "Top with parmesan and serve hot!"
        ],
        "fun_fact": "Italy has over 350 different pasta shapes — each designed for a specific sauce! 🇮🇹",
        "emoji": "🌙"
    },
    "midnight": {
        "meal": "Midnight Nutella Mug Cake 🍫☕",
        "time_range": "10 PM – 6 AM",
        "ingredients": [
            "4 tbsp flour",
            "4 tbsp sugar",
            "2 tbsp cocoa powder",
            "1 egg",
            "3 tbsp milk",
            "3 tbsp oil",
            "2 tbsp Nutella"
        ],
        "steps": [
            "Mix all dry ingredients in a large mug.",
            "Add egg, milk, and oil — stir until smooth.",
            "Drop a spoonful of Nutella in the center.",
            "Microwave on high for 90 seconds.",
            "Let cool for 1 minute and dig in — no judgment! 😄"
        ],
        "fun_fact": "Nutella was invented in Italy in the 1940s as a way to stretch chocolate during cocoa shortages! 🍫",
        "emoji": "🌃"
    }
}

def get_meal_time():
    hour = datetime.now().hour
    if 6 <= hour < 11:
        return "breakfast"
    elif 11 <= hour < 13:
        return "brunch"
    elif 13 <= hour < 16:
        return "lunch"
    elif 16 <= hour < 19:
        return "snack"
    elif 19 <= hour < 22:
        return "dinner"
    else:
        return "midnight"

# ✅ Serve index.html from static folder
@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/api/recipe")
def get_recipe():
    meal_time = get_meal_time()
    recipe = RECIPES[meal_time]
    return jsonify({
        "meal_time": meal_time,
        "current_hour": datetime.now().hour,
        "recipe": recipe
    })

@app.route("/api/recipe/<meal_time>")
def get_recipe_by_time(meal_time):
    if meal_time not in RECIPES:
        return jsonify({"error": "Invalid meal time"}), 404
    return jsonify({
        "meal_time": meal_time,
        "recipe": RECIPES[meal_time]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
