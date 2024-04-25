import React from "react";
import {DifficultyType} from "~/models/difficulty";

type DifficultyProps = {
    difficulty: DifficultyType
}

const Difficulty: React.FC<DifficultyProps> = ({difficulty}) => {
    return (
        <div className="p-4 max-w-sm mx-auto bg-white rounded-xl shadow-md">
            <div className="text-center">
                <div className="text-2xl font-bold">Guess the {difficulty.codeLength} Digit Number Combination</div>
                <div className="text-gray-500">{difficulty.isDuplicateAllowed ? 'Yes' : 'No'} duplicate numbers, only includes {difficulty.minimumNumber} - {difficulty.maximumNumber}</div>
            </div>
        </div>
    );
};

export default Difficulty;
