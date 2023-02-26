class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (6, 0, 50)

        # Ship settings.
        self.ship_speed = 1.5

        # Bullet_settings
        self.bullet_speed = 2.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (180, 30, 20)