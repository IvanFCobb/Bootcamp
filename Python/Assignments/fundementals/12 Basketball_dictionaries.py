players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33, "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32, "position": "Power Foward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age": 32, "position": "Point Guard",
    "team": "Brooklyn Nets"
}


class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    def display_player_name(self):
        print(self.name)

    def __repr__(self):
        display = f"Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team}"
        return display


player_kevin = Player(kevin)

player_jason = Player(jason)

player_kyrie = Player(kyrie)

player_kevin.display_player_name()
player_jason.display_player_name()
player_kyrie.display_player_name()

new_team = []

for player_dictionary in players:
    player = Player(player_dictionary)
    new_team.append(player)

print(new_team)
