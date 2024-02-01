from common.events import event_manager


def subscribe_to(event_type: str):
    def decorator(func):
        event_manager.subscribe(event_type, func)
        return func

    return decorator