import copy


class Solution:
    def numTrees(self, n):

        lst = [i for i in range(1, n + 1)]
        perms = self.getPerms(lst)

        _set = set()
        for p in perms:
            bst = self.bst(p)
            _set.add(self.bst_to_string(bst))

        return len(_set)

    def getPerms(self, n_lst):
        if len(n_lst) == 1:
            return [copy.copy(n_lst)]

        n_lst_c = copy.copy(n_lst)

        lst = []
        for i in n_lst:
            ind = n_lst_c.index(i)

            del n_lst_c[ind]
            res = self.getPerms(n_lst_c)
            for l in res:
                l.insert(0, i)
                lst.append(l)
            n_lst_c.insert(ind, i)

        return lst

    def findInd(self, value, lst):
        for i, val in enumerate(lst):
            if value == val:
                return i
        return -1

    def bst(self, lst):

        length = 2 ** len(lst)
        b = [None for _ in range(length)]
        b[0] = lst[0]
        root = 0
        for i, val in enumerate(lst[1:]):

            while True:
                if b[root] is None:
                    b[root] = val
                    break

                elif val < b[root]:
                    root = self.left(root)

                elif val > b[root]:
                    root = self.right(root)
            root = 0
        return b

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def bst_to_string(self, lst):

        for i in range(len(lst) - 1, 0, -1):
            if lst[i] is not None:
                break

            del lst[len(lst) - 1]

        result = "["
        p = 0
        while p < len(lst):

            if lst[p] is None:
                result += "null, "
                while p < len(lst) and lst[p] is None:
                    p += 1
                continue

            result += str(lst[p]) + ", "
            p += 1


        return result[:-2] + ']'
s = Solution()
solution = s.numTrees(3)
print("result: ", solution)
solution = s.numTrees(4)
print("result: ", solution)
solution = s.numTrees(5)
print("result: ", solution)
solution = s.numTrees(9)
print("result: ", solution)

# TODO: Optimize it now.