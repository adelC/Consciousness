```
Initialization 
	HN = network.train()					##The Hpfield NT trained offline. 2 patterns (images) stored, fruit and cat
	SG = empty										## Init Symbolic knowledge graphs
	actions = [up, left, right] 	## List of snake actions

while True:
	
  Perception              ## Red or white pixel appears in front of the snake  
		If white pixel:
			input = upload image of a fruit ## using scikit-image
		Else if red pixel
			input = upload the image of the cat ## using scikit-image
	
	Memory
		retreived_pattern = HN(input)

	Belief
		retreived_variables = SG(retreived_pattern) # list of activated nodes
		If retreived_variables is empty
			SG.train()
			retrieved_variables = SG(retreived_pattern)
			action = get_action(retreived_variables)
		Else
			action = get_action(retreived_variables) 
snake_move(action)

```

