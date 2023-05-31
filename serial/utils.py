"""Helper utils for datetime (de)serialization. You should not need to modify anything here."""

import datetime
import json
from typing import Any, Dict


class JSONDatetimeEncoder(json.JSONEncoder):
    """JSON encoder for datetime, date"""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)


def json_deserial_hook_datetime(pairs: Dict[Any, Any]) -> Dict[Any, Any]:
    """JSON deserialization hook for datetime fields"""
    parsed = dict()
    for key, val in pairs:
        if isinstance(val, str):
            try:
                parsed[key] = datetime.datetime.fromisoformat(val)
            except ValueError:
                parsed[key] = val  # type: ignore
    return parsed
