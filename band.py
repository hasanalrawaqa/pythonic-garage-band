class MusicalInstrument:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def __str__(self):
        return f"{self.name}"


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = MusicalInstrument(instrument)

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument.name.lower()}"

    def get_instrument(self):
        return self.instrument.name.lower()

    def play_solo(self):
        if self.instrument.name.lower() == "guitar":
            return "face melting guitar solo"
        elif self.instrument.name.lower() == "bass":
            return "bom bom buh bom"
        elif self.instrument.name.lower() == "drums":
            return "rattle boom crash"



class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar")


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")


class Band:
    instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members if members else []
        Band.instances.append(self)

    def __str__(self):
        return f"{self.name} band"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def add_member(self, member):
        self.members.append(member)

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances

    @classmethod
    def create_band(cls, name):
        band = cls(name)
        band.add_member(Guitarist("Kurt Cobain"))
        band.add_member(Bassist("Krist Novoselic"))
        band.add_member(Drummer("Dave Grohl"))
        return band
