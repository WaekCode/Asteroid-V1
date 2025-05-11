from circleshape import CircleShape
import pygame
from shot import Shot
from constants import * 


class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    # in the player class   
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
  
    def move(self, dt):
        # Calculate movement vector
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_TURN_SPEED * dt
        # Update regular position attributes (if needed)
        self.x, self.y = self.position.x, self.position.y

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        
        # Rotation (unchanged)
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt    
        # Movement (new)
        if keys[pygame.K_w]:  # Forward
            self.move(dt)
        if keys[pygame.K_s]:  # Backward
            self.move(-dt)  # Negative dt reverses direction
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt