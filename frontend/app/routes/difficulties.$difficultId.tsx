import {useLoaderData} from "react-router";
import {DifficultyType} from "~/models/difficulty";
import Difficulty from "~/components/Difficulty";
import {json, LoaderFunction, LoaderFunctionArgs} from "@remix-run/node";
import {DifficultyService} from "~/services/difficultyService";


export const loader: LoaderFunction = async ({params}: LoaderFunctionArgs) => {
    const difficultyService = new DifficultyService();
    const {difficultId} = params;
    const difficulty = await difficultyService.getDifficulty(parseInt(difficultId));

    if (!difficulty) {
        throw new Response('Difficulty not found', {status: 404});
    }

    return json(difficulty);
}

export default function DifficultyRoute() {
    const difficulty = useLoaderData<DifficultyType>();
    return (
        <Difficulty difficulty={difficulty}/>
    );
}