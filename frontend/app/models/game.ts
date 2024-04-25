import {z} from "zod";

/** REST API Game schema. */
const ApiGameSchema = z.object({
    id: z.number(),
    difficulty_id: z.number(),
    is_multiplayer: z.boolean(),
    status: z.enum(['in_progress', 'won', 'lost']),
});

/** Game schema. */
const GameSchema = ApiGameSchema.transform((data) => ({
    id: data.id,
    difficultyId: data.difficulty_id,
    isMultiplayer: data.is_multiplayer,
    status: data.status
}));

/** Game type. */
export type GameType = z.infer<typeof GameSchema>;

export default GameSchema;