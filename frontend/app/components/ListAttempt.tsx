import {AttemptType} from "~/models/attempt";
import React from "react";
import Attempt from "~/components/Attempt";

type ListAttemptProps = {
    attempts: AttemptType[]
}

const ListAttempt: React.FC<ListAttemptProps> = ({attempts}) => {
    return (
        <div>
            {attempts.sort((a, b) => a.numberOfAttempts - b.numberOfAttempts).map((attempt) => (
                <Attempt key={attempt.id} attempt={attempt}/>
            ))}
        </div>
    );
};

export default ListAttempt;

