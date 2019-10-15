# Python Crash Course
#
# Chapter 8 Functions, p. 148 - 150

# lists and dictionaries can also be passed to functions, note
# that the function can modify them directly
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design from the uncompleted queue to the
    completed queue.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate printing
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# if in this instance we did not want unprinted_designs to be modified by the
# function, we would need to pass a copy (slice) as such
# print_models(unprinted_designs[:], completed_models)