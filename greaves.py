from armor import Armor
class Greaves(Armor):
	def __init__(self, name="NULL", description="NULL", itemType="NULL", armorValue=0, stun=0):
		super().__init__(name, description, itemType, armorValue)
		self.stun = stun
	
	def display(self):
		super().display()
		print("Stun        = ", self.stun)