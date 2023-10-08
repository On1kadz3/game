class Entity:
    def __init__(self, name, healthpoints, damage, armor, attack_range, movement_speed, vision_distance):
        self.name = name
        self.healthpoints = healthpoints
        self.damage = damage
        self.armor = armor
        self.attack_range = attack_range
        self.movement_speed = movement_speed
        self.vision_distance = vision_distance
