from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import collections

options = Options()
options.headless = True
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1200")

driver=webdriver.Chrome(options=options)

def parse_recipe_json(meta):
    file = open( "recipes/" + meta["name"] + ".md", mode='w', encoding='utf-8')
    file.write("# " + meta["name"])
    file.write("\n")

    if "description" in meta:
        file.write("##### " + meta["description"])
        file.write("\n")

    if "image" in meta:
        img_data = meta["image"]
        if type(img_data) is list:
            if type(img_data[0]) is str:
                file.write("![main](" + img_data[0] + ")")
            else:
                file.write("![main](" + img_data[0]['url'] + ")")
        elif type(img_data) is dict:
            file.write("![main](" + img_data['url'] + ")")

    file.write("\n# Ingredients:\n")
    for ing in meta["recipeIngredient"]:
        file.write(ing)
        file.write("\n\n")

    file.write("\n# Steps:\n")
    for step in meta["recipeInstructions"]:
        if 'text' in step:
            file.write("- " + step['text'])
            file.write("\n\n")
        elif 'name' in step:
            file.write("#### " + step['name'] + ":")
            file.write("\n\n")
            for stepp in step["itemListElement"]:
                file.write("- " + stepp['text'])
                file.write("\n\n")
    file.close()

def scrap_recipe(url):
    driver.get(url)

    eles = driver.find_elements(By.TAG_NAME, 'script')
    for e in eles:
        tex = e.get_attribute('innerText')

        if "\"recipeIngredient\"" in tex:
            meta = json.loads(tex)
            if type(meta) is dict:
                if "@type" in meta and meta["@type"] == "Recipe":
                    parse_recipe_json(meta)
                    return
                for key in meta["@graph"]:
                    if key["@type"] == 'Recipe':
                        parse_recipe_json(key)
            else:
                parse_recipe_json(meta[0])



# urls = ["https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/","https://www.allrecipes.com/recipe/17481/simple-white-cake/", "https://sallysbakingaddiction.com/homemade-pizza-crust-recipe/"]
urls = ["https://kidtestedrecipes.com/easy-chipotle-chicken-wrap/?utm_source=pinterest&utm_medium=social&utm_campaign=grow-social-pro","https://natashaskitchen.com/creamy-cajun-chicken-pasta/","https://maesmenu.com/recipes/chicken-miso-soup/","https://www.cook2eatwell.com/chicken-satay-with-peanut-sauce/","https://www.saltandlavender.com/creamy-mushroom-chicken/"]


for u in urls:
    try:
        scrap_recipe(u)
    except:
        print(u + " failed")