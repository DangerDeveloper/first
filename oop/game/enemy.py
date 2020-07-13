class Enemy:

    def __init__(self, name='Enemy', hit_point=0, lives=1):
        self.name = name
        self.hit_point = hit_point
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_point - damage
        if remaining_points >= 0:
            self.hit_point = remaining_points
            print('I Took {} points damage and have {} left'.format(damage, self.hit_point))
        else:
            self.lives -= 1

    def __str__(self):
        return 'Name: {0.name}, Lives: {0.lives}, Hit Point: {0.hit_point}'.format(self)


class Troll(Enemy):
    pass
