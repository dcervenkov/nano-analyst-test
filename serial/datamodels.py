from dataclasses import dataclass
from datetime import datetime


@dataclass
class ServiceRequest:
    country: str
    datetime_from: datetime
    datetime_to: datetime
    freq: str
    model_prefix: str
