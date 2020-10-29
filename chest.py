from armor import Armor
class Chest(Armor):
	# Constructor with default values for chest armor runs constructor from armor
	def __init__(self, name="NULL", description="NULL", itemType="NULL", armorValue=0, defense=0, defChance=0):
		super().__init__(name, description, itemType, armorValue)
		self.defense = defense				# Number that damage is reduced
		self.defChance = defChance		# Percent chance that defense activates

	def display(self):
		super().display()
		print("Defense     = ", self.defense)
		print("Def Chance  = ", self.defChance)