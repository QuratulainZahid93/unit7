#7.9
# sandwich_orders = ["pastrami", "club", "pastrami","chicken", "pastrami"]
# finished_orders = []
#
# while sandwich_orders:
#     if "pastrami" in sandwich_orders:
#         print("delhi is running out of pastarmi")
#         sandwich_orders.remove("pastrami")
#     else:
#         sandwich = sandwich_orders.pop()
#         print("i am making your " +sandwich)
#         finished_orders.append(sandwich)
#
# print(finished_orders)
# print(sandwich_orders)

####################################################################################

# orders = ["pastrami", "club", "pastrami","chicken", "pastrami"]
# orderss = [1, 2, 3, 4, 5]
# ordersss = ['beef', 'chicken', 'veg', 'egg']
# finished_orders = []
# def sandwich(sandwich_orders):
#     while sandwich_orders:
#         sandwichh = sandwich_orders.pop()
#         print("i am making your " +str(sandwichh))
#         finished_orders.append(sandwichh)
#
#
# sandwich(orders)
# print("\n")
# sandwich(ordersss)
# print("\n")
# sandwich(orderss)

##################################################################################

# def make_album(artist_name, album_title):
#     music_album = {}
#     """Return a full name, neatly formatted."""
#     music_album[artist_name] = alb_title
#     return music_album
#
#
#
# art_name = input("enter name of artist: ")
# alb_title = input("Enter name of album: ")
#
# album = make_album(art_name, alb_title)
# print(album)


##################################################################################

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
