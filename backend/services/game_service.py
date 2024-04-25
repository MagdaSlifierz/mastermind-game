import random

from sqlalchemy.orm import Session

from clients.random_client import RandomClient
from models.attempt import Attempt
from models.difficulty import Difficulty
from models.game import Game
from schemas.attempt_schema import AttemptSchema, CreateAttemptSchema
from schemas.game_schema import GameSchema, CreateGameSchema
from schemas.hints_schema import HintSchema


def create_frequency_map(items: str) -> dict[chr, int]:
    """ Create frequency map. """
    frequency_map = {}
    for item in items:
        if item in frequency_map:
            frequency_map[item] += 1
        else:
            frequency_map[item] = 1
    return frequency_map


def compare_secret_code_to_user_guess(secret_code: str, user_guess: str) -> tuple[int, int]:
    """ Create feedback. """
    secret_code_frequency_map = create_frequency_map(secret_code)

    correct_number = 0
    correct_place = 0

    for i in range(len(user_guess)):
        number = user_guess[i]
        if number in secret_code_frequency_map and secret_code_frequency_map[number] > 0:
            correct_number += 1
            secret_code_frequency_map[number] -= 1

        if number == secret_code[i]:
            correct_place += 1

    return correct_number, correct_place


def create_feedback(secret_code: str, user_guess: str) -> str:
    """ Create feedback. """
    correct_number, correct_place = compare_secret_code_to_user_guess(secret_code, user_guess)
    if correct_number == len(secret_code) and correct_place == len(secret_code):
        return "You won!"
    if correct_number == 0 and correct_place == 0:
        return "No correct number(s), no correct place(s)"
    return f"{correct_number} correct number(s), {correct_place} correct place(s)"


def game_is_over(status: str) -> bool:
    """ Check if game is over. """
    return status == "won" or status == "lost"


class GameService:

    def __init__(self, db: Session):
        self.db = db

    def save_game(self, game: CreateGameSchema) -> GameSchema:
        """ Save a game. """
        new_game = Game(**game.dict())
        if not new_game.is_multiplayer:
            difficulty = self.db.query(Difficulty).filter(Difficulty.id == new_game.difficulty_id).first()
            new_game.secret_code = RandomClient().generate_secret_code(
                difficulty.code_length,
                difficulty.minimum_number,
                difficulty.maximum_number,
                difficulty.is_duplicate_allowed)
            new_game.hints = '-' * len(new_game.secret_code)
        self.db.add(new_game)
        self.db.commit()
        self.db.refresh(new_game)
        return new_game

    def get_game_hints(self, game_id: int) -> HintSchema:
        """ Get hints by game id. """
        db_game = self.db.query(Game).filter(Game.id == game_id).first()
        if not db_game:
            raise ValueError("Game not found")

        db_difficulty = db_game.difficulty
        if len(db_game.attempts) == db_difficulty.max_attempts:
            raise ValueError("No more hints available")

        if '-' not in db_game.hints:
            raise ValueError("All hints have been provided")

        available_indices = [i for i, hint in enumerate(db_game.hints) if hint == '-']
        index = random.choice(available_indices)
        hint_list = list(db_game.hints)
        hint_list[index] = db_game.secret_code[index]
        db_game.hints = ''.join(hint_list)
        self.db.commit()
        return db_game

    def find_all_games(self) -> list[GameSchema]:
        """ Find all games. """
        return self.db.query(Game).all()

    def find_game_by_id(self, game_id: int) -> GameSchema:
        """ Find a game by id. """
        return self.db.query(Game).filter(Game.id == game_id).first()

    def save_attempt_to_game(self, game_id: int, attempt: CreateAttemptSchema) -> AttemptSchema:
        """ Save an attempt to a game. """
        db_game = self.db.query(Game).filter(Game.id == game_id).first()
        db_difficulty = db_game.difficulty

        if len(db_game.attempts) > db_difficulty.max_attempts:
            raise ValueError("Game is over")

        feedback = create_feedback(db_game.secret_code, attempt.guess)
        if feedback == "You won!":
            db_game.status = "won"
        elif len(db_game.attempts) + 1 == db_difficulty.max_attempts:
            db_game.status = "lost"

        new_attempt = Attempt(**attempt.dict())
        new_attempt.number_of_attempts = len(db_game.attempts) + 1
        new_attempt.feedback = feedback
        self.db.add(new_attempt)
        self.db.commit()
        self.db.refresh(db_game)
        self.db.refresh(new_attempt)
        return new_attempt

    def find_all_attempts_by_game_id(self, game_id: int) -> list[AttemptSchema]:
        """ Find all attempts by game id. """
        return self.db.query(Attempt).filter(Attempt.game_id == game_id).all()
