import pandas as pd

#Enumerate colors.
class COLOR:
	RED = "tomato"
	GREEN = "yellowgreen"
	BLUE = "lightblue"

NEWLINE_INDENT = "\n	"

def fill(color):
	return f"[style=filled fillcolor=\"{color}\"]"

def dual_label(weapon, n):
	return f"[label=\"{weapon}\" taillabel=\"{n}\"]"

def solo_node(player, color):
	return f"{NEWLINE_INDENT}\"{player}\" {fill(color)};"

def inter_node(actor, victim, weapon, n):
	return f"{NEWLINE_INDENT}\"{actor}\" -> \"{victim}\" {dual_label(weapon, n)};"

def digraphWrite(data, name):
	print("Writing digraph code...")
	with open(f"{name}.dot","w") as f:
		f.write("digraph {")

		# We're rounding all the values to the neaerest 100

		# We need to define the colours first for them to work
		for i in data.index:
			row = data.iloc[i]
			temp = ""

			if(row['Deed'] == "died"):
				if (row['Weapon'] == "Blue Zone"):
					temp = solo_node(row['Player'], COLOR.BLUE)
				else:
					temp = solo_node(row['Player'], COLOR.RED)
			elif(row['Deed'] == "won"):
				temp = solo_node(row['Player'], COLOR.GREEN)

			f.write(temp)

		# Then we can define the graph edges
		n = 0
		for i in data.index:
			row = data.iloc[i]

			if(row['Deed'] == "killed"):
				n += 1
				f.write(inter_node(row['Player'], row['Target'], row['Weapon'], n))

		f.write("\n}")

	print(f"Outputted graph script to {name}.dot...")


def main():
	data = pd.read_csv("battlegrounds.csv", low_memory=False)
	digraphWrite(data, "kill_map")	

# Load data
if __name__ == '__main__':
	main()
