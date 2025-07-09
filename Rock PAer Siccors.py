import pygame
import random

class Button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

class RpsGame():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        # Load your images here, make sure these files exist in your working dir!
        self.bg = pygame.image.load("background.jpg").convert()
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()

        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()

        self.rock_btn = Button(20, 500, 300, 140)
        self.paper_btn = Button(330, 500, 300, 140)
        self.scissors_btn = Button(640, 500, 300, 140)

        self.font = pygame.font.Font('Splatvh.ttf', 90)

        # Scores
        self.pl_score = 0
        self.pc_score = 0
        self.p_option = None
        self.pc_random_choice = None

        self.result_text = ""

    def draw_buttons(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))

    def display_choices(self):
        if self.p_option == "rock":
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.p_option == "paper":
            self.screen.blit(self.choose_paper, (120, 200))
        elif self.p_option == "scissors":
            self.screen.blit(self.choose_scissors, (120, 200))

        if self.pc_random_choice == "rock":
            self.screen.blit(self.choose_rock, (600, 200))
        elif self.pc_random_choice == "paper":
            self.screen.blit(self.choose_paper, (600, 200))
        elif self.pc_random_choice == "scissors":
            self.screen.blit(self.choose_scissors, (600, 200))

    def player_choice(self):
        if self.rock_btn.clicked():
            self.p_option = "rock"
        elif self.paper_btn.clicked():
            self.p_option = "paper"
        elif self.scissors_btn.clicked():
            self.p_option = "scissors"
        else:
            self.p_option = None

        return self.p_option

    def computer_choice(self):
        option = ["rock", "paper", "scissors"]
        self.pc_random_choice = random.choice(option)
        return self.pc_random_choice

    def update_score(self):
        pl = self.p_option
        pc = self.pc_random_choice
        if pl == pc:
            self.result_text = "It's a Tie!"
        elif (pl == "rock" and pc == "scissors") or \
             (pl == "paper" and pc == "rock") or \
             (pl == "scissors" and pc == "paper"):
            self.pl_score += 1
            self.result_text = "You Win!"
        else:
            self.pc_score += 1
            self.result_text = "Computer Wins!"

    def draw_score(self):
        score_text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))
        self.screen.blit(score_text, (420, 20))

        result_surface = self.font.render(self.result_text, True, (255, 255, 0))
        self.screen.blit(result_surface, (320, 100))

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            self.draw_buttons()
            self.draw_score()
            self.display_choices()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rock_btn.clicked() or self.paper_btn.clicked() or self.scissors_btn.clicked():
                        if self.player_choice():
                            self.computer_choice()
                            self.update_score()

            pygame.display.flip()
            clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = RpsGame()
    game.run()
