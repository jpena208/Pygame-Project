from items import Items
class Armor(Items):
	# Constructor with default values for armor runs constructor for items
	def __init__(self, name="NULL", description="NULL", itemType="NULL", armorValue = 0):
		super().__init__(name, description, itemType)
		self.armorValue = armorValue		# Hit Points for armor
	
	# Display for armor
	def display(self):
		super().display()
		print("Armor Value = ", self.armorValue)