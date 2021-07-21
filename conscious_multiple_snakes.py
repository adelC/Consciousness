import turtle
import time
import random
import pickle
import signal

import datetime
from itertools import combinations


the_list = [0 ,
10 ,
20 ,
30 ,
40 ,
50 ,
60 ,
70 ,
80 ,
90 ,
100 ,
110 ,
120 ,
130 ,
140 ,
150 ,
160 ,
170 ,
180 ,
190 ,
200 ,
210 ,
220 ,
230 ,
240 ,
250 ,
260 ,
270 ,
280 ,
290,
-10 ,
-20 ,
-30 ,
-40 ,
-50 ,
-60 ,
-70 ,
-80 ,
-90 ,
-100 ,
-110 ,
-120 ,
-130 ,
-140 ,
-150 ,
-160 ,
-170 ,
-180 ,
-190 ,
-200 ,
-210 ,
-220 ,
-230 ,
-240 ,
-250 ,
-260 ,
-270 ,
-280 ,
-290]

the_list2 = [0 ,
10 ,
20 ,
30 ,
40 ,
50 ,
60 ,
70 ,
80 ,
90 ,
100 ,
110 ,
120 ,
130 ,
140 ,
150 ,

-10 ,
-20 ,
-30 ,
-40 ,
-50 ,
-60 ,
-70 ,
-80 ,
-90 ,
-100 ,
-110 ,
-120 ,
-130 ,
-140 ,
-150 ,
]

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game for Consciousness")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
# pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# last day 25
day = 1
days_passed = []
# Main game loop
frames_per_day = 200
first_frame = 0
initial_energy = 150

### Initial Costs ###
timestamp_cost = 0
sight_neuron_cost = 0

pickle_sight = open("memory/sight_vectors.pickle","rb")
sight_dict = pickle.load(pickle_sight)
pickle_direction = open("memory/direction_vectors.pickle","rb")
direction_dict = pickle.load(pickle_direction)
pickle_constrained = open("memory/individual_neurons/constrained_vectors.pickle","rb")
constrained_dict = pickle.load(pickle_constrained)
day_constrained_dict = {}

# sight_dict = {first_frame:'name'}
bites = []
food_energy = []
# food_model_list = []
DRAFT_MODEL = [['D|up', 'A|up', 6], ['D|down', 'A|down', 5], ['D|left', 'A|left', 4], ['A|left', 'D|left', 2], ['A|up', 'D|up', 2], [(0, 100), (-20, 90), 1], [(250, 100), (230, 90), 1], [(250, 180), 'A|up', 1], ['A|down', (-90, -210), 1], [(250, -90), (270, -90), 1], ['D|up', (-130, 110), 1], [(60, 220), 'D|right', 1], ['A|down', (10, 20), 1], ['A|right', 'D|right', 1], ['D|down', (210, -140), 1], [(190, 180), (190, 200), 1], ['A|down', 'D|down', 1], ['D|right', (-160, -20), 1], [(-100, -80), (-100, -100), 1], [(210, -160), 'A|right', 1], ['D|down', (-230, -150), 1], [(-130, 170), 'D|up', 1], ['D|left', (-150, -80), 1], ['A|right', (210, -270), 1], ['D|right', (-70, 110), 1], ['D|right', (20, -280), 1], [(-50, -10), (-50, 10), 1], [(-210, 20), 'A|up', 1], [(110, 260), (130, 260), 1], [(170, -260), 'D|down', 1], [(-210, 190), 'D|up', 1], [(-130, -170), 'D|down', 1], [(-290, -160), 'D|up', 1], [(140, 80), (160, 80), 1], [(250, 80), 'D|right', 1], [(-190, 240), 'A|down', 1], [(-90, -230), (-90, -210), 1], ['A|down', (-40, -110), 1], [(-10, 210), 'A|left', 1], [(180, -130), (180, -150), 1], [(210, -100), 'A|right', 1], [(170, -100), 'D|down', 1], ['A|down', (-160, 90), 1], [(-210, -130), 'D|down', 1], [(200, -270), 'D|right', 1], ['D|up', (-260, 40), 1], ['A|down', (-80, -80), 1], ['A|right', (-110, -240), 1], ['A|up', (-60, 260), 1], [(-50, -260), (-70, -260), 1], [(240, 220), 'A|up', 1], [(-190, 100), (-170, 90), 1], ['D|up', (0, 20), 1], ['D|up', (0, 30), 1], ['A|up', (-260, -70), 1], ['D|right', (-160, 30), 1], [(-20, 50), 'A|right', 1], [(-40, 100), (-20, 110), 1], ['D|up', (-230, 160), 1], ['A|down', (290, 0), 1], [(230, 200), 'A|up', 1], [(-270, -60), 'A|left', 1], [(-20, 110), 'D|up', 1], [(-260, -50), 'A|down', 1], [(-10, 210), 'A|up', 1], [(200, 240), 'D|right', 1], [(200, -30), (190, -50), 1]]

