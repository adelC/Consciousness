from typing import Any, Dict, Tuple
from gym import Env
from gym import spaces
import cv2
from utils import init_turtle_env
import numpy as np
import random
from snake_agent import SnakeAgent
from apple import Apple

#from gym.core import _ActionType, _OperationType


# To make our own environment, we will need
# 1. an initialize 
# 2. a reset
# 3. a stateSpace -- NOK
# 4. a stateSpacePlus -- NOK
# 5. PossibleActions
# 6. is the move legal ? 
# 7. effect the environement 
# 8. step function need to return the new position 

SCREEN_V = 8 # The lenght of the vector perceived by the snake 



class SnakeEnv(Env):
    def __init__(self) -> None:
        super().__init__()
       
        self.state_space = None
        self.action_space = spaces.Discrete(9,)
        self.observation_space = spaces.Box(low=0, high=255, shape=(SCREEN_V, 3))
        
        # Create a canvas to render the environment images upon 
        self.current_screen = np.ones((500,500,3),dtype='uint8')

       # Define elements present inside the environment
        self.elements = []
       


    def reset(self) -> Any:
        self.snake = SnakeAgent("Snake")
        self.apple = Apple()
        self.elements = [self.snake, self.apple]
        self.current_screen = np.ones((500,500,3),dtype='uint8')
        self.draw_elements_on_current_screen()

    
    
    def step(self, action):

        self.check_action_valide(action)
        if self.snake.direction == 0:
            self.snake.move(-10, 0)
        elif self.snake.direction == 1:
            self.snake.move(10, 0)
        elif self.snake.direction == 2:
            self.snake.move(0, 10)
        elif self.snake.direction == 3:
            self.snake.move(0, -10)
        elif self.snake.direction == 4:
            self.snake.move(10, -10)
        elif self.snake.direction == 5:
            self.snake.move(-10, -10)
        elif self.snake.direction == 6:
            self.snake.move(10, 10)
        elif self.snake.direction == 7:
            self.snake.move(-10, 10)

         # Increase Snake length on eating apple
        if self.snake.get_position() == self.apple.get_position():
            self.apple.set_position(random.randrange(1,50)*10,random.randrange(1,50)*10)
            #score += 1
            self.snake.snake_position.insert(0, list(self.snake.head))

        else: 
            self.snake.snake_position.insert(0, list(self.snake.head))
            print("before", self.snake.snake_position)
            self.snake.snake_position.pop()
            print("after", self.snake.snake_position)

        # Draw elements on the canvas
        self.current_screen = np.zeros((500,500,3),dtype='uint8')
        self.draw_elements_on_current_screen()

  
        
    def render(self):
        cv2.imshow("Game", self.current_screen)
        cv2.waitKey(100)
        
   
     
    def draw_elements_on_current_screen(self):
        
        cv2.rectangle(self.current_screen, (self.apple.x, self.apple.y), (self.apple.x + 10, self.apple.y + 10), (0, 0, 255), 3)
        # Apple icone !!
        #x = self.apple.get_position()[0]
        #y = self.apple.get_position()[1]
        #self.current_screen[y : y + self.apple.icon.shape[1], x:x + self.apple.icon.shape[0]] = self.apple.icon
        
        # Display Snake
        for position in self.snake.snake_position:
                cv2.rectangle(self.current_screen, (position[0], position[1]), (position[0] + 10, position[1] + 10), (0, 255, 0), 3)

    
    
    def check_action_valide(self, action):

        # Assert that it is a valid action 
        assert self.action_space.contains(action), "Invalid Action"
        if action == 0 and self.snake.direction != 1:
            self.snake.direction = 0
        elif action == 1 and self.snake.direction != 0:
            self.snake.direction = 1
        elif action == 2 and self.snake.direction != 3:
            self.snake.direction = 2
        elif action == 3 and self.snake.direction != 2:
            self.snake.direction = 3
        elif action == 4 and self.snake.direction != 7:
            self.snake.direction = 4
        elif action == 5 and self.snake.direction != 6:
            self.snake.direction = 5
        elif action == 6 and self.snake.direction != 5:
            self.snake.direction = 6
        elif action == 7 and self.snake.direction != 4:
            self.snake.direction = 7
        else:
            self.snake.direction = action



    def get_action_meanings(self):
        return {0: "Left", 1: "Right", 2: "Up", 3: "Down", 4: "DownRight", 5: "DownLeft", 6: "UpRight", 7: "UpLeft"}


if __name__ == "__main__":
    
    env = SnakeEnv()
    obs = env.reset()

    while True:
        # Take a random action
        #action = env.action_space.sample()
        action = int(np.random.randint(8, size=1))
        env.step(action)
        # Render the game
        env.render()
        #if done == True:
        #    break

    env.close()



