import React from "react";
import {AttemptType} from "~/models/attempt";

type AttemptProps = {
    attempt: AttemptType
}

const Attempt: React.FC<AttemptProps> = ({attempt}) => {
    return (
        <div className="flex justify-between">
            <div>{attempt.numberOfAttempts}</div>
            <div>{attempt.guess}</div>
            <div>{attempt.feedback}</div>
            <div>
                <button onClick={() => {
                    const utterance = new SpeechSynthesisUtterance(attempt.feedback);
                    speechSynthesis.speak(utterance);
                }}>Speak
                </button>
            </div>
        </div>
    );
};

export default Attempt;