class Items:
	# Constructor with default values
	def __init__(self, name="NULL", description="NULL", itemType="NULL"):
		self.name = name
		self.description = description
		self.itemType = itemType

	# Displays the name, description and type of an item
	def display(self):
		print("Name        = ", self.name)
		print("Type        = ", self.description)
		print("Description = ", self.itemType)