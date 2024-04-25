import {z} from "zod";


/** Create game schema. */
const CreateGameSchema = z.object({
    difficultyId: z.number(),
    isMultiplayer: z.boolean()
});

/** REST API create game schema. */
const ApiCreateGameSchema = CreateGameSchema.transform((data) => ({
    difficulty_id: data.difficultyId,
    is_multiplayer: data.isMultiplayer
}));


/** Create game type. */
export type CreateGameType = z.infer<typeof CreateGameSchema>;

export default ApiCreateGameSchema;