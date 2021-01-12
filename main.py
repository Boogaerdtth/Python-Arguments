# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name = 'You'):
	print(f"Hey {name}, what's up?") 

#greet('Bob')
#greet()

#2
def force(mass = 1, body = 'earth'):
	body = {'earth': 9.8, 'jupiter': 24.9, 'neptunes': 11.15, 'saturnus': 10.44, 'uranus': 8.87, \
	'venus': 8.87, 'mars': 3.71, 'mercurius': 3.7, 'pluto': 0.58 }
	planet_input = input("What kind of planet? ")
	mass = input("What is the weight you want to drop? ")
	print(float(mass) * body[planet_input])
#force()

#3
def pull(m1, m2, d):
	G = 6.674 * 10**-11
	print(G * ((m1 * m2) / d**2))

pull(800, 1500, 3)
