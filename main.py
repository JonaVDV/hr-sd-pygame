import pygame

class Player:
    def __init__(self, delta_time, screen) -> None:
        self.position = pygame.Vector2(0, 0)
        self.color = pygame.Color(0, 0, 0)
        self.delta_time = delta_time
        self.screen = screen
        pass
    
    def getPosition(self):
        return self.position

    def initPlayer(self, position, color):
        
        pygame.draw.circle(self.screen, color, (int(position.x), int(position.y)), 40)
    
    def setPosition(self, position):
        self.position = position
        pass
    
    def setColor(self, color):
        self.color = color
        pass


    def setPlayerControls(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.position.y -= 300 * self.delta_time
        if key[pygame.K_a]:
            self.position.x -= 300 * self.delta_time
        if key[pygame.K_s]:
            self.position.y += 300 * self.delta_time
        if key[pygame.K_d]:
            self.position.x += 300 * self.delta_time
    
    pass

class Game_Profile:
    def __init__(self, pygame = pygame) -> None:
        self.fps = pygame.time.Clock().get_fps()
        # player position
        self.player_position = pygame.Vector2(0, 0)
        
        
        pass
        
    pass
    
class Game:
    def __init__(self, fps, clock: pygame.time.Clock, 
                 screen = None, pygame = pygame) -> None:
        self.pygame = pygame
        self.fps = fps
        self.clock = clock
        self.screen = screen
        self.running = True
        self.delta_time = clock.tick(fps) / 1000.0
        self.player_position = pygame.Vector2(0, 0)
        self.current_fps = 0
        self.player = Player(self.delta_time, self.screen)
    
    def initGame(self):
        self.pygame.init()
        self.clock = self.pygame.time.Clock()
        self.screen = self.pygame.display.set_mode((800, 600), self.pygame.RESIZABLE)
        self.pygame.display.set_caption("Game")
        self.gameLoop()
    
    def slomotion(self):
        self.delta_time = self.clock.tick(self.fps) / 500.0
    
    def gameLoop(self):
        """
        The main game loop that runs while the game is running. It updates the clock, checks if the game should be quit,
        creates the player, and updates the display.
        """
        while self.running:
            self.clock.tick(self.fps)
            self.checkQuitGame()
            self.createPlayer()
            self.createPlayerControls()
            self.pygame.display.update()
    
    def createPlayer(self):
        if self.screen is None:
            return
        width, height = self.screen.get_size()
        self.player_position = pygame.Vector2(width / 2, height / 2)
        pygame.draw.circle(self.screen, "red", (int(self.player_position.x), int(self.player_position.y)), 40)
        
    def createPlayerControls(self):
        if self.screen is None:
            return
        pressed_keys = self.pygame.key.get_pressed()
        if pressed_keys[self.pygame.K_w]:
            self.player_position.y -= 300 * self.delta_time
        if pressed_keys[self.pygame.K_s]:
            self.player_position.y += 300 * self.delta_time
        if pressed_keys[self.pygame.K_a]:
            self.player_position.x -= 300 * self.delta_time
        if pressed_keys[self.pygame.K_d]:
            self.player_position.x += 300 * self.delta_time
    
    def checkQuitGame(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.running = False


game = Game(60, pygame.time.Clock())
game.initGame()

