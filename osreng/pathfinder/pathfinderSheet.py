class PathfinderSheet:
    def __init__(self):
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10

        self.ancestry = None
        self.languages = []
        self.hit_points = 0

    @property
    def size(self):
        return self.ancestry.size

    @property
    def speed(self):
        return self.ancestry.speed

    def set_ancestry(self, ancestry):
        self.ancestry = ancestry
        self.languages += ancestry.languages
        self.hit_points = ancestry.hit_points
