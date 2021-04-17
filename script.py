poketypes = {
    'Fire': {
        'Water': 0.5,
        'Grass': 2
    },
    'Water': {
        'Fire': 2,
        'Grass': 0.5
    },
    'Grass': {
        'Fire': 0.5,
        'Water': 2
    }

}


class Pokemon:
    knocked_out = False

    def __init__(self, name, level, poketype):
        self.name = name
        self.level = level
        self.poketype = poketype
        self.health = level

    def lose_health(self, health):
        self.health -= health
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        else:
            print(f'{self.name} now has {self.health} health.')

    def gain_health(self, health):
        self.health += health
        if self.health > self.level:
            self.health = self.level
        if self.knocked_out:
            self.revive()
        else:
            print(f'{self.name} now has {self.health} health.')

    def revive(self):
        print(f'{self.name} has been revived with {self.health} health.')
        self.knocked_out = False

    def knock_out(self):
        print(f'{self.name} is knocked out.')
        self.knocked_out = True

    def attack(self, other):
        multiplier = poketypes[self.poketype][other.poketype]
        attack = 1 * multiplier
        print(f'{self.name} attacked {other.name} with {attack}.')
        if multiplier == 0.5:
            print("It's not very effective.")
        elif multiplier == 2:
            print("It's super effective.")
        other.lose_health(attack)

    def __repr__(self):
        return f'{self.name}'


class Trainer:
    def __init__(self, name, pokemons, total_potions):
        self.name = name
        self.pokemons = pokemons[:6] if len(pokemons) > 6 else pokemons
        self.pokemon = self.pokemons[0]
        self.total_potions = total_potions

    def attack(self, other):
        if self.pokemon.knocked_out == False:
            self.pokemon.attack(other.pokemon)
        else:
            print(f'{self.pokemon.name} is knocked out, choose another pokemon {self.name}.')

    def use_potion(self):
        if self.total_potions > 0:
            print(f'{self.name} used potion on {self.pokemon.name}')
            self.pokemon.gain_health(5)
            self.total_potions -= 1
        else:
            print(f"{self.name} cannot use potion, There's no more.")

    def swap_pokemon(self, number):
        if self.pokemons[number] == self.pokemon:
            print(f'{self.name} cannot swap out active pokemon with active pokemon.')
        elif not self.pokemons[number].knocked_out:
            print(f'{self.name} swapped out {self.pokemon} with {self.pokemons[number]}')
            self.pokemon = self.pokemons[number]
        else:
            print(f'{self.pokemons[number]} is knocked out. Choose another pokemon, {self.name}.')

    def __repr__(self):
        print(f'{self.name} currently has the following pokemons:')
        for pokemon in self.pokemons:
            print(pokemon)
        return f'Current pokemon: {self.pokemon}'


class FireType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, 'Fire')


class GrassType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, 'Grass')


class WaterType(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, 'Water')


Venusaur = GrassType('Venusaur', 5)
Charizard = FireType('Charizard', 5)
Blastoise = WaterType('Blastoise', 5)

Ash = Trainer('Ash Kectup', [Venusaur, Charizard, Blastoise], 0)

User = Trainer('THE USER', [FireType(f'Houndour {x}', 100) for x in range(5)], 1000)

print(Ash)
print(User)

Ash.attack(User)
User.attack(Ash)
User.use_potion()
Ash.attack(User)
User.swap_pokemon(0)
User.swap_pokemon(1)
