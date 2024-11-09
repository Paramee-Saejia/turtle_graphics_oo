import turtle
import random
class Polygon:
    def __init__(self, num_sides ):
        self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-250, 250), random.randint(-100, 100)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)
        self.t= turtle.Turtle()
        self.t.pensize(random.uniform(0.05, 10))
        self.t.speed(0)
        self.t.hideturtle()


    def draw_polygon(self):


        #set angle
        self.t.penup()
        self.t.goto(self.location[0], self.location[1])
        self.t.setheading(self.orientation)
        self.t.pencolor(self.color)
        self.t.pensize(self.border_size)
        self.t.pendown()
        angle = 360 / self.num_sides
        for _ in range(self.num_sides):
            self.t.forward(self.size)
            self.t.left(angle)
        turtle.penup()


class  EmbeddedPolygon(Polygon):
    def __init__(self,num_sides):
        super().__init__(num_sides)
        self.reduction_ratio = 0.618



    def draw_embedpolygon(self ):
        for _ in range(self.num_sides):
            self.draw_polygon()
            self.__reposition()




    def __reposition(self):
        self.size *= self.reduction_ratio

        self.t.penup()
        self.t.forward(self.size * (1 - self.reduction_ratio) / 2)
        self.t.left(90)
        self.t.forward(self.size * (1 - self.reduction_ratio) / 2)
        self.t.right(90)
        self.location[0] = self.t.pos()[0]
        self.location[1] = self.t.pos()[1]

class Run():
    def __init__(self, choice):

        screen = turtle.Screen()
        screen.bgcolor('black')
        screen.setup(800, 600)
        screen.colormode(255)
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            n_poly = 20
            if choice == 1:
               for i in range(n_poly): self.__normal_poly(3)
            if choice == 2:
                for i in range(n_poly): self.__normal_poly(4)
            if choice == 3:
                for i in range(n_poly): self.__normal_poly(5)
            if choice == 4:
                action = self.__normal_poly
                for i in range(n_poly):
                    action(random.choice([3, 4, 5]))

        if choice == 5 or choice == 6 or choice == 7 or choice == 8:
             n_poly = 20
             if choice == 5:
                for i in range(n_poly): self.__embedded_poly(3)
             if choice == 6:
                for i in range(n_poly): self.__embedded_poly(4)
             if choice == 7:
                 for i in range(n_poly): self.__embedded_poly(5)
             if choice == 8:
                 action = self.__embedded_poly
                 for i in range(n_poly):
                    action(random.choice([3, 4, 5]))

             if choice == 9:
                 action = [
                     self.__normal_poly, self.__embedded_poly
                 ]
                 for i in range(n_poly):
                    random.choice(action)(random.choice([3, 4, 5]))







    def __normal_poly(self,num_sides):
        poly = Polygon(num_sides)
        poly.draw_polygon()

    def __embedded_poly(self,num_sides):
        poly = EmbeddedPolygon(num_sides)
        poly.draw_embedpolygon()



choice = Run(choice=1)




