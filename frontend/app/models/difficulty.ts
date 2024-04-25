import {z} from "zod";

/** REST API Difficulty schema. */
const ApiDifficultySchema = z.object({
    id: z.number(),
    name: z.string(),
    label: z.string(),
    max_attempts: z.number(),
    code_length: z.number(),
    minimum_number: z.number(),
    maximum_number: z.number(),
    is_duplicate_allowed: z.boolean()
});

/** Difficulty schema. */
const DifficultySchema = ApiDifficultySchema.transform((data) => ({
    id: data.id,
    name: data.name,
    label: data.label,
    maxAttempts: data.max_attempts,
    codeLength: data.code_length,
    minimumNumber: data.minimum_number,
    maximumNumber: data.maximum_number,
    isDuplicateAllowed: data.is_duplicate_allowed
}));

/** Difficulty list schema. */
export const DifficultyListSchema = z.array(DifficultySchema);

/** Difficulty type. */
export type DifficultyType = z.infer<typeof DifficultySchema>;

/** Difficulty list type. */
export type DifficultyListType = z.infer<typeof DifficultyListSchema>;

export default DifficultySchema;