from pydantic import BaseModel, ValidationError


class User(BaseModel):
    age: int | None
    name = 'Frlix D. Tran'


try:
    user = User(age=100)
    print(user)
except (ValidationError, TypeError) as error:
    print('Something went wrong!')
    if isinstance(error, TypeError):
        print(error)
    else:
        print(error.json())


# assert user.id == 123
# assert user_x.id == 123
# assert isinstance(user_x.id, int)
