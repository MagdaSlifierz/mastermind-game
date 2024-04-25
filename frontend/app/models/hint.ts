import {z} from "zod";

/** REST API Hint schema. */
const ApiHintSchema = z.object({
    hints: z.string()
});

/** Hint schema. */
const HintSchema = ApiHintSchema.transform((data) => ({
    hints: data.hints
}));

/** Hint type. */
export type HintType = z.infer<typeof HintSchema>;

export default HintSchema;