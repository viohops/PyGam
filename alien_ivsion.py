import sys
import pygame
from settings import Settings 
from ship import Ship

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_widh, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
       
        
    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()
            
            
    def _check_events(self):
        """Обробатывает нажатие клавишь и события мыши"""
        #Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        #При каждом проходе цикла перерисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #Отображениепоследнего прорисованого экрана
        pygame.display.flip()
              
if __name__ == '__main__':
    #Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()