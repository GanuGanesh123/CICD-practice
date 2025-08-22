class Server:
    def __init__(self, ip):
        self.ip = ip

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

# Example usage
servers = [Server("192.168.1.1"), Server("192.168.1.2"), Server("192.168.1.3")]
load_balancer = LoadBalancer(servers)

for _ in range(6):
    server = load_balancer.get_next_server()
    print(f"Forwarding request to {server.ip}")