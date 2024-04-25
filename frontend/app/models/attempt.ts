import {z} from "zod";

/** REST API Attempt schema. */
const ApiAttemptSchema = z.object({
    id: z.number(),
    game_id: z.number(),
    number_of_attempts: z.number(),
    guess: z.string(),
    feedback: z.string()
});

/** Attempt schema. */
const AttemptSchema = ApiAttemptSchema.transform((data) => ({
    id: data.id,
    gameId: data.game_id,
    numberOfAttempts: data.number_of_attempts,
    guess: data.guess,
    feedback: data.feedback
}));

/** Attempt list schema. */
export const AttemptListSchema = z.array(AttemptSchema);

/** Attempt type. */
export type AttemptType = z.infer<typeof AttemptSchema>;

/** Attempt list type. */
export type AttemptListType = z.infer<typeof AttemptListSchema>;

export default AttemptSchema;