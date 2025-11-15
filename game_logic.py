class Game:
    def __init__(self):
        self.player_hp = 100
        self.enemy_hp = 100
        self.turn = "player"

    def player_action(self, action):
        message = ""

        if action == "attack":
            self.enemy_hp -= 20
            message = "Atacaste y causaste 20 de daño."

        elif action == "defend":
            self.player_hp += 5
            message = "Te defendiste y recuperaste 5 de vida."

        elif action == "heal":
            heal_amount = 15
            self.player_hp = min(100, self.player_hp + heal_amount)
            message = f"Te curaste {heal_amount} puntos."

        else:
            message = "Acción no válida."

        # Luego juega el enemigo si sigue vivo
        if self.enemy_hp > 0:
            message += " | Turno del enemigo: "
            message += self.enemy_turn()

        # Mantener juego cíclico
        if self.player_hp <= 0:
            message += " | Perdiste. Reiniciando..."
            self.__init__()

        if self.enemy_hp <= 0:
            message += " | ¡Ganaste! Reiniciando..."
            self.__init__()

        return message

    def enemy_turn(self):
        import random
        action = random.choice(["attack", "attack", "attack", "heal"])

        if action == "attack":
            self.player_hp -= 15
            return "El enemigo te atacó y te hizo 15 de daño."
        else:
            self.enemy_hp += 10
            return "El enemigo se curó 10 puntos."
