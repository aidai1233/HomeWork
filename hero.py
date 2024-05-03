class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def __str__(self):
        return (f' Name: {self.name}\n '
                f'Nickname: {self.nickname}\n '
                f'Superpower: {self.superpower}\n '
                f'HP: {self.health_points}\n'
                f' Catchphrase: {self.catchphrase} ')

    def health_points1(self):
        self.health_points = int(self.health_points) ** 2
        return self.health_points

    def __repr__(self):
        return (f'nickname: {self.nickname}\n '
                f'superpower: {self.superpower}\n '
                f'HP: {self.health_points}\n')

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Панда', 'Воин дракона', 'Побеждать', '100', 'скдш')

print(f'{hero} \n'
      f'длина коронной фразы героя: {len(hero)}\n'
      f'HP^2: {hero.health_points1()}')

class Crane(SuperHero):
    territory = 'sky'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def __str__(self):
        return (super().__str__() +
                f'\n Damage: {self.damage}\n '
                f' HP^2: {self.health_points1()}')

    def health_points1(self):
        self.health_points = int(self.health_points) ** 2
        self.fly = True
        return self.health_points

    def true_in_true_phrase(self):
        print('True in the True phrase')


class Snake(SuperHero):
    territory = 'earth'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def __str__(self):
        return (super().__str__() +
                f'\n Damage: {self.damage}\n'
                f' HP^2: {self.health_points1()}')

    def health_points1(self):
        self.health_points = int(self.health_points) ** 2
        self.fly = True
        return self.health_points

    def true_in_true_phrase(self):
        print('True in the True phrase')


class Villain(Crane):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)

    def gen_x(self):
        pass

    def crit(self):
        self.damage = int(self.damage) ** 2
        return self.damage



hero2 = Snake('Гадюка', 'Змеиный мастер', 'Ядовитые укусы', '100', 'шшш', '50')
print(f'\n {hero2}')
hero2.true_in_true_phrase()

hero1 = Crane('Журавль', 'Небесный воин', 'Летать', '100', 'кря-кря', '25')
print(f'\n {hero1}')
hero1.true_in_true_phrase()

hero3 = Villain('Кай', 'помощник Угвея', 'Силовые камни', 90, 'Я - непобедимый!', 50)
print(f'\n {hero3}')
print(f'Урон до критического: {hero3.damage}')
hero3.crit()
print(f'Урон после критического: {hero3.damage}')

