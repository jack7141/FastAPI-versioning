from typing import Callable, Dict, List, Optional

from common.designpattern import SingletonMeta


class EventManager(metaclass=SingletonMeta):
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, listener: Callable):
        self._subscribers.setdefault(event_type, []).append(listener)

    def publish(self, event_type: str, data: Optional[dict] = None):
        for listener in self._subscribers.get(event_type, []):
            listener(data)


# Singleton instance of EventManager
event_manager = EventManager()


