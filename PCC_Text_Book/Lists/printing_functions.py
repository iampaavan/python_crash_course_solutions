"""8-15: Printing Models"""
"""Put the functions for the example printing_models.py in a separate file called printing_functions.py.
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions."""

"""Functions related to printing 3d models."""


def print_models(unprinted_designs, completed_models):
	"""Simulate printing each design, until there are none left.
	Move each design to completed_models[] after printing."""
	while unprinted_designs:
		current_model = unprinted_designs.pop()
		
		# Simulate creating a 3d print from the design
		print(f"Printing model: {current_model}")
		completed_models.append(current_model)
		

def show_completed_models(completed_models):
	"""Show all the models that were printed"""
	print(f"The following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

