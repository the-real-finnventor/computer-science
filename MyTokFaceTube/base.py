class SocialGraphError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))


class User:
    def __init__(self, name: str):
        self.name = name
        self.edges = set()

    def __str__(self) -> str:
        return self.name

    def __eq__(self, __value: object) -> bool:
        if type(__value) == str:
            return self.name == __value
        elif type(__value) == User:
            return self.name == __value.name
        else:
            return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return self.__str__()

    def GetConnectedUsers(self) -> set:
        rv = set()
        for edge in self.edges:
            rv.add(edge.GetOther(self))
        return rv


class Edge:
    def __init__(self, user1: User, user2: User):
        self.user1 = user1
        self.user2 = user2
        user1.edges.add(self)
        user2.edges.add(self)

    def __str__(self) -> str:
        return f"{self.user1} - {self.user2}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Edge:
            if self.user1 == __value.user1 and self.user2 == __value.user2:
                return True
            if self.user1 == __value.user2 and self.user2 == __value.user1:
                return True
        return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __hash__(self) -> int:
        return hash(self.user1)

    def GetOther(self, first: User) -> User:
        if self.user1 != first:
            return self.user1
        elif self.user2 != first:
            return self.user2


class Path:
    def findPath(self, curr: User, endUser: User, checked: set, currPath: list):
        # print()
        # print(curr.edges)
        # print(f"checked: {checked}")
        # print(f"checked: {[id(x) for x in checked]}")
        for edge in curr.edges:
            # print(edge)
            # print(currPath)
            # print(id(edge))
            # Skip all checked edges
            if edge in checked:
                continue
            # Check if we are done
            if edge.user1 == endUser or edge.user2 == endUser:
                currPath.append(edge)
                return currPath
            # Set up to call self.findPath again
            newCurrPath = currPath.copy()
            newCurrPath.append(edge)
            checked.add(edge)
            # Follow the path
            if edge.user1 != curr:
                return self.findPath(
                    edge.user1, endUser, checked, newCurrPath)
            else:
                return self.findPath(
                    edge.user2, endUser, checked, newCurrPath)
        # Failed to find path
        return None

    def __init__(self, startUser: User, endUser: User):
        self.path = self.findPath(startUser, endUser, set(), [])

    def GetPathEdges(self) -> list:
        return self.path

    def GetPathUsers(self) -> list:
        if len(self.path) == 1:
            return [self.path[0].user1, self.path[0].user2]
        lastUser = self.path[1]
        rv = []
        for edge in self.path:
            if edge.user1 == lastUser.user1:
                lastUser = edge.user1
            if edge.user1 == lastUser.user2:
                lastUser = edge.user1
            if edge.user2 == lastUser.user1:
                lastUser = edge.user2
            if edge.user2 == lastUser.user2:
                lastUser = edge.user2
            rv.append(lastUser)
        return rv

    def __str__(self) -> str:
        if self.path != None:
            return " > ".join(str(x) for x in self.path)
        return "None"

    def __eq__(self, __value: object) -> bool:
        if type(__value) == Path:
            return self.path == __value.path
        return False

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __hash__(self) -> int:
        return hash(self.path)

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self):
        self.curr_index = 0
        return self

    def __next__(self):
        self.curr_index += 1
        if len(self.path) == self.curr_index:
            raise StopIteration
        return self.path[self.curr_index - 1]


class SocialGraph:
    def __init__(self):
        self.users = set()
        self.edges = set()

    def AddUser(self, name: str) -> User:
        for user in self.users:
            if user.name == name:
                raise SocialGraphError("User already exists")
        newUser = User(name)
        self.users.add(newUser)
        return newUser

    def AddFriend(self, user1: User, user2: User) -> Edge:
        for edge in self.edges:
            if edge.user1 == user1 and edge.user2 == user2:
                raise SocialGraphError("Friendship already exists")
            elif edge.user2 == user1 and edge.user1 == user2:
                raise SocialGraphError("Friendship already exists")
        if user1 == user2:
            raise SocialGraphError("You can't friend yourself")
        newEdge = Edge(user1, user2)
        self.edges.add(newEdge)
        return newEdge

    def GetUsers(self) -> set:
        return self.users

    def GetEdges(self) -> set:
        return self.edges

    def FindPath(self, startUser: User, endUser: User) -> Path:
        if startUser == endUser:
            raise SocialGraphError("Cannot find a path to self")
        return Path(startUser, endUser)

    def CloserFriend(self, start: User, friend1: User, friend2: User) -> User | None:
        far1 = self.HowFar(start, friend1)
        far2 = self.HowFar(start, friend2)
        if far1 and far2:
            if far1 < far2:
                return friend1
            if far2 < far1:
                return friend2

    def HowFar(self, start: User, end: User) -> int | None:
        visited = set()
        frontier = start.GetConnectedUsers()
        last_frontier = set()
        steps = 1
        while frontier:
            if end in frontier:
                return steps
            last_frontier = frontier
            frontier = set()
            for user in last_frontier:
                visited.add(user)
                for connectedUser in user.GetConnectedUsers():
                    if connectedUser not in visited:
                        frontier.add(connectedUser)
            steps += 1
