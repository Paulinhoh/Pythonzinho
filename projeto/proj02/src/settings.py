class Settings():
    """Uma classe para armazenar todas as configurações da Alien Invasion."""
    
    def __init__(self):
        """Inicializa as configurações do jogo."""
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        
        # Configurações dos projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
