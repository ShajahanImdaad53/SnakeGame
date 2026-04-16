import pygame
import random
import time
import os

# --- Initialization and Constants ---
pygame.init()

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
grey = pygame.Color(200, 200, 200) 
brick_color = pygame.Color(100, 100, 100)

# Window size
window_x = 720
window_y = 480
grid_size = 10 

# Initializing game window
pygame.display.set_caption('Multi-Stage Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# Game State Variables
current_stage = 1
fruits_required_for_next_stage = 15
fruits_eaten_this_stage = 0
base_snake_speed = 10 # Slower starting speed
snake_speed = base_snake_speed

fps = pygame.time.Clock()

# --- Game Object Positions ---
snake_position = [window_x // 2, window_y // 2] 
snake_body = [[window_x // 2, window_y // 2], 
              [window_x // 2 - grid_size, window_y // 2], 
              [window_x // 2 - (2 * grid_size), window_y // 2]]
fruit_position = [random.randrange(1, (window_x//grid_size)) * grid_size, 
                  random.randrange(1, (window_y//grid_size)) * grid_size]
fruit_spawn = True
special_fruit_mode = False
fruits_eaten_total = 0 # Use total for blinking fruit logic

direction = 'RIGHT'
change_to = direction
score = 0

# High Score
high_score_file = 'high_score.txt'
if os.path.exists(high_score_file):
    with open(high_score_file, 'r') as f:
        high_score = int(f.read().strip())
else:
    high_score = 0

# --- Obstacles Data (Stage 2+) ---
obstacles = []

def generate_obstacles(stage):
    # Clears previous stage's obstacles
    global obstacles
    obstacles = []
    if stage < 2:
        return

    num_bricks = (stage - 1) * 20 # Increase number of bricks each stage
    for _ in range(num_bricks):
        while True:
            pos = [random.randrange(1, (window_x//grid_size)) * grid_size, 
                   random.randrange(1, (window_y//grid_size)) * grid_size]
            # Ensure new brick is not on snake or fruit
            if pos not in snake_body and pos != fruit_position:
                obstacles.append(pos)
                break

# --- Helper Functions ---
def show_score_and_stage(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Stage: {current_stage}  Score: {score}  High: {high_score}  Fruits to next: {max(0, fruits_required_for_next_stage - fruits_eaten_this_stage)}', True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def game_over():
    global high_score
    if score > high_score:
        high_score = score
        with open(high_score_file, 'w') as f:
            f.write(str(high_score))
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Game Over! Final Score: {score}', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

def draw_grid():
    for x in range(0, window_x, grid_size):
        pygame.draw.line(game_window, grey, (x, 0), (x, window_y), 1)
    for y in range(0, window_y, grid_size):
        pygame.draw.line(game_window, grey, (0, y), (window_x, y), 1)

def check_level_up():
    global current_stage, fruits_eaten_this_stage, snake_speed, fruits_required_for_next_stage
    if fruits_eaten_this_stage >= fruits_required_for_next_stage:
        current_stage += 1
        fruits_eaten_this_stage = 0
        snake_speed = base_snake_speed + (current_stage - 1) * 3 # Increase speed every stage
        generate_obstacles(current_stage)
        # Optionally, move the snake head back to center to avoid spawning in a wall
        snake_position[:] = [window_x // 2, window_y // 2]
        # Clear body to prevent instant collision bugs when moving to new map
        snake_body[:] = [list(snake_position)]


# --- Main Game Loop ---
paused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_p:
                paused = not paused
    
    if paused:
        continue
    
    # Validate direction change
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    # Move the snake (FIXED MOVEMENT LOGIC)
    if direction == 'UP':
        snake_position[1] -= grid_size
    if direction == 'DOWN':
        snake_position[1] += grid_size
    if direction == 'LEFT':
        snake_position[0] -= grid_size
    if direction == 'RIGHT':
        snake_position[0] += grid_size
    
    # Snake body growing mechanism and fruit handling
    snake_body.insert(0, list(snake_position)) 

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        fruits_eaten_this_stage += 1
        fruits_eaten_total += 1
        special_fruit_mode = (fruits_eaten_total % 10 == 0)
        score += 10
        fruit_spawn = False
        check_level_up() # Check for level up immediately after eating fruit
    else:
        snake_body.pop()
        
    # Spawn new fruit (ensure it doesn't spawn on obstacles)
    if not fruit_spawn:
        while True:
            new_pos = [random.randrange(1, (window_x//grid_size)) * grid_size, 
                       random.randrange(1, (window_y//grid_size)) * grid_size]
            if new_pos not in obstacles:
                fruit_position = new_pos
                fruit_spawn = True
                break
        
    # Refresh game screen with white background and draw grid
    game_window.fill(white)
    draw_grid()

    # Draw obstacles
    for block in obstacles:
        pygame.draw.rect(game_window, brick_color, pygame.Rect(block[0], block[1], grid_size, grid_size))

    # Draw snake head (ellipse) and body (rects)
    head_rect = pygame.Rect(0, 0, grid_size * 2, grid_size * 1.5)
    head_rect.center = (snake_body[0][0] + grid_size/2, snake_body[0][1] + grid_size/2)
    pygame.draw.ellipse(game_window, blue, head_rect)

    for pos in snake_body[1:]:
        body_rect = pygame.Rect(pos[0], pos[1], grid_size, grid_size)
        pygame.draw.rect(game_window, green, body_rect)
    
    # Draw fruit as a circle (blinking red if special, else black)
    fruit_color = black 
    if special_fruit_mode:
        if int(pygame.time.get_ticks() / 250) % 2 == 0:
             fruit_color = red
    pygame.draw.circle(game_window, fruit_color, (fruit_position[0] + grid_size // 2, fruit_position[1] + grid_size // 2), grid_size // 2)
    
    # Game Over conditions:
    # Hitting walls
    if snake_position[0] < 0 or snake_position[0] > window_x - grid_size:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - grid_size:
        game_over()
        
    # Hitting own body
    for block in snake_body[1:]:
        if block[0] == snake_position[0] and block[1] == snake_position[1]:
            game_over()
    
    # Hitting obstacles (New condition for stage 2+)
    if current_stage >= 2:
        for block in obstacles:
            if block[0] == snake_position[0] and block[1] == snake_position[1]:
                game_over()
            
    # Display score and stage information
    show_score_and_stage(black, 'times new roman', 20)
    
    if paused:
        pause_font = pygame.font.SysFont('times new roman', 50)
        pause_surface = pause_font.render('PAUSED', True, red)
        pause_rect = pause_surface.get_rect()
        pause_rect.center = (window_x/2, window_y/2)
        game_window.blit(pause_surface, pause_rect)
    
    # Update display and control speed
    pygame.display.update()
    fps.tick(snake_speed)
