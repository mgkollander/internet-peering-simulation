import random

class ISP:
    def __init__(self, name):
        self.name = name
        self.peers = set()
        self.routing_table = {}

    def peer_with(self, other_isp, cost):
        if other_isp != self:
            self.peers.add(other_isp)
            other_isp.peers.add(self)
            self.routing_table[other_isp] = cost
            other_isp.routing_table[self] = cost

    def update_routing_table(self):
        for peer in self.peers:
            for dest, cost in peer.routing_table.items():
                if dest != self and (dest not in self.routing_table or cost + self.routing_table[peer] < self.routing_table[dest]):
                    self.routing_table[dest] = cost + self.routing_table[peer]

    def __repr__(self):
        return self.name

class InternetPeeringSimulation:
    def __init__(self, isp_count):
        self.isps = [ISP(f"ISP-{i}") for i in range(1, isp_count + 1)]
        self.network_topology = {}

    def randomly_peer_isps(self, num_peers):
        for _ in range(num_peers):
            isp1 = random.choice(self.isps)
            isp2 = random.choice([isp for isp in self.isps if isp != isp1])
            cost = random.randint(1, 10)  # Random cost for the link
            isp1.peer_with(isp2, cost)
            self.network_topology[(isp1, isp2)] = cost
            self.network_topology[(isp2, isp1)] = cost

    def simulate_routing(self, num_iterations):
        for _ in range(num_iterations):
            for isp in self.isps:
                isp.update_routing_table()

    def print_peering_status(self):
        for isp in self.isps:
            peers = ", ".join(peer.name for peer in isp.peers)
            print(f"{isp.name} is peering with: {peers}")

    def print_routing_table(self):
        for isp in self.isps:
            print(f"Routing table for {isp.name}: {isp.routing_table}")

if __name__ == "__main__":
    # Simulation parameters
    num_isps = 5
    num_peers = 2
    num_iterations = 3

    # Initialize simulation
    simulation = InternetPeeringSimulation(num_isps)
    simulation.randomly_peer_isps(num_peers)

    # Initial peering status
    print("Initial peering status:")
    simulation.print_peering_status()

    # Initial network topology
    print("\nInitial network topology:")
    print(simulation.network_topology)

    # Simulate routing updates
    simulation.simulate_routing(num_iterations)

    # Final peering status
    print("\nFinal peering status:")
    simulation.print_peering_status()

    # Final routing tables
    print("\nFinal routing tables:")
    simulation.print_routing_table()
