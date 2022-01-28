import numpy as np
import cv2
import random
import time

def collision_with_apple(apple_position, score):
    apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
    score += 1
    return apple_position, score

def collision_with_boundaries(snake_head):
    if snake_head[0]>=500 or snake_head[0]<0 or snake_head[1]>=500 or snake_head[1]<0 :
        return 1
    else:
        return 0

def collision_with_self(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0

# def sight_vector():


img = np.zeros((500,500,3),dtype='uint8')
# Initial Snake and Apple position
snake_position = [[250,250],[240,250],[230,250]]
snake_vision = [[260,250]]
apple_position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
obstacle_pink = [[150, 200],[160, 200],[170, 200],[180, 200],[190, 200],[200, 200]]
apple = cv2.imread('apple_image.jpg')

score = 0
prev_button_direction = 1
button_direction = 1
snake_head = [250,250]

# Energy & Cost
initial_energy = 300
frame_cost = 0


key_pressed = []

while True:

    initial_energy -=5

    if key_pressed !=[]:
        key_pressed.clear()

    cv2.imshow('a', img)
    cv2.waitKey(1)
    img = np.zeros((500, 500, 3), dtype='uint8')

    # Display Apple
    cv2.rectangle(img, (apple_position[0], apple_position[1]), (apple_position[0] + 10, apple_position[1] + 10),
                  (0, 0, 255), 3)

    # Display Snake
    for position in snake_position:
        cv2.rectangle(img, (position[0], position[1]), (position[0] + 10, position[1] + 10), (0, 255, 0), 3)

    # Takes step after fixed time
    t_end = time.time() + 0.2
    k = -1
    while time.time() < t_end:
        if k == -1:
            k = cv2.waitKey(125)
        else:
            continue

    # 0-Left, 1-Right, 3-Up, 2-Down, 4-Up_Right, 5-Up_Left, 6-Down_Right, 7-Down-Left, q-Break
    # a-Left, d-Right, w-Up, s-Down, e-Up_Right, q-Up_Left, x-Down_Right, z-Down_Left

    if k == ord('a') and prev_button_direction != 1:
        button_direction = 0
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('d') and prev_button_direction != 0:
        button_direction = 1
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('w') and prev_button_direction != 2:
        button_direction = 3
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('s') and prev_button_direction != 3:
        button_direction = 2
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('e') and prev_button_direction != 7:
        button_direction = 4
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('q') and prev_button_direction != 6:
        button_direction = 5
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('x') and prev_button_direction != 5:
        button_direction = 6
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('z') and prev_button_direction != 4:
        button_direction = 7
        key_pressed.clear()
        key_pressed.append('Yes')
    elif k == ord('c'):
        break
    else:
        button_direction = button_direction
    prev_button_direction = button_direction

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

    print(vision_vector_list)

    # Increase Snake length on eating apple
    if snake_head == apple_position:
        initial_energy+=300
        apple_position, score = collision_with_apple(apple_position, score)
        snake_position.insert(0, list(snake_head))

    else:
        snake_position.insert(0, list(snake_head))
        snake_position.pop()

    print('Snake -->',head_direction)
    print('Snake ',snake_head)

    # Check for a collision with the border
    if snake_head[0] > 490:
        snake_head = [490, snake_head[1]]
    if snake_head[0] < 10:
        snake_head = [10, snake_head[1]]
    if snake_head[1] > 490:
        snake_head = [snake_head[0], 490]
    if snake_head[1] < 10:
        snake_head = [snake_head[0], 10]

    print('Energy --> ',initial_energy)


    # # On collision kill the snake and print the score
    # if collision_with_boundaries(snake_head) == 1 or collision_with_self(snake_position) == 1:
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     img = np.zeros((500, 500, 3), dtype='uint8')
    #     cv2.putText(img, 'Your Score is {}'.format(score), (140, 250), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    #     cv2.imshow('a', img)
    #     cv2.waitKey(0)
    #     cv2.imwrite('D:/downloads/ii.jpg', img)
    #     break

cv2.destroyAllWindows()
