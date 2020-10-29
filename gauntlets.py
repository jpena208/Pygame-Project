from armor import Armor
class Gauntlets(Armor):
	def __init__(name="NULL", description="NULL", itemType="NULL", armorValue=0, reach=0):
		super().__init__(name, description, itemType, armorValue)
		self.reach = reach

	def display(self):
		super().display()
		print("Reach       = ", self.reach)