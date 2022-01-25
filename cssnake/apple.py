

import random
import cv2


class Apple(object):
    def __init__(self) -> None:
        super().__init__()
        #self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.x = random.randrange(1,50)*10
        self.y = random.randrange(1,50)*10
        self.icon = cv2.imread("images/apple.png") / 255.0
        self.icon_w = 64    
        self.icon_h = 64
        self.icon = cv2.resize(self.icon, (self.icon_h, self.icon_w))

    
    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x, y):
        self.x = x
        self.y = y
