#!/usr/bin/env python3
"""
Main game file for the 2D Arcade Game Development Project.
This is the entry point for our game.
"""

import arcade

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Two Player Arcade Game"

class MyGame(arcade.Window):
    """
    Main application class for our game.
    """
    
    def __init__(self):
        """Initialize the game."""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # Initialize game variables
        self.player1_sprite = None
        self.player2_sprite = None
        self.player1_list = None
        self.player2_list = None
        
        # Track pressed keys
        self.pressed_keys = set()
        
        # Game state
        self.score = 0
        self.game_over = False
        
    def setup(self):
        """Set up the game variables. Call this function to restart the game."""
        # Create sprite lists
        self.player1_list = arcade.SpriteList()
        self.player2_list = arcade.SpriteList()
        
        # Set up player 1 (WASD controls)
        self.player1_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.5)
        self.player1_sprite.center_x = SCREEN_WIDTH // 4
        self.player1_sprite.center_y = SCREEN_HEIGHT // 2
        self.player1_list.append(self.player1_sprite)
        
        # Set up player 2 (Arrow keys)
        self.player2_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png", 0.5)
        self.player2_sprite.center_x = 3 * SCREEN_WIDTH // 4
        self.player2_sprite.center_y = SCREEN_HEIGHT // 2
        self.player2_list.append(self.player2_sprite)
        
        # Reset game state
        self.score = 0
        self.game_over = False
        self.pressed_keys.clear()
        
    def on_draw(self):
        """Render the screen."""
        # Clear the screen
        self.clear()
        
        # Draw all sprites
        self.player1_list.draw()
        self.player2_list.draw()
        
        # Draw the score
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.color.BLACK, 24)
        
        # Draw player labels
        arcade.draw_text("Player 1 (WASD)", 10, SCREEN_HEIGHT - 60, arcade.color.BLACK, 16)
        arcade.draw_text("Player 2 (Arrow Keys)", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 16)
        
    def on_update(self, delta_time):
        """Movement and game logic."""
        # Update player 1 movement based on pressed keys
        self.player1_sprite.change_x = 0
        self.player1_sprite.change_y = 0
        
        if arcade.key.A in self.pressed_keys:
            self.player1_sprite.change_x -= 5
        if arcade.key.D in self.pressed_keys:
            self.player1_sprite.change_x += 5
        if arcade.key.W in self.pressed_keys:
            self.player1_sprite.change_y += 5
        if arcade.key.S in self.pressed_keys:
            self.player1_sprite.change_y -= 5
            
        # Update player 2 movement based on pressed keys
        self.player2_sprite.change_x = 0
        self.player2_sprite.change_y = 0
        
        if arcade.key.LEFT in self.pressed_keys:
            self.player2_sprite.change_x -= 5
        if arcade.key.RIGHT in self.pressed_keys:
            self.player2_sprite.change_x += 5
        if arcade.key.UP in self.pressed_keys:
            self.player2_sprite.change_y += 5
        if arcade.key.DOWN in self.pressed_keys:
            self.player2_sprite.change_y -= 5
        
        # Update all sprites
        self.player1_list.update()
        self.player2_list.update()
        
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        # Add the key to the set of pressed keys
        self.pressed_keys.add(key)
            
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        # Remove the key from the set of pressed keys
        self.pressed_keys.discard(key)

def main():
    """Main function to run the game."""
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main() 