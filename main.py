import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player:
    def __init__(self, delta_time: float, screen: pygame.Surface) -> None:
        self.position = pygame.Vector2(0, 0)
        self.color = pygame.Color(0, 0, 0)
        self.delta_time = delta_time
        self.screen = screen
    
    def get_position(self) -> pygame.Vector2:
        return self.position

    def init_player(self, position: pygame.Vector2, color: pygame.Color) -> None:
        pygame.draw.circle(self.screen, color, (int(position.x), int(position.y)), 40)
    
    def set_position(self, position: pygame.Vector2) -> None:
        self.position = position
    
    def set_color(self, color: pygame.Color) -> None:
        self.color = color

class Game:
    def __init__(self, frames_per_second: int, pygame = pygame) -> None:
        self.pygame = pygame
        self.frames_per_second = frames_per_second
        self.clock = pygame.time.Clock()
        self.game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.running = True
        self.time_since_last_frame = self.clock.tick(frames_per_second) / 1000.0
        self.player_position = pygame.Vector2(0, 0)
        self.current_fps = 0
        self.player = Player(self.time_since_last_frame, self.game_screen)
    
    def init_game(self) -> None:
        self.pygame.init()
        self.clock = self.pygame.time.Clock()
        self.pygame.display.set_caption("Game")
        self.game_loop()
    
    def speed_up(self) -> None:
        self.time_since_last_frame = self.clock.tick(self.frames_per_second) / 500.0
    
    def slow_motion(self) -> None:
        self.time_since_last_frame = self.clock.tick(self.frames_per_second) / 2000.0
    
    def game_loop(self) -> None:
        """
        The main game loop that runs while the game is running. It updates the clock, checks if the game should be quit,
        creates the player, and updates the display.
        """
        while self.running:
            self.clock.tick(self.frames_per_second)
            self.handle_events()
            self.move_player()
            self.draw_screen()
    
    def handle_events(self) -> None:
            """
            Handle events such as quitting the game.

            Returns:
                None
            """
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.running = False
    
    def move_player(self) -> None:
        """
        Moves the player based on the keys pressed by the user.

        The player can be moved up, down, left, or right using the W, A, S, and D keys respectively.
        The player's position is updated based on the time since the last frame and the movement speed.

        Returns:
            None
        """
        key = self.pygame.key.get_pressed()
        if key[self.pygame.K_w]:
            self.player_position.y -= 300 * self.time_since_last_frame
        if key[self.pygame.K_a]:
            self.player_position.x -= 300 * self.time_since_last_frame
        if key[self.pygame.K_s]:
            self.player_position.y += 300 * self.time_since_last_frame
        if key[self.pygame.K_d]:
            self.player_position.x += 300 * self.time_since_last_frame
        self.player.set_position(self.player_position)
    
    def draw_screen(self) -> None:
        self.game_screen.fill(self.pygame.Color(255, 255, 255))
        self.player.init_player(self.player_position, pygame.Color("red"))
        self.pygame.display.flip()


game = Game(60)
game.init_game()