"""
Sophia Babayev, Section 10
Builds a sandwich and tracks its type and unique condiments.
"""


bottom_slice = input().strip().lower()

if bottom_slice != "bottom slice":
	print("You just made a mess!")
else:
	ingredient = input().strip().lower()
	sandwich_type = ingredient
	type_count = 0
	condiments = []

	while ingredient != "top slice":
		if ingredient == sandwich_type:
			type_count += 1
		elif ingredient not in condiments:
			condiments.append(ingredient)
		ingredient = input().strip().lower()

	condiment_text = ", ".join(condiments) if condiments else "No condiments"
	print(
		f"You have created a {type_count}-{sandwich_type} sandwich "
		f"with the condiments: {condiment_text}"
	)

