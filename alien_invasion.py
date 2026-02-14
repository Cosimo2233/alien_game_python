import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        #设置背景色
        self.bg_color=(self.settings.bg_color)

    def run_game(self):
        """开始游戏主循环"""
        while True:          
            self._check_event()
            self.ship.update()
            self._update_screen()
            self.clock.tick(90)
        
    def _check_event(self):
        """响应鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key ==pygame.K_d:
                    self.ship.moving_right=True
            elif event.type==pygame.KEYUP:
                if event.key ==pygame.K_d:
                    self.ship.moving_right=False

    def _update_screen(self):
        """更新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        pygame.display.flip()

if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()