pickle_food_attention = open("memory/attention_models/food_attention.pickle", "rb")
food_model_list = pickle.load(pickle_food_attention)
pickle_body_attention = open("memory/attention_models/body_attention.pickle", "rb")
body_attention_list = pickle.load(pickle_body_attention)
self_centered = ['False']

while True:



    found_food=[]
    sight_neuron_cost+=1
    timestamp_cost+=1

    energy_cost=sight_neuron_cost+timestamp_cost

    wn.update()

    ##### Random Reflex ####
    # myList = [go_up, go_down, go_left, go_right]
    # the_choice = random.choice(myList)
    # def runn():
    #     the_choice()
    #
    # runn()

    first_frame+=1
    if first_frame == 201:
        day+=1
        first_frame = 1

    # print(day, first_frame)
    current_energy = initial_energy - energy_cost

    foodx = food.xcor()
    foody = food.ycor()

    x = head.xcor()
    y = head.ycor()
    # print((foodx, foody))
    # print((x, y))
    # print(head.direction)
    x_difference = x - foodx
    y_difference = y - foody
    # print(x_difference)
    # print(y_difference)
    head_position = (x, y)

    foodx_minus = foodx - 30
    foodx_plus = foodx + 30
    foody_plus = foody + 30
    foody_minus = foody - 30

    ###### Sight On The Left ###########
    if x == foodx:
        if head.direction == 'left' and x-10 > foodx:
            if found_food==[]:
                found_food.append('left')
            # print('I can see it on my LEFT!')
    if y == foody:
        if head.direction == 'left' and x-10 > foodx:
            if found_food == []:
                found_food.append('left')
            # print('I can see it on my LEFT!')
    if head.direction == 'left' and x - 10 > foodx:
        if y in range(foody_minus, foody):
            if found_food == []:
                found_food.append('left')
            # print('I can see it on my LEFT!')
        if y in range(foody, foody_plus):
            if found_food == []:
                found_food.append('left')
            # print('I can see it on my LEFT!')

    ###### Sight On The Right ###########
    if x == foodx:
        if head.direction == 'right' and x+10 < foodx:
            if found_food == []:
                found_food.append('right')
            # print('I can see it on my RIGHT!')
    if y == foody:
        if head.direction == 'right' and x+10 < foodx:
            if found_food == []:
                found_food.append('right')
            # print('I can see it on my RIGHT!')
    if head.direction == 'right' and x+10 < foodx:
        if y in range(foody_minus, foody):
            if found_food == []:
                found_food.append('right')
            # print('I can see it on my RIGHT!')
        if y in range(foody, foody_plus):
            if found_food == []:
                found_food.append('right')
            # print('I can see it on my RIGHT!')

    ###### Sight Above ########
    if x == foodx:
        if head.direction == 'up' and y+10 < foody:
            if found_food == []:
                found_food.append('up')
            # print('I can see it UP THERE!')
    if y == foody:
        if head.direction == 'up' and y+10 < foody:
            if found_food == []:
                found_food.append('up')
            # print('I can see it UP THERE!')
    if head.direction == 'up' and y+10 < foody:
        if x in range(foodx_minus, foodx):
            if found_food == []:
                found_food.append('up')
            # print('I can see it UP THERE!')
        if x in range(foodx, foodx_plus):
            if found_food == []:
                found_food.append('up')
            # print('I can see it UP THERE!')

    ###### Sight Below ########
    if x == foodx:
        if head.direction == 'down' and y-10 > foody:
            if found_food == []:
                found_food.append('down')
            # print('I can see it DOWN THERE!')
    if y == foody:
        if head.direction == 'down' and y-10 > foody:
            if found_food == []:
                found_food.append('down')
            # print('I can see it DOWN THERE!')
    if head.direction == 'down' and y-10 > foody:
        if x in range(foodx_minus, foodx):
            if found_food == []:
                found_food.append('down')
            # print('I can see it DOWN THERE!')
        if x in range(foodx, foodx_plus):
            if found_food == []:
                found_food.append('down')
            # print('I can see it DOWN THERE!')



    # Check for a collision with the border
    if head.xcor() > 289 or head.xcor() < -289 or head.ycor() > 289 or head.ycor() < -289:
        head.goto(0,0)
        # print(food_model_list)
        # time.sleep(1)
        # head.goto(0, 0)
        # head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        myList = [go_up, go_down, go_left, go_right]
        the_choice = random.choice(myList)
        the_choice()


        # Clear the segments list
        # segments.clear()

        #
        # # Reset the score
        # score = 0
        #
        # # Reset the delay
        # delay = 0.1
        #
        # pen.clear()
        # pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for a collision with the food
    if head.distance(food) < 30:
        food_energy.append(150)
        # Move the food to a random spot
        # x = random.randint(-290, 290)
        # y = random.randint(-290, 290)

        xx = random.choice(the_list2)
        yy = random.choice(the_list2)
        food.goto(xx, yy)

        # Add a segment
        if sum(bites) < 11:
            new_bite =1
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            segments.append(new_segment)
            bites.append(new_bite)

        # Shorten the delay
        # delay -= 0.001
        #
        # # Increase the score
        # score += 10
        #
        # if score > high_score:
        #     high_score = score
        #
        # pen.clear()
        # pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments

    # for segment in segments:
    #     if segment.distance(head) < 10:
    #
    #         time.sleep(1)
    #         head.goto(0, 0)
    #         head.direction = "stop"
    #
    #         # Hide the segments
    #         for segment in segments:
    #             segment.goto(1000, 1000)
    #
    #         # Clear the segments list
    #         segments.clear()


            # # Reset the score
            # score = 0
            #
            # # Reset the delay
            # delay = 0.1
            #
            # # Update the score display
            # pen.clear()
            # pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
            #           font=("Courier", 24, "normal"))

    # print('Energy-->',current_energy+sum(food_energy))

    ##### This is for saving the memory Dr Bach! ###
    ###### Vectors Of Sight ######
    for dafood in found_food:
        sight_neuron = [dafood, (foodx, foody), (current_energy+sum(food_energy)), first_frame,day]
        sight_dict[head_position].update({
            day:sight_neuron
        })
        try:
            sight_dict[first_frame].pop('name')
        except KeyError:
            pass
        # print('Sight -->', sight_neuron)
        # print('dafood:', dafood, 'foodx,foody:', (foodx, foody), 'head.direction:', head.direction,
        #       'energy:', (current_energy + sum(food_energy)), 'frame:', first_frame, 'day:', day)

    if not found_food:
        dafood = 'nofood'
        sight_neuron = [dafood, dafood, (current_energy+sum(food_energy)), first_frame,day]
        sight_dict[head_position].update({day:sight_neuron})
        try:
            sight_dict[first_frame].pop('name')
        except KeyError:
            pass
        # print('Sight -->', sight_neuron)

    ###### Vectors Of Direction ######
        direction_neuron = [(head.direction), (current_energy+sum(food_energy)), first_frame,day]
        direction_dict[head_position].update({day: direction_neuron})
        try:
            direction_dict[head_position].pop('name')
        except KeyError:
            pass
        # print('Direction -->', direction_neuron)

    dafood = 'A|'+str(dafood)
    head_direction = 'D|'+str(head.direction)
    snake_head = 'snake_head'
    snake_body = 'snake_body'
    snake_legs = 'snake_legs'
    the_neurons = [dafood, (foodx, foody),head_position, head_direction]
    the_neurons_full = [dafood, (foodx, foody),head_position, head_direction, snake_head, snake_body]
    # the_choice = random.choice(the_neurons)
    # the_neurons.remove(the_choice)
    # the_choice2 = random.choice(the_neurons)
    # # the_neurons.remove(the_choice2)
    # # the_choice3 = random.choice(the_neurons)
    #
    # all_energy = current_energy+sum(food_energy)
    # print('Energy ==> ', all_energy)
    #
    # #### ATTENTION GUIDANCE for Body and Food ####
    #
    # the_list_comparison = {}
    # for i, x in enumerate(DRAFT_MODEL):
    #     sett1 = x
    #     sett1 = [x for x in sett1 if not isinstance(x, int)]
    #     sett2 = the_neurons_full
    #     sett2 = [x for x in sett2 if not isinstance(x, int)]
    #     sett1 = set(sett1)
    #     sett2 = set(sett2)
    #     # print(sett1,sett2)
    #     is_subset = sett1.issubset(sett2)
    #     if is_subset == True:
    #         the_list_comparison.update({x[2]: x})
    # dictionary_items = the_list_comparison.items()
    # sorted_items = sorted(dictionary_items)
    # decided = 'no'
    # try:
    #     new_list = sorted_items[0]
    #     print(new_list)
    #     if decided == 'no':
    #         if 'D|up' in new_list:
    #             decided = 'yes'
    #             go_up()
    #             print('Going Up')
    #     if decided == 'no':
    #         if 'D|down' in new_list:
    #             decided = 'yes'
    #             go_down()
    #             print('Going Down')
    #     if decided == 'no':
    #         if 'D|left' in new_list:
    #             decided = 'yes'
    #             go_left()
    #             print('Going Left')
    #     if decided == 'no':
    #         if 'D|right' in new_list:
    #             decided = 'yes'
    #             go_right()
    #             print('Going Right')
    # except IndexError:
    #     myList = [go_up, go_down, go_left, go_right]
    #     the_choice = random.choice(myList)
    #     the_choice()

