import DifficultySchema, {DifficultyListSchema, DifficultyType} from "~/models/difficulty";
import {config} from "~/config";

const API_BASE_URL = 'http://localhost:8000';

/** Difficulty service. */
export class DifficultyService {

    /** Get all difficulties. */
    async getDifficulties(): Promise<DifficultyType[]> {
        const response = await fetch(`${API_BASE_URL}/difficulties`);
        return DifficultyListSchema.parse(await response.json());
    }

    /** Get a difficulty by ID. */
    async getDifficulty(difficultyId: number): Promise<DifficultyType> {
        const response = await fetch(`${API_BASE_URL}/difficulties/${difficultyId}`);
        return DifficultySchema.parse(await response.json());
    }
}
