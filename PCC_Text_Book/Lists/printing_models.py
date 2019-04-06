from Lists import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
print(f'**********************************************************')
pf.show_completed_models(completed_models)
print(f'**********************************************************')
