class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (12, 27, 47)

        # Ship settings.
        self.ship_limit = 2

        # Bullet_setting
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (155, 185, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.2

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 4
        self.alien_speed = 2
        self.background_speed = 4

         # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase speed settings and aline point value."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.background_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)