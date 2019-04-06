

class Permutations:

    def permute(self, nums):

        self.lst = list()
        self.backtrack(self.lst, list(), nums)
        return self.lst

    def backtrack(self, lst, tmp_lst, nums):

        if len(tmp_lst) == len(nums):
            lst.append([i for i in tmp_lst])

        for i in range(len(nums)):

            if nums[i] not in tmp_lst:
                tmp_lst.append(nums[i])
                self.backtrack(lst, tmp_lst, nums)
                del tmp_lst[-1]


if __name__ == "__main__":

    print(Permutations().permute([1,2,3]))
