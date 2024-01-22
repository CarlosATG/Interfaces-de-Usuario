import pygame, sys
from button import Button

pygame.init()
pygame.mixer.music.load("8bit.mp3")
pygame.mixer.music.play(-1)  # The -1 means the music will loop indefinitely
pygame.mixer.music.set_volume(0.1)
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load("assets/Arcoiris.png")
Siguiente = pygame.image.load("assets/next.png").convert_alpha()
Back= pygame.image.load("assets/back.png").convert_alpha()
BG_Mensajes= pygame.image.load("assets/Messages.png").convert_alpha()
font =pygame.font.Font("assets/Pixel_like.ttf",24)
timer=pygame.time.Clock()
snip = font.render('', True, 'black')
speed= 3
done= False
class boton():
    def __init__(self, x,y,image, scale):
        width=image.get_width()
        height = image.get_height()
        self.image= pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
    def draw(self):
        pos= pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1:
                print('CLICKED')
        SCREEN.blit(self.image,(self.rect.x,self.rect.y))

Btn_Siguiente=boton(1200,20,Siguiente, 0.05)
Btn_Back=boton(30,20,Back, 0.05)
Btn_Message=boton(0, 520, BG_Mensajes, 1)
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/04B_30__.TTF", size)

def FirstLevel():
    blue = (0, 0, 255)  # RGB for blue
    pink = (255, 192, 203)  # RGB for pink
    counter = 0
    message=""
    font = pygame.font.Font("assets/Pixel_like.ttf", 24)
    screen_width, screen_height = SCREEN.get_size()
    # Main loop for the first level
    running = True
    Primer_Mensaje= 'Hola, vamos a empezar este nivel de la mejor manera posible...'
    while running:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return  # Exit the function
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check which half was clicked
                if event.pos[0] < screen_width // 2:
                    message = "Blue half clicked!"
                else:
                    message = "Pink half clicked!"

        # Draw the two halves
        SCREEN.fill((255, 255, 255))  # Clear screen
        pygame.draw.rect(SCREEN, blue, (0, 0, screen_width // 2, screen_height))
        pygame.draw.rect(SCREEN, pink, (screen_width // 2, 0, screen_width // 2, screen_height))
        Btn_Siguiente.draw()
        Btn_Back.draw()
        Btn_Message.draw()
        # Display the message
        if counter < speed *len(Primer_Mensaje):
            counter +=1
        elif counter >=speed*len(Primer_Mensaje):
            done = True
        snip= font.render(Primer_Mensaje[0:counter//speed], True, 'Black')
        SCREEN.blit(snip,(38,560))
        if message:
            font = pygame.font.Font("assets/Pixel_like.ttf", 24)
            text = font.render(message, True, (0, 0, 0))
            SCREEN.blit(text, (screen_width // 4, screen_height // 2))

        pygame.display.flip()
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():

    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        #pygame.mixer.music.play(-1)  # The -1 means the music will loop indefinitely
        MENU_TEXT = get_font(100).render("SEXUALIDAD", True, "#f08080")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="JUGAR", font=get_font(75), base_color="#FFB2B2", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="INFO", font=get_font(75), base_color="#FFFBEF", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        pos=pygame.mouse.get_pos()
        print(pos)
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #play()
                    FirstLevel()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

main_menu()