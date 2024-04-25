import dotenv from 'dotenv';

dotenv.config();

/** Configuration object. */
export const config = {
    apiBaseURL: process.env.API_BASE_URL || 'http://localhost:8000', // Default URL in case the environment variable is not set.
}
