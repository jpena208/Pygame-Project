from armor import Armor
class Helmet(Armor):
	def __init__(self, name="NULL", description="NULL", itemType="NULL", armorValue=0, critChance=0, critical=1.5):
		super().__init__(name, description, itemType, armorValue)
		self.critChance = critChance
		self.critical = 1.5
	
	def display(self):
		super().display()
		print("Critical    = ", self.critical)
		print("Crit Chance = ", self.critChance)