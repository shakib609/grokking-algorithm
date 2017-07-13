from collections import deque

graph = {
    "Shakib": ["Moinul", "Shamim", "Salman"],
    "Shamim": ["Golam"],
    "Salman": ["Golam"],
    "Golam": ["Saiful"],
    "Moinul": []
}


def is_fruit_seller(name):
    return name == "Saiful"


def bfs_search_fruit_seller(name):
    searched = []
    search_list = deque()
    search_list += graph.get(name, [])
    while search_list:
        person = search_list.popleft()
        if person not in searched:
            if is_fruit_seller(person):
                print("{} is a fruit seller!".format(person))
                return True
            searched.append(person)
            search_list += graph[person]
    return False


if __name__ == '__main__':
    bfs_search_fruit_seller("Shakib")
