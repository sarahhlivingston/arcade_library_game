"""
Player module for the 2D game.
Contains player character logic and behavior.
"""

import arcade

class Player(arcade.Sprite):
    """
    Player character class.
    """
    
    def __init__(self, x, y):
        """Initialize the player."""
        super().__init__(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.center_x = x
        self.center_y = y
        
        # Player stats
        self.health = 100
        self.max_health = 100
        self.speed = 5
        
        # Movement state
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Update player position and state."""
        # Update position based on movement state
        if self.moving_left:
            self.change_x = -self.speed
        elif self.moving_right:
            self.change_x = self.speed
        else:
            self.change_x = 0
            
        if self.moving_up:
            self.change_y = self.speed
        elif self.moving_down:
            self.change_y = -self.speed
        else:
            self.change_y = 0
            
        # Call parent update
        super().update()
        
    def take_damage(self, amount):
        """Player takes damage."""
        self.health -= amount
        if self.health < 0:
            self.health = 0
            
    def heal(self, amount):
        """Player heals."""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
            
    def is_alive(self):
        """Check if player is alive."""
        return self.health > 0 