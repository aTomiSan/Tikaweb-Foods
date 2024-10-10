from flask import redirect, render_template, request, session
from app import ap
from users import create_new_user, check_user
from foods import add_food_func, list_foods, finish, hide_food, store_groceries, move_to_store, increase_amount, decrease_amount
from groceries import add_grocery_func, list_groceries, remove_grocery_func, increase_grocery, decrease_grocery, add_as_grocery, empty_shopping_list, decrease_type, increase_type
from recipes import add_recipe_func, list_recipes, get_recipe 
from expenses import list_expenses, add_to_expenses

@ap.route("/")
def index(): 
    return render_template("index.html")

@ap.route("/login", methods=["POST"]) 
def login(): 
    username = request.form["username"]
    password = request.form["password"]
    if check_user(username, password):
        session["username"] = username
        return redirect("/")
    else: 
        return redirect("/")
        # return render_template("index.html")

@ap.route("/new_user")
def new_user():
    return render_template("new_user.html")

@ap.route("/create_user", methods=["POST"])
def create_user(): 
    print("begin")
    username = request.form["username"]
    password = request.form["password"]
    print("requested")
    create_new_user(username, password) 
    return redirect("/")

@ap.route("/profile/<int:id>")
def profile(id):
    allow = False
    if is_admin():
        allow = True
    elif is_user() and user_id() == id:
        allow = True
    elif is_user():
        sql = "SELECT 1 FROM friends WHERE user1=:user1 AND user2=:user2"
        result = db.session.execute(sql, {"user1":user_id(), "user2":id})
        if result.fetchone():
            allow = True
    if not allow:
        return render_template("error.html", error="Ei oikeutta nähdä sivua")

@ap.route("/logout")
def logout():
    del session["username"]
    return redirect("/")



# FOODS 

@ap.route("/foods")
def foods(): 
    in_store, foodlist = list_foods()
    return render_template("foods.html", stored=in_store, allfoods=foodlist)

@ap.route("/new_food")
def new_food(): 
    return render_template("new_food.html")

@ap.route("/add_food", methods=["POST"])
def add_food(): 
    name = request.form["name"] 
    amount = request.form["amount"] 
    stored = request.form["stored"] 
    add_food_func(name, amount, stored)
    if request.form["add_grocery"] == "1":
        add_grocery_func(name, 1)
    return redirect("/foods")

@ap.route("/add_to_groceries")
def add_to_groceries(): 
    id = request.args["id"]
    add_as_grocery(id)
    return redirect("/foods")

@ap.route("/decrease_food")
def decrease_food(): 
    id = request.args["id"]
    decrease_amount(id)
    return redirect("/foods")

@ap.route("/increase_food")
def increase_food(): 
    id = request.args["id"]
    increase_amount(id)
    return redirect("/foods")

@ap.route("/finished")
def finished(): 
    id = request.args["id"]
    finish(id)
    return redirect("/foods")

@ap.route("/remove_food")
def remove_food(): 
    id = request.args["id"]
    hide_food(id)
    return redirect("/foods")

@ap.route("/add_to_store")
def add_to_store(): 
    id = request.args["id"]
    move_to_store(id)
    return redirect("/foods")


# GROCERIES 

@ap.route("/groceries")
def groceries(): 
    grocery_list = list_groceries() 
    return render_template("groceries.html", grocery_list=grocery_list)

@ap.route("/new_grocery")
def new_grocery():
    return render_template("new_grocery.html")

@ap.route("/add_grocery", methods=["POST"])
def add_grocery(): 
    name = request.form["name"]
    amount = request.form["amount"] 
    add_grocery_func(name, int(amount))
    return redirect("/groceries")

@ap.route("/remove_grocery", methods=["POST"])
def remove_grocery(): 
    id = request.form["id"]
    remove_grocery_func(id)
    return redirect("/groceries")

@ap.route("/increase", methods=["POST"])
def increase():
    id = request.form["id"]
    increase_grocery(id)
    return redirect("/groceries")

@ap.route("/decrease", methods=["POST"])
def decrease():
    id = request.form["id"]
    decrease_grocery(id)
    return redirect("/groceries")

@ap.route("/all_stored")
def all_stored(): 
    store_groceries()
    return redirect("/groceries")

@ap.route("/empty_groceries")
def empty_groceries(): 
    empty_shopping_list()
    return redirect("/groceries")

@ap.route("/before")
def before(): 
    id = request.args["id"]
    decrease_type(id) 
    return redirect("/groceries")

@ap.route("/after")
def after(): 
    id = request.args["id"]
    increase_type(id) 
    return redirect("/groceries")



# RECIPES 

@ap.route("/recipes")
def recipes(): 
    recipes = list_recipes()
    return render_template("recipes.html", recipes=recipes)

@ap.route("/new_recipe")
def new_recipe(): 
    return render_template("new_recipe.html", name="", ingredients="", additional="")

@ap.route("/add_recipe", methods=["POST"])
def add_recipe(): 
    name = request.form["recipe_name"]
    ingredients = request.form["ingredients"]
    print(ingredients)
    additional = request.form["additional"]
    add_recipe_func(name, ingredients, additional)
    ingredients = ingredients.split() 
    for i in ingredients:
        add_food_func(i, 1, 0)
    return redirect("/recipes")

@ap.route("/recipes/<int:id>")
def recipe(id): 
    name, ingredients, additional = get_recipe(id)
    return render_template("recipe.html", id=id, name=name, ingredients=ingredients, additional=additional)

@ap.route("/add_missing", methods=["POST"])
def add_missing():
    id = request.form["id"]
    name, ingredients, additional = get_recipe(id)
    for i in ingredients: 
        if i[1] == 0: 
            add_grocery_func(i[0], 1)
    return redirect("/recipes/" + str(id))


@ap.route("/add_all", methods=["POST"])
def add_all():
    id = request.form["id"]
    name, ingredients, additional = get_recipe(id)
    for i in ingredients: 
        add_grocery_func(i[0], 1)
    return redirect("/recipes/" + str(id))

@ap.route("/edit_recipe", methods=["POST"])
def edit_recipe():
    id = request.form["id"]
    name, ingredients, additional = get_recipe(id)
    ingredients_str = ""
    for x in ingredients: 
        ingredients_str += str(x[0]) + "\n"
    return render_template("new_recipe.html", name=name, ingredients=ingredients_str, additional=additional)


# EXPENSES 

@ap.route("/expenses")
def expenses():
    expense_list = list_expenses()
    return render_template("expenses.html", expense_list=expense_list)


@ap.route("/add_expense", methods=["POST"])
def add_expense():
    print("trying")
    value = request.form["value"]
    print(value)
    add_to_expenses(value)
    return redirect("/expenses")








