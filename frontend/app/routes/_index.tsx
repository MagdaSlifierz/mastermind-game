import {json, LoaderFunction, MetaFunction} from "@remix-run/node";
import {DifficultyService} from "~/services/difficultyService";
import {useNavigate} from '@remix-run/react';
import {useState} from "react";
import {GameType} from "~/models/game";
import {GameApiService} from "~/services/gameService";
import {useLoaderData} from "react-router";
import {DifficultyType} from "~/models/difficulty";
import Difficulty from "~/components/Difficulty";
import {useSearchParams} from "@remix-run/react";

export const meta: MetaFunction = () => {
    return [
        {title: "Start Mastermind Game"},
        {name: "description", content: "Welcome to Mastermind game!"},
    ];
};

export const loader: LoaderFunction = async ({request}) => {
    const url = new URL(request.url);
    const difficultyId = url.searchParams.get('difficultyId') || '1';
    const difficultyService = new DifficultyService();
    return json(await difficultyService.getDifficulty(parseInt(difficultyId)));
}

export default function Index() {
    const [guess, setGuess] = useState('');
    const navigate = useNavigate();

    const difficulty = useLoaderData<DifficultyType>();

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();

        const gameApiService = new GameApiService();
        gameApiService.createGame(
            {
                difficultyId: difficulty.id,
                isMultiplayer: false,
            }
        ).then((game: GameType) => {
            console.log(game.id);

            gameApiService.createAttemptForGame(game.id, {
                gameId: game.id,
                guess: guess
            }).then(() => {
                navigate(`/games/${game.id}`);
            });
        });
    };
    return (
        <div className="container mx-auto p-4">
            <Difficulty difficulty={difficulty}/>
            <div className="max-w-md mx-auto mt-10">
                <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
                    <input
                        type="text"
                        value={guess}
                        onChange={(e) => setGuess(e.target.value)}
                        className="p-2 border-2 border-gray-300"
                        placeholder={`Enter a ${difficulty.codeLength} number guess`}
                        maxLength={difficulty.codeLength}
                    />
                    <button
                        type="submit"
                        className="bg-blue-500 text-white p-2 rounded"
                    >
                        Start Game
                    </button>
                </form>
            </div>
        </div>
    );
}
