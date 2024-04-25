import {GameApiService} from "~/services/gameService";
import {useState} from "react";
import {DifficultyType} from "~/models/difficulty";

type CreateAttemptProps = {
    gameId: number;
    difficulty: DifficultyType
}

const CreateAttempt: React.FC<CreateAttemptProps> = ({gameId, difficulty}) => {
    const [guess, setGuess] = useState('');

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();

        const gameApiService = new GameApiService();
        await gameApiService.createAttemptForGame(gameId, {
            gameId: gameId,
            guess: guess
        });
        setGuess('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Guess"
                value={guess}
                maxLength={difficulty.codeLength}
                onChange={(event) => setGuess(event.target.value)}
            />
            <button type="submit">Submit</button>
        </form>
    );
};

export default CreateAttempt;