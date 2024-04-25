import {DifficultyType} from "~/models/difficulty";


type StartGameProps = {
    difficulties: DifficultyType[]
}

const StartGame: React.FC<StartGameProps> = ({difficulties}) => {
    return (
        <div>
            {difficulties.map((difficulty) => (
                <div key={difficulty.id} className="p-4 max-w-sm mx-auto bg-white rounded-xl shadow-md">
                    <div className="text-center">
                        <div className="text-2xl font-bold">Guess the {difficulty.codeLength} Digit Number Combination</div>
                        <div className="text-gray-500">{difficulty.isDuplicateAllowed ? 'Yes' : 'No'} duplicate numbers, only includes {difficulty.minimumNumber} - {difficulty.maximumNumber}</div>
                    </div>
                </div>
            ))}
        </div>
    );
};