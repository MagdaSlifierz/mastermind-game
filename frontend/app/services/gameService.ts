import ApiCreateGameSchema, {CreateGameType} from "~/models/create-game";
import GameSchema, {GameType} from "~/models/game";
import AttemptSchema, {AttemptListSchema, AttemptType} from "~/models/attempt";
import ApiCreateAttemptSchema, {CreateAttemptType} from "~/models/create-attempt";
import {config} from "~/config";
import Hint, {HintType} from "~/models/hint";
import HintSchema from "~/models/hint";


const API_BASE_URL = 'http://localhost:8000';


/** Game API service. */
export class GameApiService {

    /** Create a new game. */
    async createGame(game: CreateGameType): Promise<GameType> {
        const response = await fetch(`${API_BASE_URL}/games`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                difficulty_id: game.difficultyId,
                is_multiplayer: game.isMultiplayer
            }),
        });
        return GameSchema.parse(await response.json());
    }

    /** Get a game by ID. */
    async getGame(gameId: number): Promise<GameType> {
        const response = await fetch(`${API_BASE_URL}/games/${gameId}`);
        return GameSchema.parse(await response.json());
    }

    async getGameHints(gameId: number): Promise<HintType> {
        const response = await fetch(`${API_BASE_URL}/games/${gameId}/hints`);
        return HintSchema.parse(await response.json());
    }

    /** Create a new attempt for a game by ID. */
    async createAttemptForGame(gameId: number, attempt: CreateAttemptType): Promise<AttemptType> {
        const response = await fetch(`${API_BASE_URL}/games/${gameId}/attempts`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                game_id: attempt.gameId,
                guess: attempt.guess
            }),
        });
        return AttemptSchema.parse(await response.json());
    }

    /** Get all attempts for a game by ID. */
    async getAllAttemptsByGameId(gameId: number): Promise<AttemptType[]> {
        const response = await fetch(`${API_BASE_URL}/games/${gameId}/attempts`);
        return AttemptListSchema.parse(await response.json());
    }
}