######################################################################################################
#################### NEW CODE ########################################################################

    it_found_list = []
    it_did_NOT_find_list = []

    def combinationsList(thelist, r):
        current_energy = initial_energy - energy_cost
        final_list = []
        similar_list = []
        the_list = list(combinations(thelist, r))
        # print(the_list)
        for x in the_list:
            # print(x)
            final_list.append(list(x))
            for xx in food_model_list:
                if xx[:-1] == list(x):
                    similar_list.append(xx)
        new_list_order = sorted(similar_list, key=lambda e: e[2], reverse=True)
        if new_list_order ==[]:
            # print('It is empty!')
            new_list_order = [['A|nofood', (0, 100), 0], ['A|nofood', (0, 0), 0], ['A|nofood', 'D|stop', 0], [(0, 100), (0, 0), 0], [(0, 100), 'D|stop', 0], [(0, 0), 'D|stop', 0]]
        # print(new_list_order)
        if new_list_order[0][2] != 0:
            print('I found a relevant!')
            constrained_neurons_non_alphabetical = new_list_order[0][:-1]
            it_found_list.append(constrained_neurons_non_alphabetical)
            # extra_data = [(current_energy + sum(food_energy)), first_frame, day]
            # constrained_neurons = constrained_neurons_non_alphabetical + extra_data
            decided = 'no'
            # print('YES')
            the_choicee = []
            if 'D|up' in new_list_order[0]:
                decided = 'yes'
                # print('going up!')
                go_up()
                the_choicee.append('going up!')
            if 'D|down' in new_list_order[0]:
                decided = 'yes'
                # print('going down!')
                go_down()
                the_choicee.append('going down!')
            if 'D|left' in new_list_order[0]:
                decided = 'yes'
                # print('going left!')
                go_left()
                the_choicee.append('going left!')
            if 'D|right' in new_list_order[0]:
                decided = 'yes'
                # print('going right!')
                go_right()
                the_choicee.append('going right!')
            # if decided == 'yes':
            #     try:
            #         for k, v in day_constrained_dict[day].items():
            #             the_dayy = 'Just for the try except'
            #             # print(day, k)
            #     except KeyError:
            #         day_constrained_dict.update({
            #             day: {
            #                 first_frame: constrained_neurons
            #             }
            #         })
            #         pass
            #
            #     all_steps = []
            #     for k, v in day_constrained_dict[day].items():
            #         all_steps.append(k)
            #     all_steps.sort()
            #     # higher_step = all_steps[0]
            #     # next_step = higher_step+1
            #     # print('Higher==>', higher_step, 'Next Step==>', next_step)
            #     day_constrained_dict[day].update({
            #         first_frame: constrained_neurons
            #     })
            #     previous_frame = first_frame - 1
            #     if first_frame > 1:
            #         print('day_constrained_dict--> ',day_constrained_dict)
            #         current_energy = day_constrained_dict[day][first_frame][2]
            #         previous_energy = day_constrained_dict[day][previous_frame][2]
            #         if current_energy > previous_energy:
            #             for_model = day_constrained_dict[day][previous_frame]
            #             del for_model[2:]
            #
            #             def change_list_order():
            #                 found_one = 'no'
            #                 for x in food_model_list:
            #                     if x[:-1] == for_model:
            #                         print(x[:-1], for_model)
            #                         x[2] = x[2] + 5
            #                         found_one = 'yes'
            #                 if found_one == 'no':
            #                     print('did not find any food')
            #                     for_model.append(5)
            #                     food_model_list.append(for_model)
            #
            #                 new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
            #                 pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
            #                 pickle.dump(new_list_order, pickle_out)
            #                 pickle_out.close()
            #         else:
            #             for_model = day_constrained_dict[day][previous_frame]
            #             del for_model[2:]
            #
            #             def change_list_order():
            #                 found_one = 'no'
            #                 for x in food_model_list:
            #                     if x[:-1] == for_model:
            #                         print(x[:-1], for_model)
            #                         x[2] = x[2] - 1
            #                         found_one = 'yes'
            #                 # if found_one == 'no':
            #                 #     print('did not find any food')
            #                 #     for_model.append(1)
            #                 #     food_model_list.append(for_model)
            #
            #                 new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
            #                 pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
            #                 pickle.dump(new_list_order, pickle_out)
            #                 pickle_out.close()
            #
            # if decided == 'no':
            #     # print('time for random')
            #     myList = [go_up, go_down, go_left, go_right]
            #     the_choice = random.choice(myList)
            #     the_choice()
            #     try:
            #         for k, v in day_constrained_dict[day].items():
            #             the_dayy = 'Just for the try except'
            #             # print(day, k)
            #     except KeyError:
            #         day_constrained_dict.update({
            #             day: {
            #                 first_frame: constrained_neurons
            #             }
            #         })
            #         pass
            #
            #     all_steps = []
            #     for k, v in day_constrained_dict[day].items():
            #         all_steps.append(k)
            #     all_steps.sort()
            #     # higher_step = all_steps[0]
            #     # next_step = higher_step+1
            #     # print('Higher==>', higher_step, 'Next Step==>', next_step)
            #     day_constrained_dict[day].update({
            #         first_frame: constrained_neurons
            #     })
            #     previous_frame = first_frame - 1
            #     if first_frame > 1:
            #         current_energy = day_constrained_dict[day][first_frame][2]
            #         previous_energy = day_constrained_dict[day][previous_frame][2]
            #         if current_energy > previous_energy:
            #             for_model = day_constrained_dict[day][previous_frame]
            #             del for_model[2:]
            #
            #             def change_list_order():
            #                 found_one = 'no'
            #                 for x in food_model_list:
            #                     if x[:-1] == for_model:
            #                         print(x[:-1], for_model)
            #                         x[2] = x[2] + 1
            #                         found_one = 'yes'
            #                 if found_one == 'no':
            #                     print('did not find any food')
            #                     for_model.append(1)
            #                     food_model_list.append(for_model)
            #
            #                 new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
            #                 pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
            #                 pickle.dump(new_list_order, pickle_out)
            #                 pickle_out.close()
            #         else:
            #             for_model = day_constrained_dict[day][previous_frame]
            #             del for_model[2:]
            #
            #             def change_list_order():
            #                 found_one = 'no'
            #                 for x in food_model_list:
            #                     if x[:-1] == for_model:
            #                         print(x[:-1], for_model)
            #                         x[2] = x[2] - 1
            #                         found_one = 'yes'
            #                 # if found_one == 'no':
            #                 #     print('did not find any food')
            #                 #     for_model.append(1)
            #                 #     food_model_list.append(for_model)
            #
            #                 new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
            #                 pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
            #                 pickle.dump(new_list_order, pickle_out)
            #                 pickle_out.close()

            # return new_list_order[0]

        else:
            print('I will go for random!')
            the_neurons = [dafood, (foodx, foody), head_position, head_direction, snake_head, snake_body]
            the_neurons_full = [dafood, (foodx, foody), head_position, head_direction, snake_head, snake_body]
            the_choice = random.choice(the_neurons)
            the_neurons.remove(the_choice)
            the_choice2 = random.choice(the_neurons)
            constrained_neurons_non_alphabetical = [the_choice, the_choice2]
            extra_data = [(current_energy + sum(food_energy)), first_frame, day]
            constrained_neurons = constrained_neurons_non_alphabetical + extra_data
            decided = 'no'
            if 'D|up' in constrained_neurons:
                decided = 'yes'
                # print('going up!')
                go_up()
            if 'D|down' in constrained_neurons:
                decided = 'yes'
                # print('going down!')
                go_down()
            if 'D|left' in constrained_neurons:
                decided = 'yes'
                # print('going left!')
                go_left()
            if 'D|right' in constrained_neurons:
                decided = 'yes'
                # print('going right!')
                go_right()
            if decided == 'no':
                # print('time for random')
                myList = [go_up, go_down, go_left, go_right]
                the_choice = random.choice(myList)
                the_choice()
            # if decided == 'yes':
            #     try:
            #         for k, v in day_constrained_dict[day].items():
            #             the_dayy = 'Just for the try except'
            #             # print(day, k)
            #     except KeyError:
            #         day_constrained_dict.update({
            #             day: {
            #                 first_frame: constrained_neurons
            #             }
            #         })
            #         pass
            #
            #     all_steps = []
            #     for k, v in day_constrained_dict[day].items():
            #         all_steps.append(k)
            #     all_steps.sort()
            #     # higher_step = all_steps[0]
            #     # next_step = higher_step+1
            #     # print('Higher==>', higher_step, 'Next Step==>', next_step)
            #     day_constrained_dict[day].update({
            #         first_frame: constrained_neurons
            #     })
            #     previous_frame = first_frame - 1
            #     if first_frame > 1:
            #         current_energy = day_constrained_dict[day][first_frame][2]
            #         previous_energy = day_constrained_dict[day][previous_frame][2]
            #         if current_energy > previous_energy:
            #             for_model = day_constrained_dict[day][previous_frame]
            #             del for_model[2:]
            #
            #             def change_list_order():
            #                 found_one = 'no'
            #                 for x in food_model_list:
            #                     if x[:-1] == for_model:
            #                         print(x[:-1], for_model)
            #                         x[2] = x[2] + 1
            #                         found_one = 'yes'
            #                 if found_one == 'no':
            #                     print('did not find any food')
            #                     for_model.append(1)
            #                     food_model_list.append(for_model)
            #
            #                 new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
            #                 pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
            #                 pickle.dump(new_list_order, pickle_out)
            #                 pickle_out.close()
            #         else:
            #             for_model = day_constrained_dict[day][previous_frame]
            #             del for_model[2:]
            #
            #             def change_list_order():
            #                 found_one = 'no'
            #                 for x in food_model_list:
            #                     if x[:-1] == for_model:
            #                         print(x[:-1], for_model)
            #                         x[2] = x[2] - 1
            #                         found_one = 'yes'
            #                 # if found_one == 'no':
            #                 #     print('did not find any food')
            #                 #     for_model.append(1)
            #                 #     food_model_list.append(for_model)
            #
            #                 new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
            #                 pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
            #                 pickle.dump(new_list_order, pickle_out)
            #                 pickle_out.close()


    combinationsList(the_neurons, 2)

    # if it_found_list!=[]:
    #     for x in it_found_list:
    #         constrained_neurons=x
    #         extra_data = [(current_energy + sum(food_energy)), first_frame, day]
    #         constrained_neurons = constrained_neurons_non_alphabetical+extra_data
    #         try:
    #             for k, v in day_constrained_dict[day].items():
    #                 the_dayy = 'Just for the try except'
    #                 # print(day, k)
    #         except KeyError:
    #             day_constrained_dict.update({
    #                 day: {
    #                     first_frame: constrained_neurons
    #                 }
    #             })
    #             pass
    #
    #         all_steps = []
    #         for k, v in day_constrained_dict[day].items():
    #             all_steps.append(k)
    #         all_steps.sort()
    #         # higher_step = all_steps[0]
    #         # next_step = higher_step+1
    #         # print('Higher==>', higher_step, 'Next Step==>', next_step)
    #         day_constrained_dict[day].update({
    #             first_frame: constrained_neurons
    #         })
    #         previous_frame = first_frame - 1
    #         if first_frame > 1:
    #             print('day_constrained_dict--> ',day_constrained_dict)
    #             current_energy = day_constrained_dict[day][first_frame][2]
    #             previous_energy = day_constrained_dict[day][previous_frame][2]
    #             if current_energy > previous_energy:
    #                 for_model = day_constrained_dict[day][previous_frame]
    #                 del for_model[2:]
    #
    #                 def change_list_order():
    #                     found_one = 'no'
    #                     for x in food_model_list:
    #                         if x[:-1] == for_model:
    #                             print(x[:-1], for_model)
    #                             x[2] = x[2] + 5
    #                             found_one = 'yes'
    #                     if found_one == 'no':
    #                         print('did not find any food')
    #                         for_model.append(5)
    #                         food_model_list.append(for_model)
    #
    #                     new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
    #                     pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
    #                     pickle.dump(new_list_order, pickle_out)
    #                     pickle_out.close()
    #             else:
    #                 for_model = day_constrained_dict[day][previous_frame]
    #                 del for_model[2:]
    #
    #                 def change_list_order():
    #                     found_one = 'no'
    #                     for x in food_model_list:
    #                         if x[:-1] == for_model:
    #                             print(x[:-1], for_model)
    #                             x[2] = x[2] - 1
    #                             found_one = 'yes'
    #                     # if found_one == 'no':
    #                     #     print('did not find any food')
    #                     #     for_model.append(1)
    #                     #     food_model_list.append(for_model)
    #
    #                     new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
    #                     pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
    #                     pickle.dump(new_list_order, pickle_out)
    #                     pickle_out.close()
    #
    #

    # extra_data = [(current_energy + sum(food_energy)), first_frame, day]
    # constrained_neurons = constrained_neurons_non_alphabetical + extra_data
    # try:
    #     for k, v in day_constrained_dict[day].items():
    #         the_dayy = 'Just for the try except'
    #         # print(day, k)
    # except KeyError:
    #     day_constrained_dict.update({
    #         day: {
    #             first_frame: constrained_neurons
    #         }
    #     })
    #     pass
    #
    # all_steps = []
    # for k, v in day_constrained_dict[day].items():
    #     all_steps.append(k)
    # all_steps.sort()
    # # higher_step = all_steps[0]
    # # next_step = higher_step+1
    # # print('Higher==>', higher_step, 'Next Step==>', next_step)
    # day_constrained_dict[day].update({
    #     first_frame: constrained_neurons
    # })
    # previous_frame = first_frame - 1
    # if first_frame > 1:
    #     current_energy = day_constrained_dict[day][first_frame][2]
    #     previous_energy = day_constrained_dict[day][previous_frame][2]
    #     if current_energy > previous_energy:
    #         for_model = day_constrained_dict[day][previous_frame]
    #         del for_model[2:]
    #
    #
    #         def change_list_order():
    #             found_one = 'no'
    #             for x in food_model_list:
    #                 if x[:-1] == for_model:
    #                     print(x[:-1], for_model)
    #                     x[2] = x[2] + 1
    #                     found_one = 'yes'
    #             if found_one == 'no':
    #                 print('did not find any food')
    #                 for_model.append(1)
    #                 food_model_list.append(for_model)
    #
    #             new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
    #             pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
    #             pickle.dump(new_list_order, pickle_out)
    #             pickle_out.close()
    #     else:
    #         for_model = day_constrained_dict[day][previous_frame]
    #         del for_model[2:]
    #
    #
    #         def change_list_order():
    #             found_one = 'no'
    #             for x in food_model_list:
    #                 if x[:-1] == for_model:
    #                     print(x[:-1], for_model)
    #                     x[2] = x[2] - 1
    #                     found_one = 'yes'
    #             # if found_one == 'no':
    #             #     print('did not find any food')
    #             #     for_model.append(1)
    #             #     food_model_list.append(for_model)
    #
    #             new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
    #             pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
    #             pickle.dump(new_list_order, pickle_out)
    #             pickle_out.close()

    # print(current_energy)
    # print(first_frame)

