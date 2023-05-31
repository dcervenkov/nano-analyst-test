import datetime
import dataclasses
import json
from typing import Any

import pytest

from .datamodels import ServiceRequest
from .utils import JSONDatetimeEncoder, json_deserial_hook_datetime


@pytest.mark.parametrize(
    "obj",
    [
        ServiceRequest(
            model_prefix="wind_production_859182400707971783",
            country="CZ",
            datetime_from=datetime.datetime(2023, 4, 1),
            datetime_to=datetime.datetime(2023, 5, 1),
            freq="H",
        ),
    ],
)
def test_serial(obj: Any) -> None:
    """Verify that (de)serialization works for objects with datetime fields."""
    serialized = JSONDatetimeEncoder().encode(dataclasses.asdict(obj))

    deserialized_obj = ServiceRequest(**json.loads(serialized, object_pairs_hook=json_deserial_hook_datetime))

    assert obj == deserialized_obj
