import {json, LoaderFunction} from "@remix-run/node";
import {DifficultyService} from "~/services/difficultyService";


/** Get all difficulties. */
export const loader: LoaderFunction = async () => {
    const difficultYService = new DifficultyService();
    return json(await difficultYService.getDifficulties());
};
