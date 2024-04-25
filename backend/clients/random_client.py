import requests


class RandomClient:
    """ Random.org API client."""

    def generate_secret_code(self, code_length: int = 4, digit_min: int = 0, digit_max: int = 7,
                             is_duplicate_allowed: bool = True) -> str:
        """ Generate a secret code. """

        try:
            url = f"https://www.random.org/integers/?num={code_length}&min={digit_min}&max={digit_max}&col=1&base=10&format=plain&rnd=new"
            if not is_duplicate_allowed:
                url = f"https://www.random.org/sequences/?min={digit_min}&max={digit_max}&col=1&format=plain&rnd=new"

            response = requests.get(url)
            response.raise_for_status()
            secret_code = response.text.strip().replace("\n", "")

            if not is_duplicate_allowed:
                secret_code = secret_code[:-(len(secret_code) - code_length)]

            return secret_code
        except requests.exceptions.HTTPError as e:
            raise Exception(f"Error: {e}")
        except requests.exceptions.ConnectionError as e:
            raise Exception(f"Error: {e}")
        except requests.exceptions.Timeout as e:
            raise Exception(f"Error: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error: {e}")
