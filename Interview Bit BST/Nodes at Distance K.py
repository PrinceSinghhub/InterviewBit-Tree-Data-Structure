from collections import deque


class Solution:
    target = None

    def dfs(self, node, par=None):
        if node:
            node.par = par
            self.dfs(node.left, node)
            self.dfs(node.right, node)

    def bfs(self, src, x):
        if (src):
            if (src.val == x):
                self.target = src
            self.bfs(src.left, x)
            self.bfs(src.right, x)

    def distanceK(self, A, B, C):
        root = A
        self.dfs(root)
        self.bfs(root, B)
        if (self.target == None):
            print(B)
        queue = deque([(self.target, 0)])
        seen = {self.target, None}
        while queue:
            if queue[0][1] == C:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))
        return []