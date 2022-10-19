# fastapi-query-conditions

## Introduction
FastAPI-Query-Conditions is a dependency that parses a query string into conditions using operators enclosed in square brackets.

For example, if you send a request to `/orders?amount[gte]=1000&amount[lt]=2000`, you can use the query string as parsed conditions like this:
```json
{"gte":1000,"lt":2000}
```


## Install
```bash
> pip install fastapi-query-conditions
```

## Quick Start
```python
from typing import Dict

from fastapi import Depends, FastAPI
from fastapi_query_conditions import query_conditions

app = FastAPI()

@app.get("/items")
def query_items(amount: Dict[str, int] = Depends(query_conditions(field='amount', factory=int))):
    print(amount)
    return amount
```

Then, if you send a request to `/items?amount[gte]=1000&amount[lt]=2000`, you can check the following results.
```python
{'gte': 1000, 'lt': 2000}
```

Also, you can use various factory functions for your query parameter.
```python
from datetime import datetime
from typing import Dict

from fastapi import Depends, FastAPI
from fastapi_query_conditions import query_conditions

app = FastAPI()

@app.get("/orders")
def query_orders(time: Dict[str, int] = Depends(query_conditions(field='time', factory=datetime.fromisoformat))):
    print(time)
    return time
```

Then, if you send a request to `/orders?time[gte]=2022-10-18T12:00&time[lt]=2022-10-18T12:30`, you can check the following results.
```python
{'gte': datetime.datetime(2022, 10, 18, 12, 0), 'lt': datetime.datetime(2022, 10, 18, 12, 30)}
```