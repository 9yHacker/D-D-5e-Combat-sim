import random, re

class Player:
	def __init__(self, hp):
		self.hp = hp;

	def initiative(self):
		return random.randint(1, 6) + 1

	def attack(self, victim):
		if not isinstance(victim, Player):
			raise Exception(f"{victim} is not a Player")
		else:
			victim.take_damage(self.cal_damage())
		
	
	def cal_damage(self):
		return 1

	def take_damage(self, damage):
		self.hp -= damage

class Battle:
	def __init__(self):
		self.initiative = {}
		self.order = []
		self.tracker = 0

	def add_unit(self, unit):
		init = unit.initiative()
		self.initiative[init] = unit
		self.order.insert(0, init)

	def add_unit_at_point(self, unit, point):
		self.initiative[point] = unit
		self.order.append(point)
		self.order.sort()
		self.order.reverse()
		
				
				

		
		





























'''
For calculating the optimal way to calculate damage for aoe abilities/spell, there can be two ways to do this.
Pick a target, then calculate all possible ways to target the surounding enemies (excluding all combinations where the targets are the same and where the combination is worse damage wise [could add this feature once I add "undesireable targets" a.k.a. sleeping enemies]) 
'''