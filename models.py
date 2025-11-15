from pydantic import BaseModel

class PlayerAction(BaseModel):
    action: str  # attack, defend, heal

class GameState(BaseModel):
    player_hp: int
    enemy_hp: int
    turn: str
    message: str
