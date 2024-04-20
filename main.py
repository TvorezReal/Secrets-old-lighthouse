import pygame
import pygame_menu

# Инициализация Pygame
pygame.init()


class StartingPage:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.menu = None
        self.title = pygame.display.set_caption("Secrets-old-lighthouse")

        # Настройки Pygame
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)  # черный цвет фона

    def start_new_game(self):
        print("Начинается новая игра...")
        # Обработка запуска новой игры

    def continue_game(self):
        print("Загрузка сохранения...")
        # Обработка загрузки игры

    def setup_menu(self):
        self.menu = pygame_menu.Menu('Разгадай Тайны старого маяка', self.width, self.height,
                                     theme=pygame_menu.themes.THEME_BLUE)

        self.menu.add.button('Начать новую игру', self.start_new_game)
        self.menu.add.button('Продолжить', self.continue_game)
        self.menu.add.button('Выход', pygame_menu.events.EXIT)

    def run(self):
        self.setup_menu()

        # Главный цикл приложения
        while self.running:
            self.screen.fill(self.bg_color)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            if self.menu:
                self.menu.update(events)
                self.menu.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()


# Запуск программы
if __name__ == "__main__":
    app = StartingPage()
    app.run()