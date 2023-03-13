class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (12, 27, 47)

        # Ship settings.
        self.ship_speed = 3
        self.ship_limit = 2

        # Bullet_settings
        self.bullet_speed = 5.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 2.4
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1