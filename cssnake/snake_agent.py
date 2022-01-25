import cv2

class SnakeAgent(object):
    def __init__(self, name) -> None:
        #self.icon = cv2.imread("snake.png") / 255.0
        #self.icon_w = 64
        #self.icon_h = 64
        #self.icon = cv2.resize(self.icon, (self.icon_h, self.icon_w))
        self.name = name
        #self.x = 0
        #self.y = 0
        self.snake_position = [[250,250],[240,250],[230,250]]
        self.head = [250, 250]
        self.direction = 1

    def set_position(self, x, y):
        self.head[0] = x 
        self.head[1] = y
    
    def get_position(self):
        return (self.head[0], self.head[1])
    
    def move(self, x, y):
        self.head[0] += x
        self.head[1] += y
        
