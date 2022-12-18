import re
from typing import Any, Callable, Tuple

from fastapi import HTTPException, Request

__version__ = "1.0.2"


def _parse_key_operator(key: str) -> Tuple[str, str]:
    match = re.match(r"([^\[]+)(?:\[([^\]]+)\])?", key)
    key, operator = match.groups()

    if operator is None:
        operator = "eq"

    return key, operator


def query_conditions(field: str, factory: Callable[[str], Any]):
    def inner(request: Request):
        conditions = {}
        for key_operator, value in request.query_params.items():
            key, operator = _parse_key_operator(key_operator)
            if key != field:
                continue

            try:
                conditions[operator] = factory(value)
            except ValueError as exception:
                raise HTTPException(status_code=400, detail=str(exception))

        return conditions

    return inner
