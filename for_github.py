### Outside the While Loop

# Energy & Cost
initial_energy = 300


### Inside the While Loop

# Frame Cost
initial_energy -=5


#######################################################################################################################
# For autonomous snake. Change from button to snake move
if button_direction == 0:
    head_direction = 'left'
if button_direction == 1:
    head_direction = 'right'
if button_direction == 2:
    head_direction = 'down'
if button_direction == 3:
    head_direction = 'up'
if button_direction == 4:
    head_direction = 'up_right'
if button_direction == 5:
    head_direction = 'up_left'
if button_direction == 6:
    head_direction = 'down_right'
if button_direction == 7:
    head_direction = 'down_left'


# Change the head position based on the button direction
if key_pressed !=[]:
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10
    elif button_direction == 4:
        snake_head[0] += 10
        snake_head[1] -= 10
    elif button_direction == 5:
        snake_head[0] -= 10
        snake_head[1] -= 10
    elif button_direction == 6:
        snake_head[0] += 10
        snake_head[1] += 10
    elif button_direction == 7:
        snake_head[0] -= 10
        snake_head[1] += 10

#######################################################################################################################
# Snake Vision
vision_vector_list = []
longest_distance = 21

#Remove "key_pressed" when the agent moves on its own
if key_pressed != []:
    ### SEE Right
    if head_direction == 'right':
        #central line
        for i in range(1,longest_distance):
            update_x = i*10
            new_position = [snake_head[0]+update_x, snake_head[1]]
            vision_vector_list.append(new_position)
        #under central line
        for i in range(1,longest_distance):
            #adding 10 more rows
            update_y = i*10
            update_x = i * 10
            for x in range(1,longest_distance):
                if x>i:
                    update_xx = x*10
                    new_position = [snake_head[0]+update_xx, snake_head[1]+update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        # above central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    new_position = [snake_head[0] + update_xx, snake_head[1] - update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
    ### SEE Left
    if head_direction == 'left':
        #central line
        for i in range(1,longest_distance):
            update_x = i*10
            new_position = [snake_head[0]-update_x, snake_head[1]]
            vision_vector_list.append(new_position)
        #under central line
        for i in range(1,longest_distance):
            #adding 10 more rows
            update_y = i*10
            update_x = i * 10
            for x in range(1,longest_distance):
                if x>i:
                    update_xx = x*10
                    new_position = [snake_head[0]-update_xx, snake_head[1]+update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        # above central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    new_position = [snake_head[0] - update_xx, snake_head[1] - update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
    ### SEE Up
    if head_direction == 'up':
        #central line
        for i in range(1,longest_distance):
            update_y = i*10
            new_position = [snake_head[0], snake_head[1]-update_y]
            vision_vector_list.append(new_position)
        #on the left of central line
        for i in range(1,longest_distance):
            #adding 10 more rows
            update_y = i*10
            update_x = i * 10
            for x in range(1,longest_distance):
                if x>i:
                    update_xx = x*10
                    update_yy = x*10
                    new_position = [snake_head[0]-update_x, snake_head[1]-update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        #on the right of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] + update_x, snake_head[1] - update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
    ### SEE Down
    if head_direction == 'down':
        # central line
        for i in range(1, longest_distance):
            update_y = i * 10
            new_position = [snake_head[0], snake_head[1] + update_y]
            vision_vector_list.append(new_position)
        # on the left of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] + update_x, snake_head[1] + update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        # on the right of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] - update_x, snake_head[1] + update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)

    ### SEE Up Right
    if head_direction == 'up_right':
        # central line
        for i in range(1, longest_distance):
            update_y = i * 10
            update_x = i*10
            new_position = [snake_head[0]+update_x, snake_head[1] - update_y]
            vision_vector_list.append(new_position)
        # on the left of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] + update_x, snake_head[1] - update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        # # on the right of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] + update_xx, snake_head[1] - update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
    ### SEE Up Left
    if head_direction == 'up_left':
        # central line
        for i in range(1, longest_distance):
            update_y = i * 10
            update_x = i*10
            new_position = [snake_head[0]-update_x, snake_head[1] - update_y]
            vision_vector_list.append(new_position)
        # on the left of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] - update_xx, snake_head[1] - update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        # # # on the right of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] - update_x, snake_head[1] - update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
    ### SEE Down Right
    if head_direction == 'down_right':
        # central line
        for i in range(1, longest_distance):
            update_y = i * 10
            update_x = i*10
            new_position = [snake_head[0]+update_x, snake_head[1] + update_y]
            vision_vector_list.append(new_position)
        # on the left of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] + update_x, snake_head[1] + update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        # # # on the right of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] + update_xx, snake_head[1] + update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
    ### SEE Down Left
    if head_direction == 'down_left':
        # central line
        for i in range(1, longest_distance):
            update_y = i * 10
            update_x = i*10
            new_position = [snake_head[0]-update_x, snake_head[1] + update_y]
            vision_vector_list.append(new_position)
        # on the left of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] - update_xx, snake_head[1] + update_y]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
        # # # # on the right of central line
        for i in range(1, longest_distance):
            # adding 10 more rows
            update_y = i * 10
            update_x = i * 10
            for x in range(1, longest_distance):
                if x > i:
                    update_xx = x * 10
                    update_yy = x * 10
                    new_position = [snake_head[0] - update_x, snake_head[1] + update_yy]
                    if new_position not in vision_vector_list:
                        vision_vector_list.append(new_position)
# Display Vision
for x in vision_vector_list:
    for position in snake_vision:
        cv2.rectangle(img, (x[0], x[1]), (x[0], x[1]), (80, 80, 80), 3)

#######################################################################################################################
# Inside the --> if snake_head == apple_position:
initial_energy+=300

#######################################################################################################################
# Check for a collision with the border
    if snake_head[0] > 490:
        snake_head = [490, snake_head[1]]
    if snake_head[0] < 10:
        snake_head = [10, snake_head[1]]
    if snake_head[1] > 490:
        snake_head = [snake_head[0], 490]
    if snake_head[1] < 10:
        snake_head = [snake_head[0], 10]