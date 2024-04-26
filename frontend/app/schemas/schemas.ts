import {z} from "zod";

export const APiDifficultySchema = z.object({
    id: z.number(),
    name: z.string(),
    label: z.string(),
    max_attempts: z.number().min(1),
    code_length: z.number().min(1),
    is_duplicate_allowed: z.boolean()
});

export const DifficultySchema = APiDifficultySchema.transform((data) => ({
    id: data.id,
    name: data.name,
    label: data.label,
    maxAttempts: data.max_attempts,
    codeLength: data.code_length,
    isDuplicateAllowed: data.is_duplicate_allowed
}));

export const DifficultyListSchema = z.array(DifficultySchema);

export const ApiCreateGameSchema = z.object({
    difficulty_id: z.number().gte(1),
    is_multiplayer: z.boolean().default(false)
});

export const ApiGameSchema = z.object({
    id: z.number(),
    difficulty_id: z.number(),
    status: z.enum(['in_progress', 'won', 'lost']).default('in_progress'),
    is_multiplayer: z.boolean().default(false),
});

export const GameSchema = ApiGameSchema.transform((data) => ({
    id: data.id,
    difficultyId: data.difficulty_id,
    status: data.status,
    isMultiplayer: data.is_multiplayer,
}));

export const ApiCreateAttemptSchema = z.object({
    game_id: z.number().gte(1),
    guess: z.string().max(4),
});

export const ApiAttemptSchema = z.object({
    id: z.number().gte(1),
    game_id: z.number().gte(1),
    number_of_attempts: z.number().gte(1),
    guess: z.string().max(4),
    feedback: z.string()
});

export const AttemptSchema = ApiAttemptSchema.transform((data) => ({
    id: data.id,
    gameId: data.game_id,
    numberOfAttempts: data.number_of_attempts,
    guess: data.guess,
    feedback: data.feedback
}));

export const AttemptListSchema = z.array(AttemptSchema);


export const GameWithAttemptsSchema = z.object({
    game: GameSchema,
    attempts: AttemptListSchema
});
