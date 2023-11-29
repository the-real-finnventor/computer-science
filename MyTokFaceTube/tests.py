import unittest
import base


class MyTokFaceTubeTests(unittest.TestCase):
    def setUp(self):
        self.MyTokFaceTubeGraph = base.SocialGraph()

    def setUpUsers(self):
        names = set([
            "Nina Stack",
            "Chang Kowalski",
            "Timothy Marquez",
            "Stephen Gibson",
            "Rose Harris",
            "Viktor Balnikov",
            "Jennifer Kim",
            "Shenzu Alvarez",
            "Ilina Brahmaputra-Marquez",
            "Maxwell Howard",
            "Wilbur Janke",
            "Daphne Merritt",
            "Shari Goldstein",
            "Mfuzi Iwanyi",
            "Lars Sjoberg",
            "Sonja Sjoberg",
            "Patton Sjoberg",
            "Lily Sjoberg",
            "Cesar Marquez",
            "Rodrigo Marquez",
            "Dashiell Gibson",
            "Kira Howard",
            "Kamoze Iwanyi",
            "Inez Marquez",
            "Violet Gibson",
            "Ronald Holtz",
            "Garth Grisan"
        ])
        self.users = {}
        for name in names:
            self.users[name] = self.MyTokFaceTubeGraph.AddUser(name)

    def setUpFriends(self):
        self.setUpUsers()
        friends = {
            "Chang Kowalski": [
                "Stephen Gibson",
                "Viktor Balnikov",
                "Daphne Merritt",
                "Rose Harris"
            ],
            "Stephen Gibson": [
                "Chang Kowalski",
                "Rose Harris",
                "Daphne Merritt",
                "Dashiell Gibson",
                "Violet Gibson",
                "Ronald Holtz"
            ],
            "Rose Harris": [
                "Chang Kowalski",
                "Stephen Gibson",
                "Jennifer Kim",
                "Daphne Merritt",
                "Dashiell Gibson",
                "Violet Gibson",
                "Ronald Holtz"
            ],
            "Viktor Balnikov": [
                "Chang Kowalski"
            ],
            "Jennifer Kim": [
                "Rose Harris",
                "Daphne Merritt",
                "Ronald Holtz"
            ],
            "Daphne Merritt": [
                "Rose Harris",
                "Jennifer Kim",
                "Ronald Holtz"
            ],
            "Lars Sjoberg": [
                "Sonja Sjoberg",
                "Patton Sjoberg",
                "Lily Sjoberg"
            ],
            "Sonja Sjoberg": [
                "Lars Sjoberg",
                "Patton Sjoberg",
                "Lily Sjoberg"
            ],
            "Patton Sjoberg": [
                "Lars Sjoberg",
                "Sonja Sjoberg",
                "Lily Sjoberg",
                "Cesar Marquez"
            ],
            "Lily Sjoberg": [
                "Lars Sjoberg",
                "Sonja Sjoberg",
                "Patton Sjoberg",
                "Cesar Marquez"
            ],
            "Cesar Marquez": [
                "Lily Sjoberg"
            ],
            "Rodrigo Marquez": [
                "Timothy Marquez",
                "Ilina Brahmaputra-Marquez"
            ],
            "Timothy Marquez": [
                "Rodrigo Marquez",
                "Ilina Brahmaputra-Marquez"
            ],
            "Dashiell Gibson": [
                "Stephen Gibson",
                "Rose Harris",
                "Kira Howard",
                "Violet Gibson",
                "Ronald Holtz"
            ],
            "Kira Howard": [
                "Rodrigo Marquez",
                "Dashiell Gibson",
                "Violet Gibson"
            ],
            "Kamoze Iwanyi": [
                "Inez Marquez",
                "Violet Gibson"
            ],
            "Inez Marquez": [
                "Kamoze Iwanyi",
                "Violet Gibson"
            ],
            "Ronald Holtz": [
                "Stephen Gibson",
                "Rose Harris",
                "Viktor Balnikov",
                "Jennifer Kim",
                "Daphne Merritt",
                "Dashiell Gibson"
            ]
        }
        self.edges = {}
        for name in friends:
            for friend in friends[name]:
                try:
                    newEdge = self.MyTokFaceTubeGraph.AddFriend(
                        self.users[name], self.users[friend])
                    self.edges[(name, friend)] = newEdge
                    self.edges[(friend, name)] = newEdge
                except base.SocialGraphError:
                    pass

    def test_add_user(self):
        self.MyTokFaceTubeGraph.AddUser("Finn")
        self.assertEqual(self.MyTokFaceTubeGraph.GetUsers().pop().name,
                         "Finn")

    def test_add_friend(self):
        self.setUpUsers()
        self.MyTokFaceTubeGraph.AddFriend(
            self.users["Dashiell Gibson"], self.users["Ronald Holtz"])
        self.assertEqual(self.MyTokFaceTubeGraph.GetEdges(
        ).pop().user1, self.users["Dashiell Gibson"])

    def test_get_users(self):
        self.setUpUsers()
        self.assertIn(
            self.MyTokFaceTubeGraph.GetUsers().pop().name, self.users.keys())

    def test_get_edges(self):
        self.setUpFriends()
        edge = self.MyTokFaceTubeGraph.GetEdges().pop()
        self.assertIn((edge.user1.name,
                      edge.user2.name), self.edges.keys())

    def test_find_path(self):
        self.setUpUsers()
        self.MyTokFaceTubeGraph.AddFriend(
            self.users["Dashiell Gibson"], self.users["Kira Howard"])
        pathUsers = self.MyTokFaceTubeGraph.FindPath(
            self.users["Dashiell Gibson"], self.users["Kira Howard"]).GetPathUsers()
        self.assertEqual([self.users["Dashiell Gibson"],
                         self.users["Kira Howard"]], pathUsers)

    def test_get_other(self):
        self.setUpUsers()
        edge = self.MyTokFaceTubeGraph.AddFriend(
            self.users["Dashiell Gibson"], self.users["Kira Howard"])
        self.assertEqual(edge.GetOther(
            self.users["Dashiell Gibson"]), self.users["Kira Howard"])

    def test_get_connected_users(self):
        self.setUpUsers()
        self.MyTokFaceTubeGraph.AddFriend(
            self.users["Dashiell Gibson"], self.users["Kira Howard"])
        self.assertIn(self.users["Dashiell Gibson"],
                      self.users["Kira Howard"].GetConnectedUsers())

    def test_how_far(self):
        self.setUpFriends()
        self.assertEqual(2, self.MyTokFaceTubeGraph.HowFar(
            self.users["Dashiell Gibson"], self.users["Jennifer Kim"]))

    def test_no_path_how_far(self):
        self.setUpUsers()
        self.assertIsNone(self.MyTokFaceTubeGraph.HowFar(
            self.users["Dashiell Gibson"], self.users["Jennifer Kim"]))

    def test_not_connected_how_far(self):
        self.setUpFriends()
        self.assertIsNone(self.MyTokFaceTubeGraph.HowFar(
            self.users["Dashiell Gibson"], self.users["Lily Sjoberg"]))

    def test_closer_friend(self):
        self.setUpFriends()
        self.assertEqual(self.MyTokFaceTubeGraph.CloserFriend(
            self.users["Dashiell Gibson"], self.users["Jennifer Kim"], self.users["Kira Howard"]), self.users["Kira Howard"])

    def test_no_path_closer_friend(self):
        self.setUpUsers()
        self.assertIsNone(self.MyTokFaceTubeGraph.CloserFriend(
            self.users["Dashiell Gibson"], self.users["Jennifer Kim"], self.users["Kira Howard"]))


if __name__ == "__main__":
    unittest.main()
