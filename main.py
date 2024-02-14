import pygame
import random

pygame.init()

screen_width = 1280
screen_height = 720
gui_font = pygame.font.Font("sysfont.otf", 36)

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Will You Be My Valentine?")
Icon = pygame.image.load("heart.png")
pygame.display.set_icon(Icon)

class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Initializing type (yes or no)
        self.type = text
        self.james_clicked = False

        # Initializing Button Shape and Color
        self.top_rect = pygame.Rect(pos, (width,height))
        self.top_color = "#f7879A"
        self.bot_rect = pygame.Rect(pos, (width, height))
        self.bot_color = "#522D33"

        # Initializing Button Display Text
        self.text_surf = gui_font.render(text, True, "#000000")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

        # Initializing Button Height  
        self.elevation = elevation
        self.change_in_elevation = elevation
        #self.og_y_pos = pos[1]

        # Initializing Button Clicked Status
        self.clicked = False
        self.og_y_pos = pos[1]


    def draw(self):

        # if yes is clicked load screen with image
        if self.james_clicked:
            james = pygame.image.load('success.png').convert_alpha()
            screen.blit(james, (0, 0))

            # moves yes and no buttons out of the way
            yes_button.top_rect.x = 10000
            yes_button.top_rect.y = 10000
            no_button.top_rect.x = 10000
            no_button.top_rect.y = 10000

        # button animation logic
        self.top_rect.y = self.og_y_pos - self.change_in_elevation 
        self.text_rect.center = self.top_rect.center

        self.bot_rect.midtop = self.top_rect.midtop
        self.bot_rect.height = self.top_rect.height + self.change_in_elevation
        
        # drawing buttons
        pygame.draw.rect(screen, self.bot_color, self.bot_rect, border_radius=32)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=32)
        screen.blit(self.text_surf, self.text_rect)
        self.checkClick()

    def checkClick(self):
        pos = pygame.mouse.get_pos()

        # check if mouse is in within buttons
        if self.top_rect.collidepoint(pos) or self.bot_rect.collidepoint(pos):
            self.top_color = '#C06978'
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1:
                self.change_in_elevation = 0
                self.clicked = True
            else:
                self.change_in_elevation = self.elevation
                if self.clicked:
                        if self.type == "NO":
                            self.randomize(screen_width,screen_height)
                        elif self.type == "YES":
                            self.james_clicked = True
                        self.clicked = False
        else:
            self.top_color = '#F7879A'
            self.change_in_elevation = self.elevation
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    def randomize(self, screen_width, screen_height):

        #randomize position of "no" button
        self.top_rect.x = random.choice(list(range(0, 175)) + list(range(500, screen_width - self.top_rect.width)))
        self.og_y_pos = random.choice(list(range(0, 575)) + list(range(625, screen_height - self.top_rect.height)))        

yes_button = Button("YES", 175, 50, (325, 645), 6)
no_button = Button("NO", 175, 50, (775, 645), 6)
valentine = pygame.image.load('valentine.png').convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 253, 208))
    screen.blit(valentine, (screen_width // 2 - valentine.get_width() // 2, screen_height // 2.25 - valentine.get_height() // 2))
    yes_button.draw()
    no_button.draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
