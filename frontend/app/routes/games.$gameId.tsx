import {json, LoaderFunction, LoaderFunctionArgs} from "@remix-run/node";
import {GameApiService} from "~/services/gameService";
import {GameType} from "~/models/game";
import {useLoaderData} from "react-router";
import ListAttempt from "~/components/ListAttempt";
import CreateAttempt from "~/components/CreateAttempt";
import {DifficultyService} from "~/services/difficultyService";
import React, {useState} from "react";
import {useNavigate} from "@remix-run/react";
import Difficulty from "~/components/Difficulty";
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faVolumeLow} from '@fortawesome/free-solid-svg-icons';
import {faHandHoldingMedical} from '@fortawesome/free-solid-svg-icons';
import {HintType} from "~/models/hint";

export const loader: LoaderFunction = async ({params}: LoaderFunctionArgs) => {
    const gameService = new GameApiService();
    const {gameId} = params;
    const game = await gameService.getGame(Number(gameId));
    if (!game) {
        throw new Response('Game not found', {status: 404});
    }

    const difficultyService = new DifficultyService();
    const difficulty = await difficultyService.getDifficulty(game.difficultyId);

    const attempts = await gameService.getAllAttemptsByGameId(Number(gameId));

    return {
        ...game,
        difficulty,
        attempts
    };
}

export default function GameRoute() {
    const data = useLoaderData();

    const [guess, setGuess] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const gameApiService = new GameApiService();
        await gameApiService.createAttemptForGame(data.id, {
            gameId: data.id,
            guess: guess
        });
        setGuess('');
        navigate(`/games/${data.id}`);
    };


    const [hint, setHint] = useState('');
    const handleHintSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const gameApiService = new GameApiService();
        await gameApiService.getGameHints(data.id).then((hint: HintType) => {
            setHint(hint.hints);
        });
    };


    return (
        <div className="container mx-auto p-4">
            <Difficulty difficulty={data.difficulty}/>
            <div className="max-w-md mx-auto mt-10">
                <h2 className="text-xl font-bold">Attempts</h2>
                <div className="space-y-4">
                    {data.attempts.sort((a, b) => a.numberOfAttempts - b.numberOfAttempts).map((attempt) => (
                        <div key={attempt.id} className="flex justify-between">
                            <div>{attempt.guess}</div>
                            <div>{attempt.feedback}</div>
                            <div>
                                <FontAwesomeIcon icon={faVolumeLow} onClick={() => {
                                    const utterance = new SpeechSynthesisUtterance(attempt.feedback);
                                    speechSynthesis.speak(utterance);
                                }}/>
                            </div>
                            <div>
                                <FontAwesomeIcon icon={faHandHoldingMedical} onClick={(event)=>handleHintSubmit(event)} />
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            Left attempts: {data.difficulty.maxAttempts - data.attempts.length}, Hint: {hint}

            <form onSubmit={handleSubmit} className="flex flex-col space-y-4">
                <input
                    type="text"
                    value={guess}
                    onChange={(e) => setGuess(e.target.value)}
                    className="p-2 border-2 border-gray-300"
                    placeholder={`Enter a ${data.difficulty.codeLength} number guess`}
                    maxLength={data.difficulty.codeLength}
                />
                <button
                    type="submit"
                    className={`bg-blue-500 text-white p-2 rounded ${data.difficulty.maxAttempts - data.attempts.length <= 0 ? 'bg-gray-500' : ''}`}
                    disabled={(data.difficulty.maxAttempts - data.attempts.length) <= 0 || ['won', 'lost'].includes(data.status)}
                >
                    {data.status === 'won' ? 'You won!' : (data.status === 'lost' ? 'You lost!' : 'Try to guess the number!')}
                </button>
            </form>
        </div>
    );
}
