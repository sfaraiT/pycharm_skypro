from datetime import datetime
from typing import Any, Dict, List

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """Function input list dict and key state."""
    filtered_data = [{"id": i["id"], "state": i["state"], "date": i["date"]} for i in data if i["state"] == state]
    return filtered_data


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Function input list dict and output new list dict"""
    return sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)


# print(filter_by_state((data)))
# print(sort_by_date((data)))
