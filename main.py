import pygame

class Game():
    
    corredores =[]
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((600, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
        
        self.runner = pygame.image.load("images/smallball.png")
        
    def competir(self):
        
        x = 0
        
        while True:
            #comprobación de los eventos
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
            # Refrescar / renderizar la pantalla
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()
        
if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.competir()