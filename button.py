import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """ Initialize button attribute. """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 400, 80
        self.button_color = (42, 72, 102)
        self.text_color = (255, 155, 235)
        self.font = pygame.font.Font("gameFont.ttf", 38)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y += 100  # Add this line to lower the position by 40 pixels

        # The button messege needs to be prepared only once.
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """ Turn msg into a rendered image and center text on yhe button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        