###############################################################################################################
###############################################################################################################
###############################################################################################################

    # def attention_control():
    #     pickle_constrained = open("memory/individual_neurons/constrained_vectors.pickle", "rb")
    #     constrained_dict = pickle.load(pickle_constrained)
    #     the_dict = constrained_dict[head_position]
    #     try:
    #         if the_dict!={'name': 'name'}:
    #
    #             print('YES!!!!!!', the_dict.keys())
    #             # for k,y in the_dict.items():
    #             #     if k !='name':
    #             #         print(k, y[3])
    #
    #     except KeyError:
    #         pass


    # attention_control()
    ##### Random Reflex ####
    # myList = [go_up, go_down, go_left, go_right]
    # the_choice = random.choice(myList)

    # def runnn():
    #     the_choice()

    # runnn()

    now = datetime.datetime.now()
    the_year = now.year
    the_month = now.month
    the_day = now.day
    the_hour = now.hour
    the_minutes = now.minute
    the_seconds = now.second
    date_info = str(the_seconds) + str(the_minutes) + str(the_hour) + str(the_day) + str(the_month) + str(the_year)
    date_info = int(date_info)
    # print(date_info)

    # def random_neurons():

    # constrained_neurons_non_alphabetical = [the_choice, the_choice2]
    #
    # # print(constrained_neurons_non_alphabetical)
    # try:
    #     constrained_neurons_non_alphabetical = sorted(constrained_neurons_non_alphabetical)
    # except TypeError:
    #     constrained_neurons_non_alphabetical = [the_choice, the_choice2]
    # extra_data = [(current_energy+sum(food_energy)), first_frame, day]
    # constrained_neurons = constrained_neurons_non_alphabetical+extra_data

    # constrained_dict[head_position].update({day: constrained_neurons})

    # !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!
    # !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!
    # !!!!!!!!!!! ##### THIS UPDATES THE CONSTRAINED NEURON FOR MEMORY MODEL
    # try:
    #     constrained_dict[head_position][day].update({date_info:constrained_neurons})
    #
    # except KeyError:
    #     constrained_dict[head_position].update({day:{date_info: constrained_neurons}})
    #     pass
    #
    # print('Constraint Neurons --> ',constrained_neurons)

    # !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!
    # !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!# !!!!!!!!!!!
    # !!!!!!!!!!! ##### THIS PRINTS THE FOOD ATTENTION MODEL
    ### CHOOSE MODEL - THIS PRINTS THE DRAFT MODEL

    # try:
    #     for k, v in day_constrained_dict[day].items():
    #         the_dayy = 'Just for the try except'
    #         # print(day, k)
    # except KeyError:
    #     day_constrained_dict.update({
    #         day:{
    #             first_frame:constrained_neurons
    #         }
    #     })
    #     pass
    #
    # all_steps = []
    # for k,v in day_constrained_dict[day].items():
    #     all_steps.append(k)
    # all_steps.sort()
    # # higher_step = all_steps[0]
    # # next_step = higher_step+1
    # # print('Higher==>', higher_step, 'Next Step==>', next_step)
    # day_constrained_dict[day].update({
    #     first_frame:constrained_neurons
    # })
    # previous_frame = first_frame-1
    # if first_frame >1:
    #     current_energy = day_constrained_dict[day][first_frame][2]
    #     previous_energy = day_constrained_dict[day][previous_frame][2]
    #     if current_energy > previous_energy:
    #         for_model = day_constrained_dict[day][previous_frame]
    #         del for_model[2:]
    #
    #
    #         def change_list_order():
    #             found_one = 'no'
    #             for x in food_model_list:
    #                 if x[:-1] == for_model:
    #                     print(x[:-1],for_model)
    #                     x[2] = x[2] + 1
    #                     found_one = 'yes'
    #             if found_one == 'no':
    #                 for_model.append(1)
    #                 food_model_list.append(for_model)
    #
    #             new_list_order = sorted(food_model_list, key=lambda e: e[2], reverse=True)
    #             #### This prints the attention for food model ####
    #             # print('\n\n',new_list_order,'\n\n')
    #             # pickle_out = open("memory/attention_models/food_attention.pickle", "wb")
    #             # pickle.dump(new_list_order, pickle_out)
    #             # pickle_out.close()
    #
    #
    #         change_list_order()
    #
    #


    # print(day_constrained_dict)


    # random_neurons()




    # #
    # pickle_out = open("memory/individual_neurons/constrained_vectors_new2.pickle", "wb")
    # pickle.dump(constrained_dict, pickle_out)
    # pickle_out.close()
    # pickle_out = open("memory/individual_neurons/constrained_vectors.pickle", "wb")
    # pickle.dump(constrained_dict, pickle_out)
    # pickle_out.close()

    ### Save In Memory ###


    # pickle_out = open("dict.pickle", "wb")
    # print('Sight dict\n\n', sight_dict)
    # print('Direction Dict\n\n', direction_dict)

    # print(head_position)
    time.sleep(delay)

wn.mainloop()

# print('The dict', sight_dict)
# print('Yes')
# example_dict = {1:"6",2:"2",3:"f"}
#
# pickle_out = open("dict.pickle","wb")
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()