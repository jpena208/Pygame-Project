from items import Items
class Weapons(Items):
	# Constructor with default values for weapons runs constructor for items
	def __init__(self, name="NULL", description="NULL", itemType="NULL", dmg=0, spd=0, firstStrike=0):
		super().__init__(name, description, itemType)
		self.dmg = dmg										# Damage of weapons
		self.spd = spd										# Speed of weapons
		self.firstStrike = firstStrike		# Percent chance to gain first strike

	def display(self):
		super().display()
		print("Damage      = ", self.dmg)
		print("Speed       = ", self.spd)
		print("First Strike= ", self.firstStrike)