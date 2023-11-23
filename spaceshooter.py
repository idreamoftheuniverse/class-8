import turtle
import random

screen = turtle.Screen()
screen.setup(400, 600)
screen.bgpic("background.png")

# Spaceship image
spaceship_img = "spaceship.png"
screen.register_shape(spaceship_img)

# Asteroid image
asteroid_img = "asteroid.png"
screen.register_shape(asteroid_img)

# Bullet image
bullet_img = "bullet.png"
screen.register_shape(bullet_img)

# Blast image
blast_img = "blast.png"
screen.register_shape(blast_img)

# Game over image
game_over_img = "game_over.png"
screen.register_shape(game_over_img)

# Asteroid turtle
asteroid = turtle.Turtle()
asteroid.penup()
asteroid.goto(0, 250)
asteroid.shape(asteroid_img)

# Bullet turtle
bullet = turtle.Turtle()
bullet.shape(bullet_img)
bullet.hideturtle()
bullet.penup()
bullet.speed(0)

# Spaceship turtle
spaceship = turtle.Turtle()
spaceship.penup()
spaceship.goto(0, -230)
spaceship.shape(spaceship_img)

# Score turtle
score_turtle = turtle.Turtle()
score_turtle.speed(0)
score_turtle.color("white")
score_turtle.penup()
score_turtle.goto(-190, 230)
score_turtle.pendown()
score_turtle.hideturtle()

# Create score variable
score = 0

# Lives turtle
lives_turtle = turtle.Turtle()
lives_turtle.speed(0)
lives_turtle.color("white")
lives_turtle.penup()
lives_turtle.goto(80, 230)
lives_turtle.pendown()
lives_turtle.hideturtle()

# Create lives variable
lives = 5

# Create game_state variable 
game_state = "play"

# Game over turtle
game_over = turtle.Turtle()
game_over.speed(0)
game_over.penup()
game_over.goto(0, 0)
game_over.hideturtle()
game_over.shape(game_over_img)

# Position the bullet turtle
bullet_x = spaceship.xcor()
bullet_y = spaceship.ycor() + 10
bullet.goto(bullet_x, bullet_y)

# Bullet movement variables
bullet_state = "loaded"

# Movement functions
def move_left():
    # move left  when game state "play"
    if(game_state == "play"):
        spaceship_x = spaceship.xcor()
        spaceship_y = spaceship.ycor()
        spaceship.goto(spaceship_x - 10, spaceship_y)
    
def move_right():
    # move right  when game state "play"
    if(game_state == "play"):
        spaceship_x = spaceship.xcor()
        spaceship_y = spaceship.ycor()
        spaceship.goto(spaceship_x + 10, spaceship_y)

# Define the fire function
def fire():
    global bullet_state
    if bullet_state == "loaded":
        bullet_state = "fired"
        bullet.goto(spaceship.xcor(), spaceship.ycor())
        bullet.showturtle()

# Create display_score function
def display_score():
    global score
    score_turtle.clear()
    score_turtle.write("Score: " + str(score), font=("Arial", 20, "bold"))
    
# Create display_lives function
def display_lives():
    global lives
    lives_turtle.clear()
    lives_turtle.write("Lives: " + str(lives), font=("Arial", 20, "bold"))
    
# Create keyboard bindings
screen.listen()
screen.onkey("Left", move_left)
screen.onkey("Right", move_right)
screen.onkey("Space", fire)
        
# Check collision between the asteroid and boundary to reset the asteroid
def reset_asteroid():
    if asteroid.ycor() < -300: #Bottom Wall
        asteroid.hideturtle()
        asteroid.goto(random.randint(-170, 170), 270)
        asteroid.showturtle()
        
# Check collision between the asteroid and bullet to destroy the asteroid
def destroy_asteroid():
    global bullet_state, score
    if bullet.distance(asteroid) < 34:
        bullet_state = "loaded"
        score = score + 1
        bullet.hideturtle()
        bullet.goto(spaceship.xcor(), spaceship.ycor())
        asteroid.hideturtle()
        asteroid.goto(random.randint(-170, 170), 270)
        asteroid.showturtle()

# Add screen tracer
screen.tracer(0)
        
# Loop to move the asteroid
while asteroid.ycor() > -330:
    # Write condition for game state "play"
    if(game_state == "play"):
        asteroid.goto(asteroid.xcor(), asteroid.ycor() - 5)
        reset_asteroid()
        destroy_asteroid()

        # Move the bullet
        if bullet_state == "fired":
            bullet_x = bullet.xcor()
            bullet_y = bullet.ycor()
            bullet.goto(bullet_x, bullet_y + 15)

        # Change bullet state to loaded
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullet_state = "loaded"
    
        distance = spaceship.distance(asteroid)
        
        # Check collision between spaceship and asteroid
        if  distance <= 67:
            # decrease lives count
            lives = lives - 1
            # reset asteroid position
            asteroid.hideturtle()
            asteroid.goto(random.randint(-170, 170), 270)
            asteroid.showturtle()

            # Write condition for blast
            if(lives == 0):
                spaceship.shape(blast_img)
                game_state = "over"
        
    # Write condition for game over
    if game_state == "over":
        game_over.showturtle()
    
    # Call display_score function
    display_score()

    # Call display_lives function
    display_lives()
    
    # Update the screen
    screen.update()