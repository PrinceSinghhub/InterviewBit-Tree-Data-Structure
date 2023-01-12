class BSTIterator:

    def __init__(self, root):
        self.stack = []
        self.root = root

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            self.stack.append(root.val)

        dfs(self.root)
        self.stack = sorted(self.stack, reverse=True)

    def next(self):
        """
        @return the next smallest number
        """

        if self.stack:
            return self.stack.pop()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        if self.stack:
            return True
        else:
            return False