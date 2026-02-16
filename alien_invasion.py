import sys
import pygame
from settings import Settings
from ship import Ship
from Bullet import Bullet   

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        # self.screeen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width=self.screeen.get_rect().width
        # self.settings.screen_height=self.screeen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        #设置背景色
        self.bg_color=(self.settings.bg_color)

    def run_game(self):
        """开始游戏主循环"""
        while True:          
            self._check_event()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self.clock.tick(90)
        
    def _check_event(self):
        """响应鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._event_keyup_events((event))

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        pygame.display.flip()
    
    def _check_keydown_events(self,event):
        """响应按下"""
        if event.key ==pygame.K_d:
           self.ship.moving_right=True
        elif event.key==pygame.K_a:
            self.ship.moving_left=True
        elif event.key==pygame.K_w:
            self.ship.moving_up=True
        elif event.key==pygame.K_s:
            self.ship.moving_down=True  
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组中"""
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)

    def _event_keyup_events(self,event):
        """响应释放"""
        if event.key ==pygame.K_d:
            self.ship.moving_right=False
        elif event.key ==pygame.K_a:
            self.ship.moving_left=False
        elif event.key==pygame.K_w:
            self.ship.moving_up=False
        elif event.key==pygame.K_s:
            self.ship.moving_down=False

if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()
