from fastapi import FastAPI
from models import PlayerAction, GameState
from game_logic import Game

app = FastAPI()
game = Game()

@app.post("/start")
def start_game():
    global game
    game = Game()
    return {"message": "Juego iniciado.", "player_hp": 100, "enemy_hp": 100}

@app.post("/action")
def do_action(action: PlayerAction):
    msg = game.player_action(action.action)
    return {
        "player_hp": game.player_hp,
        "enemy_hp": game.enemy_hp,
        "turn": game.turn,
        "message": msg
    }

@app.get("/status")
def status():
    return {
        "player_hp": game.player_hp,
        "enemy_hp": game.enemy_hp,
        "turn": game.turn
    }
