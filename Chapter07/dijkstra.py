graph = {
    "start": {
        "a": 6,
        "b": 2,
    },
    "a": {
        "finish": 1
    },
    "b": {
        "a": 3,
        "finish": 5
    },
    "finish": {}
}


costs = {
    "a": graph["start"].get("a"),
    "b": graph["start"].get("b"),
    "finish": float("inf")
}


parents = {
    "a": "start",
    "b": "start",
    "finish": None
}

processed = ["start"]


def find_lowest_cost_node(costs):
    lowest = float("inf")
    lowest_cost_node = None
    for node in costs:
        temp = costs[node]
        if node not in processed and lowest > temp:
            lowest = temp
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        neighbours = graph.get(node)
        cost = costs.get(node)
        for n in neighbours:
            new_cost = cost + neighbours.get(n)
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    k = "finish"
    path = [k]
    while k != "start":
        v = parents.get(k)
        path.append(v)
        k = v
    path.reverse()
    print(path)
    print(costs["finish"])


if __name__ == '__main__':
    dijkstra()
