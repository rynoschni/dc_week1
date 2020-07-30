meal = {
    "drink": "Beer",
    "appetizer": "chips & salsa",
    "entree": "fajita's",
  #  "dessert": "churros"
}

#print(meal["drink"])
#print("This Thursday, I will have a %s and %s for dinner!") % (meal("drink"), meal("entree"))

# if "dessert" in meal:
#     print("Of course, Ryan had a dessert!! He ate %s" % (meal("dessert")))
# else:
#     print("Ryan did not have dessert, and was sad!")

if "dessert" in meal:
    print("Of course, Ryan had a dessert!! He ate %s" % (meal("dessert")))
else:
    meal["dessert"] = "churros"
    print(meal)
    
if 'dessert' in meal:
    meal["dessert"] = 
