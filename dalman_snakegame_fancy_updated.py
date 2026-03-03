"""Credits and attributions:
    The code for classes is created by github user sree-hari-s.
    Game code built in Object-Oriented Programming class led by Dr. Feaver.
    Code further modified by myself (senior, 1st year CS).
    Hungry Hungry Caterpillar head image credit: teacherspayteachers.com.
    Apple gif image credit: fity.club."""

import time
import turtle
from random import randint
ALIGNMENT = "Center"
FONT = ("Courier", 20, "bold")
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SCREEN = turtle.Screen()


class Snake:
    """A class representing a snake (caterpillar).
    
    Attributes:
        segments (list): Contains all segments of snake object.
        create_snake() (method): Method initializing creation of snake segments.
        head (turtle): Represents head of snake, first item in segments.
        head.shape (method): Change shape of head segment."""
    
    
    def __init__(self):
        """Init Snake class.
        
        Establish attributes of Snake class.
        Also define image and register it as turtle shape.
        Then, apply image as shape to head."""
        
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        image = "caterpillar head.gif.gif"
        turtle.register_shape(image)
        self.head.shape(image)

    def create_snake(self):
        """Create segment at each starting coordinate by calling add_segment()."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Create new segment turtle object.
            Give segment circle shape and green color.
            Set it to not draw as it moves.
            Move to position outlined in function parameter.
            Add new segment to self.segments.
        
        Parameters:
            position: Takes value of coord set iterated through last function's for loop."""
            
        new_segment = turtle.Turtle("circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Call add_segment() and add it to end of self.segments list."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Iterate backwards through self.segments by -1.
            Create new_x variable storing current x-coord of last segment.
            Create new_y variable storing current y-coord of last segment.
            Move iterated segment to new coordinates (new_x, new_y).
            Move head forward 20 pixels."""
        
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        """Heading of head is set to UP if not already."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Heading of head is set to DOWN if not already."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Heading of head set to LEFT if not already."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Heading of head is set to RIGHT if not already."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


class Food(turtle.Turtle):
    """A class representing food/apple items the snake eats.
    
    Attributes:
        super().__init__() (method): Inherit Turtle class methods and attributes.
        shape() (method): Change shape of Food item.
        penup() (method): Object does not draw when moving.
        shapesize() (method): Sets length and width of object.
        speed() (method): Sets speed of Food object when moving.
        goto() (method): Object moves to parameter coordinates.
        refresh_food_location() (method): Moves food item to new location."""
        
    
    def __init__(self):
        """Init Food class."""
        super().__init__()
        image = "Red-apple-jumping.gif"
        turtle.register_shape(image)
        self.shape(image)
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.speed("fastest")
        random_x = randint(-270, 270)
        random_y = randint(-270, 260)
        self.goto(random_x, random_y)
        self.refresh_food_location()

    def refresh_food_location(self):
        """Moves food item to new location.
        
        Assign local variable random_x to random int between -280 and 280.
        Assign local variable random_y to random int between -280 and 280.
        Move food object to coordinates set to random_x, random_y."""
            
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
        

class Score(turtle.Turtle):
    """A class representing the text of score (apples eaten) UI.
    
    Attributes:
        super().__init__() (method): Inherit Turtle class methods and attributes.
        penup() (method): Object does not draw when moving.
        color() (method): Change color to white.
        hideturtle() (method): Hide score.
        goto() (method): Object moves to parameter coordinates.
        score (int): Score value (as opposed to turtle object).
        current_score() (method): Write current value of score variable."""
    
    
    def __init__(self):
        """Init Score class."""
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.current_score()

    def increase_score(self):
        """Add 1 to score, clears previous score, calls current_score() on self."""
        self.score += 1
        self.clear()
        self.current_score()

    def current_score(self):
        """Write value of score.
            Format: aligned center; Courier 20 pt bold font."""
            
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Write "Game Over at coord (0, 0).
            Format: aligned center; Courier 20 pt. bold font."""
            
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)


def screen_setup():
    """Call global variable SCREEN.
        Change SCREEN's width/height to 600x600 pixels.
        Set SCREEN's background color to #90EE90."""
        
    global SCREEN 
    SCREEN.setup(width = 600,height = 600)
    SCREEN.bgcolor("#90EE90")

def reset_game(self, score):
    """End game by calling game_over() on score. 
        Update SCREEN, and has program sleep for 2 seconds.
    
    Parameters:
        score: instance of Score() established within game()."""
    
    score.game_over()
    SCREEN.update()
    time.sleep(2)

def game():
    """Setup screen, class instances, controls, main loop controlling game. 
    
    Setup:
    Call global variable SCREEN, run screen_setup(), and give SCREEN title. 
    Disable automatic screen refreshes.
    Create instances of Snake(), Food(), and Score() classes.
    Tell SCREEN to take computer inputs.
    Assign each direction method to the respective arrow key.
    
    Game while loop:
    Refresh SCREEN, set time.sleep to 0.1, call snake.move().
    Detect if food has been eaten.
    If distance of head is less than 20 pixels from food:
    Refresh food location, increase score, extend snake by 1 segment.
    Detect if snake has collided with wall.
    Detect if snake has collided with self.
    For each segment starting from index [2:]:
    If distance bw head and seg less than 15 pixels:
    Break loop, call score.game_over(), update screen, sleep time 2 sec."""
    
      
    global SCREEN
    screen_setup()
    SCREEN.title("The Hungry Hungry Caterpillar Munching Simulator!")
    SCREEN.tracer(0)
    snake = Snake()
    food = Food()
    score = Score()
    SCREEN.listen()
    SCREEN.onkey(snake.up, "Up")
    SCREEN.onkey(snake.down, "Down")
    SCREEN.onkey(snake.left, "Left")
    SCREEN.onkey(snake.right, "Right")
    
    game_on = True
    while game_on:
        SCREEN.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 20:
            food.refresh_food_location()
            score.increase_score()
            snake.extend()
        if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
            game_on = False
            score.game_over()
            SCREEN.update()
            time.sleep(2)
        for seg in snake.segments[2:]:
            if snake.head.distance(seg) < 15:
                game_on = False
                score.game_over()
                SCREEN.update()
                time.sleep(2)
                
def main():
    """Program entry point.
    
    Call global variable SCREEN, run screen_setup(), and give SCREEN title.
    Displays title and asks player if they want to play, y/n.
    If "y" is inputted, run game().
    After game loop is broken, clear screen and run setup on it again."""
    
    
    global SCREEN
    screen_setup()
    SCREEN.title("The Hungry Hungry Caterpillar Munching Simulator!")
    while SCREEN.textinput("The Hungry Hungry Caterpillar Munching Simulator!", "Do you want to play? y/n") == "y":
        game()
        SCREEN.clearscreen()
        screen_setup()
        
# Entry function is only called if file is run directly.
# If imported as module, main() will not be called.        
if __name__ == "__main__":
    main()