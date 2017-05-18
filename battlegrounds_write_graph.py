import pandas as pd

def digraphWrite(data, name):
	print "Writing digraph code..."
	file = open(name+".dot","w")
	file.write("digraph {")

	# We're rounding all the values to the neaerest 100

	# We need to define the colours first for them to work
	for i in data.index:
		row = data.iloc[i]
		temp = ""


		if(row['Deed'] == "died"):
			temp = "\n	\""+row['Player']+"\" [style=filled fillcolor=\"tomato\"];"
		elif(row['Deed'] == "won"):
			temp = "\n	\""+row['Player']+"\" [style=filled fillcolor=\"yellowgreen\"];"

		file.write(temp)

	# Then we can define the graph edges
	for i in data.index:
		row = data.iloc[i]
		temp = ""

		if(row['Deed'] == "killed"):
			temp = "\n	\""+row['Player']+"\" -> \""+row['Target']+"\" [label=\""+row['Weapon']+"\"];"

		file.write(temp)

	file.write("\n}")
	file.close()
	print "Outputted graph script to "+name+".dot..."

# Load data
data = pd.read_csv("battlegrounds.csv", low_memory=False)
digraphWrite(data, "kill_map")