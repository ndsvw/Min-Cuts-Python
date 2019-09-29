import unittest

from min_cuts import union_vertices, count_probable_min_cuts


class MinCutsTest(unittest.TestCase):

    def test_union_vertices(self):
        # Test 1
        G = [
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        union_vertices(G, 0, 1)
        self.assertListEqual(G[0], [])
        self.assertListEqual(G[1], [2, 2])
        self.assertListEqual(G[2], [1, 1])

        # Test 2
        G = [
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        union_vertices(G, 0, 2)
        self.assertListEqual(G[0], [])
        self.assertListEqual(G[1], [2, 2])
        self.assertListEqual(G[2], [1, 1])

        # Test 3
        G = [
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        union_vertices(G, 2, 1)
        self.assertListEqual(G[0], [1, 1])
        self.assertListEqual(G[1], [0, 0])
        self.assertListEqual(G[2], [])

        # Test 4
        G = [
            [1, 2],
            [0, 3, 4],
            [0],
            [1, 4],
            [1, 3]
        ]
        union_vertices(G, 1, 3)
        self.assertSetEqual(set(G[0]), {3, 2})
        self.assertListEqual(G[1], [])
        self.assertListEqual(G[2], [0])
        self.assertTrue(all([
            G[3].count(4) == 2,
            G[3].count(0) == 1,
            len(G[3]) == 3
        ]))
        self.assertTrue(all([
            G[4].count(3) == 2,
            len(G[4]) == 2
        ]))

        # Test 5
        G = [
            [1, 2],
            [0, 3, 4],
            [0],
            [1, 4],
            [1, 3]
        ]
        union_vertices(G, 0, 2)
        self.assertListEqual(G[0], [])
        self.assertSetEqual(set(G[1]), {2, 3, 4})
        self.assertListEqual(G[2], [1])
        self.assertListEqual(G[3], [1, 4])
        self.assertListEqual(G[4], [1, 3])

    def test_count_probable_min_cuts(self):
        G = [
            [1, 2],
            [0, 2],
            [0, 1]
        ]
        self.assertTrue(count_probable_min_cuts(G) == 2)

        G = [
            [2],
            [2],
            [0, 1]
        ]
        self.assertTrue(count_probable_min_cuts(G) == 1)

        G = [
            [1, 2],
            [0, 3, 4],
            [0],
            [1, 4],
            [1, 3]
        ]
        self.assertTrue(count_probable_min_cuts(G) in [1, 2])

        G = [
            [],
            []
        ]
        self.assertTrue(count_probable_min_cuts(G) == 0)


if __name__ == "__main__":
    unittest.main()
