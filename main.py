import pygame

#pygame setup
pygame.init()
width = 720
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
base_size = 40
title_font = pygame.font.SysFont("Roboto", base_size)
labels_font = pygame.font.SysFont("Roboto", base_size)
movement_speed = base_size*4
global base_color, collision_color, player_color
base_color = 'white'
collision_color = 'red'
player_color = base_color


enum_directions = {
    'left': [-1,0],
    'right': [1,0],
    'down': [0,1],
    'up': [0,-1]
}

def move(direction, pos):
    pos.x += movement_speed * dt * direction[0]
    pos.y += movement_speed * dt * direction[1]
    print(f'{round(pos.x,0)}:{round(pos.y,0)}')
    collision(pos)

def level_generation():
    segment = (150,150,80,200)
    pygame.draw.rect(screen, "orange", segment)
    return [segment]

def collision(pos):
    for segment in segments:
        if round(pos.x + base_size//2,0) == segment[0] or round(pos.x - base_size//2,0) == segment[0] + segment[2] or round(pos.y + base_size//2,0) == segment[1] or round(pos.y + base_size//2,0) == segment[1] + segment[3]:
                player_color = collision_color
                print(f"BOOM: player({pos.x},{pos.y}) | segment({segment})")
        else:
            player_color = base_color


def run():
    global dt
    dt = 0 
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("darkgreen")
        pygame.draw.rect(screen, "black", (0,0,width,base_size*1.5))
        global segments
        segments = level_generation()
        pygame.draw.rect(screen, player_color, (player_pos[0]-10,player_pos[1]-10,base_size,base_size))
        title_text = title_font.render('SquaredCorridor', True, 'white')

        screen.blit(title_text, ( (width // 2) - (title_text.get_width() // 2) , base_size // 2 ))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_pos[1] > base_size*1.5 + base_size // 2 :
            move(enum_directions['up'], player_pos)
        if keys[pygame.K_s] and player_pos[1] < height - base_size:
            move(enum_directions['down'], player_pos)
        if keys[pygame.K_a] and player_pos[0] > base_size // 2:
            move(enum_directions['left'], player_pos)
        if keys[pygame.K_d] and player_pos[0] < width - base_size:
            move(enum_directions['right'], player_pos)

        pygame.display.flip()
        
        dt = clock.tick(60)/1000


    pygame.quit()

def main():
    run()

if __name__ == '__main__':
    main()

# Create separate surfaces for menu and game
# Add level_generation()
