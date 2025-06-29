import time

class RateLimiter:
    def __init__(self, max_requests: int, per_seconds: int):
        self.max_requests = max_requests
        self.per_seconds = per_seconds
        self.clients = {}

    def allow_request(self, client_ip: str) -> bool:
        current_time = time.time()
        client_data = self.clients.get(client_ip)

        if not client_data:
            # First request from this IP
            self.clients[client_ip] = {"count": 1, "start_time": current_time}
            return True

        elapsed = current_time - client_data["start_time"]

        if elapsed > self.per_seconds:
            # Reset window
            self.clients[client_ip] = {"count": 1, "start_time": current_time}
            return True
        elif client_data["count"] < self.max_requests:
            self.clients[client_ip]["count"] += 1
            return True
        return False
