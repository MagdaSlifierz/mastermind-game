import {z} from "zod";

/** Create attempt schema. */
const CreateAttemptSchema = z.object({
    gameId: z.number(),
    guess: z.string()
});

/** REST API create attempt schema. */
const ApiCreateAttemptSchema = CreateAttemptSchema.transform((data) => ({
    game_id: data.gameId,
    guess: data.guess
}));

/** Create attempt type. */
export type CreateAttemptType = z.infer<typeof CreateAttemptSchema>;

export default ApiCreateAttemptSchema;
