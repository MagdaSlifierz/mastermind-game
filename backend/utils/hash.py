from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """Hash class to hash and verify passwords."""

    @staticmethod
    def create_access_token(data: dict) -> str:
        """Create an access token."""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, "secret", algorithm="HS256")
        return encoded_jwt

    @staticmethod
    def verify_token(token: str, credentials_exception) -> dict:
        """Verify the token."""
        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            return {"data": {"username": username}}
        except JWTError:
            raise credentials_exception

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash the password."""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify the password."""
        return pwd_context.verify(plain_password, hashed_password)
