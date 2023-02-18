from pydantic import BaseModel, Extra, validator
from enum import Enum
from typing import List, Tuple


def snake_to_camel_case(value: str) -> str:
    if not isinstance(value, str):
        raise ValueError('Value must be a string!')
    words = value.split('_')
    value = ''.join(word.title() for word in words if word)
    return f'{value[0].lower()}{value[1:]}'


class CustomBaseModel(BaseModel):
    class Config:
        alias_generator = snake_to_camel_case
        extra = Extra.forbid
        allow_population_by_field_name = True


class PolygonType(Enum):
    triangle = 3


class PolygonModel(CustomBaseModel):
    polygon_type: PolygonType
    vertices: List[Tuple[int | float, int | float]]

    @validator('vertices')
    def validate_vertices(cls, value, values):
        polygon_type = values.get('polygon_type')
        if polygon_type:
            num_vertices_required = polygon_type.value
            if len(value) != num_vertices_required:
                raise ValueError
        return value


print(PolygonModel(polygon_type=3,
      vertices=[(1, 1), (1, 1), (1, 1)]))


t = PolygonType(3)
print(t)
