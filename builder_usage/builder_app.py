import builder


class Boso510(builder.StyleStandard):
    def get_donor(self):
        self.building.donor = self.donor

    def build_engene(self):
        self.building.engene = 'sr20det'

    def put_wheels(self):
        self.building.wheels = 'Work Equip'


Dutsun510Boso = builder.BuildIt(donor='Dutsun 510', style=Boso510)

print Dutsun510Boso()