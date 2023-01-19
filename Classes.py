from dataclasses import dataclass
import numbers


@dataclass
class Potty:
    number: int
    name: str
    address: str
    cleanDayInt: int #This is an int so that I can easily reference the weekdayArray index for that day
    longitude: float
    latitude: float
    notes: str
    badAddress: bool

@dataclass
class Customer:
    name: str = ''
    ship2addy: str = ''
    bill2addy: str = ''
    useAddy: str = ''
    lng: float = None
    lat: float = None