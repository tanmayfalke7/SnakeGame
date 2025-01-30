import pygame
import random

pygame.mixer.init()
pygame.mixer.music.load('Snake_Game.mp3')
pygame.mixer.music.play()
pygame.init()
#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))
bgimg = pygame.image.load("photo_2024-02-19_15-17-42.jpg")
bgimg = pygame.transform.scale(bgimg , (screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("SnakeS GamE")

pygame.display.update()

# Game specific variables



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])


#snk_list =[]
#snk_length = 1
def Game_loop():
    #gamespecigicvariables

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    snake_size = 10
    init_velocity = 4
    velocity_x = 0
    velocity_y = 0
    score = 0

    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    fps = 30   
    snk_list =[]
    snk_length = 1 

    while not exit_game:
        if game_over:
            
            gameWindow.fill(white)
            text_screen("GO TO SLEEP ...(press enter to restart)", red, 100, 250)
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('Snake_Game.mp3')
                        pygame.mixer.music.play()
                        Game_loop()    
        else:    
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                    # snake_x = snake_x + 20
                     velocity_x = init_velocity
                     velocity_y = 0
                        
                #if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        #snake_x = snake_x - 20
                        velocity_x = -init_velocity
                        velocity_y = 0
                #if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        #snake_y = snake_y - 20
                        velocity_y = -init_velocity
                        velocity_x = 0
                #if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        #snake_y = snake_y + 20 
                        velocity_y = init_velocity
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y 
            if abs(snake_x - food_x)<7 and abs(snake_y - food_y)<7:
                score+=1  
                print("score :", score)
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length+=5 

            gameWindow.fill(black)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score"+ str(score + 1), white, 5,5)
            pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, snake_size]) 
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True    
            if (snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y> screen_height):
                game_over = True
                #pygame.mixer.music.load('')
                #pygame.mixer.music.play()
                print("Game Over")     
            #pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size]) 
            plot_snake(gameWindow, red,snk_list,snake_size)
        pygame.display.update() 
        clock.tick(fps)      

    pygame.quit()
    quit()    
Game_loop()    